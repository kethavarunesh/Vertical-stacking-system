# Generated by Django 5.0.3 on 2024-05-04 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
    ]
