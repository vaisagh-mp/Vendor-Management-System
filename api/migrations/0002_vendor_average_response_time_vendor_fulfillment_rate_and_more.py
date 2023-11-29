# Generated by Django 4.2.7 on 2023-11-26 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='average_response_time',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='vendor',
            name='fulfillment_rate',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='vendor',
            name='on_time_delivery_rate',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='vendor',
            name='quality_rating_avg',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='contact_details',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_number', models.CharField(max_length=100, unique=True)),
                ('order_date', models.DateTimeField()),
                ('delivery_date', models.DateTimeField()),
                ('items', models.JSONField()),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
                ('quality_rating', models.FloatField(blank=True, null=True)),
                ('issue_date', models.DateTimeField()),
                ('acknowledgment_date', models.DateTimeField(blank=True, null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vendor')),
            ],
        ),
    ]