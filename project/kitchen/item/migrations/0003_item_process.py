# Generated by Django 4.2.1 on 2023-06-05 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='process',
            field=models.TextField(blank=True, null=True),
        ),
    ]