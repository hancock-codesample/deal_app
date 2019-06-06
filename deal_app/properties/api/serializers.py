from rest_framework import serializers

from deal_app.properties.models import Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"

"""
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
"""
