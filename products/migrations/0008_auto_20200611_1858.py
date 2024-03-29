# Generated by Django 3.0.4 on 2020-06-11 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200605_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutomotiveLubricants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, null=True)),
                ('description_long', models.TextField(max_length=600, null=True)),
                ('description_short', models.TextField(max_length=150, null=True)),
                ('category', models.CharField(choices=[('Engine Oil', 'Engine Oil'), ('Gear Oil', 'Gear Oil')], max_length=200, null=True)),
                ('image_1', models.ImageField(blank=True, upload_to='product_image/')),
                ('image_2', models.ImageField(blank=True, upload_to='product_image/')),
                ('image_3', models.ImageField(blank=True, upload_to='product_image/')),
            ],
        ),
        migrations.CreateModel(
            name='IndustrialLubricants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, null=True)),
                ('description_long', models.TextField(max_length=600, null=True)),
                ('description_short', models.TextField(max_length=150, null=True)),
                ('category', models.CharField(choices=[('Metal Working Fluids', 'Metal Working Fluids'), ('Compressor Oil', 'Compressor Oil'), ('Rust Preventive Oil', 'Rust Preventive Oil'), ('Aluminium Wire Drawing oil', 'Aluminium Wire Drawing oil'), ('Hydraulic Oil', 'Hydraulic Oil')], max_length=200, null=True)),
                ('image_1', models.ImageField(blank=True, upload_to='product_image/')),
                ('image_2', models.ImageField(blank=True, upload_to='product_image/')),
                ('image_3', models.ImageField(blank=True, upload_to='product_image/')),
            ],
        ),
        migrations.CreateModel(
            name='Sulfonates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, null=True)),
                ('description_long', models.TextField(max_length=600, null=True)),
                ('description_short', models.TextField(max_length=150, null=True)),
                ('category', models.CharField(choices=[('Sodium Petroleum Sulfonate', 'Sodium Petroleum Sulfonate'), ('Calcium Petroleum Sulfonate', 'Calcium Petroleum Sulfonate'), ('Barium Petroleum Sulfonate', 'Barium Petroleum Sulfonate')], max_length=200, null=True)),
                ('image_1', models.ImageField(blank=True, upload_to='product_image/')),
                ('image_2', models.ImageField(blank=True, upload_to='product_image/')),
                ('image_3', models.ImageField(blank=True, upload_to='product_image/')),
            ],
        ),
        migrations.CreateModel(
            name='Textile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, null=True)),
                ('description_long', models.TextField(max_length=600, null=True)),
                ('description_short', models.TextField(max_length=150, null=True)),
                ('image_1', models.ImageField(blank=True, upload_to='product_image/')),
                ('image_2', models.ImageField(blank=True, upload_to='product_image/')),
                ('image_3', models.ImageField(blank=True, upload_to='product_image/')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
