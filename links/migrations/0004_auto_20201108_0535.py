# Generated by Django 2.1.4 on 2020-11-08 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_vote'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['description']},
        ),
    ]
