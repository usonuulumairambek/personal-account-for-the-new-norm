# Generated by Django 3.1.5 on 2021-05-07 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excelfile',
            name='category',
            field=models.CharField(blank=True, choices=[('clothes', 'Одежда'), ('shoes', 'Обувь'), ('perfume', 'Парфюм')], max_length=64, null=True),
        ),
    ]
