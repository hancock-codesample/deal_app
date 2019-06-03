from rest_framework import serializers

from deal_app.properties.models import Property, PropertyPurchase, PropertyIncome


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property

        fields = [
            'portfolio',
            'street_address',
            'city',
            'zip_code',
            'state',
            'estimated_value',
            'last_price',
            'mls_number',
            'prop_tax',
            'bedrooms',
            'uuid'
        ]


class PropertyIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyIncome

        fields = [
            'property',
            'gross_monthly_rent',
            'electricity',
            'water_sewer',
            'pmi',
            'garbage',
            'hoas',
            'monthly_insurance',
            'vacancy_percent',
            'maintenance',
            'capex',
            'management_fees_percent',
            'annual_income_growth',
            'annual_appreciation',
            'annual_expense_growth',
            'uuid',
        ]


class PropertyPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyPurchase

        fields = [
            'portfolio',
            'street_address',
            'city',
            'zip_code',
            'state',
            'estimated_value',
            'last_price',
            'mls_number',
            'prop_tax',
            'bedrooms',
            'uuid'
        ]
