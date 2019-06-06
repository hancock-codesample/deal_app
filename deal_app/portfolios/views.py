from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, UpdateView, ListView, DeleteView, TemplateView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect

from deal_app.portfolios.forms import PortfolioForm
from deal_app.portfolios.models import Portfolio


class PortfolioCreateView(CreateView):
    form_class = PortfolioForm
    template_name = 'portfolios/portfolio_create.html'
    model = Portfolio

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


portfolio_create_view = PortfolioCreateView.as_view()


class PortfolioListView(LoginRequiredMixin, ListView):
    model = Portfolio

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


portfolio_list_view = PortfolioListView.as_view()


class PortfolioDetailView(LoginRequiredMixin, DetailView):
    model = Portfolio


portfolio_detail_view = PortfolioDetailView.as_view()


class PortfolioUpdateView(LoginRequiredMixin, UpdateView):
    model = Portfolio
    form_class = PortfolioForm


portfolio_update_view = PortfolioUpdateView.as_view()


class PortfolioDeleteView(LoginRequiredMixin, DeleteView):
    model = Portfolio
    success_url = reverse_lazy('portfolios:list')


portfolio_delete_view = PortfolioDeleteView.as_view()


def confirm_portfolio_delete_view(request, id):
    portfolio = get_object_or_404(Portfolio, id=id)
    if request.method == "POST":
        portfolio.delete()
        return redirect('portfolios:detail')
    context = {
        "portfolio": portfolio
    }
    return render(request, "portfolios/portfolio_confirm_delete.html", context)
