# Generated by Django 4.1.6 on 2023-02-08 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_homecarusel_superuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='HomeTopic name')),
                ('img', models.ImageField(upload_to='media', verbose_name='HomeTopic image')),
                ('info', models.CharField(max_length=15, verbose_name='HomeTopic info1')),
            ],
        ),
    ]