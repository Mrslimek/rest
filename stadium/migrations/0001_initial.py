# Generated by Django 5.1.2 on 2024-11-05 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория услуги',
                'verbose_name_plural': 'Категории услуг',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название услуги')),
                ('image', models.ImageField(upload_to='./stadium', verbose_name='Картинка')),
                ('description', models.TextField(verbose_name='Описание')),
                ('best', models.BooleanField(default=False, verbose_name='Продвигаемая')),
                ('service_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stadium.servicecategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Услуги',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Subservice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название подуслуги')),
                ('unit', models.CharField(max_length=255, verbose_name='Единицы измерения')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Цена')),
                ('type_of_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stadium.service', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Подуслуги',
                'verbose_name_plural': 'Подуслуги',
            },
        ),
    ]
