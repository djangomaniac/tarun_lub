# Generated by Django 3.0.4 on 2020-06-12 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200611_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='textile',
            name='category',
            field=models.CharField(choices=[('Knitting Oil', 'Knitting Oil')], max_length=200, null=True),
        ),
    ]
