# Generated by Django 3.1.6 on 2021-02-28 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backlog_manager', '0003_auto_20210223_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='backlogitem',
            name='status',
            field=models.CharField(choices=[('p', 'Planned'), ('o', 'Ongoing'), ('d', 'Done')], default='p', max_length=1),
        ),
    ]
