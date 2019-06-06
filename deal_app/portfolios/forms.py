from django import forms
from django.utils.translation import ugettext_lazy as _
from deal_app.portfolios.models import Portfolio
from crispy_forms.helper import FormHelper


class PortfolioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PortfolioForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

    class Meta:
        model = Portfolio
        fields = ('name', 'unit_cashflow_criteria')
        exclude = ['user']
        labels = {
            'name': _('Portfolio Name'),
            'unit_cashflow_criteria': _('Per unit cash flow criteria')
        }
