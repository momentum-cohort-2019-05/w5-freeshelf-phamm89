# Generated by Django 2.2.2 on 2019-06-28 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_load_samplebooks'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['book_category'], 'verbose_name_plural': 'categories'},
        ),
    ]