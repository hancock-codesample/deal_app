from rest_framework import serializers

from deal_app.portfolios.models import Portfolio


class PortfolioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portfolio

        fields = [
            'name',
            'unit_cashflow_criteria',
            'uuid'
        ]
