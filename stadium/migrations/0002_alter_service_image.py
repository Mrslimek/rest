# Generated by Django 5.1.2 on 2024-11-12 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stadium', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='./stadium', verbose_name='Картинка'),
        ),
    ]
