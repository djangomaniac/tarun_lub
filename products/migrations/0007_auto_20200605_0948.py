# Generated by Django 3.0.4 on 2020-06-05 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200605_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description_long',
            field=models.TextField(max_length=600, null=True),
        ),
    ]