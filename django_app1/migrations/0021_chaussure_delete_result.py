# Generated by Django 5.0.3 on 2024-03-28 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app1', '0020_alter_company_location_alter_company_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chaussure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('product_url', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Result',
        ),
    ]