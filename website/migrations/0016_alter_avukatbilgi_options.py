# Generated by Django 3.2.7 on 2022-02-23 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_rename_avukatlarimiz_avukatbilgi'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='avukatbilgi',
            options={'verbose_name_plural': 'Avukatlarımız'},
        ),
    ]