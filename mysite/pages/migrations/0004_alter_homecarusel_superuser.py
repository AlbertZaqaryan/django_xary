# Generated by Django 4.1.6 on 2023-02-08 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_homecarusel_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecarusel',
            name='superuser',
            field=models.ImageField(blank=True, upload_to='media', verbose_name='HomeCarusel superuser image'),
        ),
    ]
