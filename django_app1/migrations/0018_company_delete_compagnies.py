# Generated by Django 5.0.3 on 2024-03-19 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app1', '0017_compagnies_delete_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('sector', models.CharField(max_length=255, verbose_name='Sector')),
                ('location', models.CharField(max_length=255, verbose_name='Location')),
                ('url_posts', models.URLField(verbose_name='URL Posts')),
                ('num_posts', models.CharField(max_length=255, verbose_name='Number of Posts')),
            ],
        ),
        migrations.DeleteModel(
            name='Compagnies',
        ),
    ]
