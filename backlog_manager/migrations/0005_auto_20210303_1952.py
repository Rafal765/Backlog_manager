# Generated by Django 3.1.6 on 2021-03-03 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backlog_manager', '0004_backlogitem_status'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='backlogitem',
            unique_together=set(),
        ),
    ]
