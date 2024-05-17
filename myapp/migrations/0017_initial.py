# Generated by Django 5.0.3 on 2024-05-04 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0016_delete_layoutdetals'),
    ]

    operations = [
        migrations.CreateModel(
            name='LayoutDetals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('layout_name', models.CharField(max_length=100)),
                ('layout_image', models.ImageField(upload_to='layout_images/')),
            ],
        ),
        migrations.CreateModel(
            name='TableDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('binserial_no', models.CharField(max_length=100)),
                ('bin_location', models.CharField(max_length=100)),
                ('projectname', models.CharField(max_length=100)),
                ('component1', models.CharField(max_length=100)),
                ('component2', models.CharField(max_length=100)),
                ('employeecode', models.CharField(max_length=100)),
                ('layout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.layoutdetals')),
            ],
        ),
    ]
