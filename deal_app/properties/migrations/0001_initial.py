# Generated by Django 2.2.1 on 2019-06-06 19:35

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('portfolios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('zip_code', models.IntegerField()),
                ('state', models.CharField(max_length=20)),
                ('number_units', models.IntegerField(blank=True, null=True)),
                ('estimated_value', models.FloatField(blank=True, null=True)),
                ('last_price', models.FloatField(blank=True, null=True)),
                ('mls_number', models.CharField(blank=True, max_length=100, null=True)),
                ('prop_tax', models.FloatField(blank=True, null=True)),
                ('bedrooms', models.IntegerField(blank=True, null=True)),
                ('prop_type', models.CharField(choices=[('SFH', 'Single Family Home'), ('DUP', 'Duplex'), ('TRP', 'Triplex'), ('FRP', 'Fourplex'), ('MF', 'Multi-Family')], default='SFH', max_length=3)),
                ('purchase_price', models.FloatField()),
                ('date_acquired', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('after_repair_value', models.FloatField(default=models.FloatField())),
                ('closing_cost_general', models.FloatField(blank=True, null=True)),
                ('estimated_repair_general', models.FloatField(blank=True, null=True)),
                ('cash_deal', models.BooleanField(default=False)),
                ('down_payment_percent', models.FloatField(blank=True, null=True)),
                ('loan_interest_rate', models.FloatField(blank=True, null=True)),
                ('lender_points', models.FloatField(blank=True, null=True)),
                ('misc_lender_charges', models.FloatField(blank=True, null=True)),
                ('years_amortized', models.FloatField()),
                ('gross_monthly_rent', models.FloatField(blank=True, null=True)),
                ('monthly_mortgage_cost', models.FloatField(blank=True, null=True)),
                ('electricity', models.FloatField(blank=True, null=True)),
                ('water_sewer', models.FloatField(blank=True, null=True)),
                ('pmi', models.FloatField(blank=True, null=True)),
                ('garbage', models.FloatField(blank=True, null=True)),
                ('hoas', models.FloatField(blank=True, null=True)),
                ('monthly_insurance', models.FloatField(blank=True, null=True)),
                ('vacancy_percent', models.FloatField(blank=True, null=True)),
                ('maintenance', models.FloatField(blank=True, null=True)),
                ('capex', models.FloatField(blank=True, null=True)),
                ('management_fees_percent', models.FloatField(blank=True, null=True)),
                ('annual_income_growth', models.FloatField(blank=True, null=True)),
                ('annual_appreciation', models.FloatField(blank=True, null=True)),
                ('annual_expense_growth', models.FloatField(blank=True, null=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolios.Portfolio')),
            ],
            options={
                'verbose_name_plural': 'Properties',
            },
        ),
    ]
