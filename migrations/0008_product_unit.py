# Generated by Django 3.2.3 on 2021-09-08 05:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('kg', 'kg'), ('litre', 'litre')], default=django.utils.timezone.now, max_length=7),
            preserve_default=False,
        ),
    ]
