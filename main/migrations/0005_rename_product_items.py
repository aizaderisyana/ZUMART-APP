# Generated by Django 4.2.5 on 2023-09-15 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_product_appname_alter_product_kelas_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Items',
        ),
    ]
