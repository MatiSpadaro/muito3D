# Generated by Django 4.2.5 on 2023-09-12 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app3D', '0004_productos_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedidos',
            old_name='filamento',
            new_name='material',
        ),
    ]
