# Generated by Django 4.2.4 on 2024-10-10 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LinkServicesOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mining_order_id', models.IntegerField()),
                ('mining_service_id', models.IntegerField()),
                ('square', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'link_services_orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MiningOrder',
            fields=[
                ('mining_order_id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('formation_date', models.DateTimeField(blank=True, null=True)),
                ('company_name', models.TextField(blank=True, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('mining_start_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.TextField()),
                ('creator_id', models.IntegerField(blank=True, null=True)),
                ('moderator_id', models.IntegerField(blank=True, null=True)),
                ('moderation_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mining_order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MiningService',
            fields=[
                ('mining_service_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(unique=True)),
                ('description', models.TextField(unique=True)),
                ('status', models.TextField()),
                ('url', models.TextField(unique=True)),
                ('long_description', models.TextField(unique=True)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mining_service',
                'managed': False,
            },
        ),
    ]
