# Generated by Django 4.0.5 on 2022-06-03 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0003_delete_jsonfiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadJsonForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
