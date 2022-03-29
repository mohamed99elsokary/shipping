# Generated by Django 4.0.3 on 2022-03-29 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='media/')),
                ('is_sea_freight', models.BooleanField()),
                ('is_land_shipping', models.BooleanField()),
                ('is_customs_clearance', models.BooleanField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(choices=[('sea freight', 'sea freight'), ('land_shipping', 'land shipping'), ('custom clearance', 'custom clearance')], max_length=50)),
                ('price', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_pricing', to='company.company')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.material')),
            ],
        ),
    ]
