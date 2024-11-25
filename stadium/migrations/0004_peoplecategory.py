# Generated by Django 5.1.2 on 2024-11-15 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stadium', '0003_alter_service_title_alter_servicecategory_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeopleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('category_user', models.ManyToManyField(to='stadium.servicecategory')),
            ],
            options={
                'verbose_name': 'Пользователь категории',
                'verbose_name_plural': 'Пользователи категорий',
            },
        ),
    ]
