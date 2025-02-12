# Generated by Django 3.1.6 on 2021-02-23 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backlog_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BacklogItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
                ('anime', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backlog_manager.anime')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backlog_manager.books')),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backlog_manager.games')),
                ('movie_tv', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backlog_manager.movietv')),
            ],
        ),
        migrations.RemoveField(
            model_name='backlogbook',
            name='book',
        ),
        migrations.RemoveField(
            model_name='backlogbook',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='backloggame',
            name='game',
        ),
        migrations.RemoveField(
            model_name='backloggame',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='backlogmovietv',
            name='movie_tv',
        ),
        migrations.RemoveField(
            model_name='backlogmovietv',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='backlog',
            name='anime',
        ),
        migrations.RemoveField(
            model_name='backlog',
            name='books',
        ),
        migrations.RemoveField(
            model_name='backlog',
            name='games',
        ),
        migrations.RemoveField(
            model_name='backlog',
            name='movies_tv',
        ),
        migrations.RemoveField(
            model_name='backlog',
            name='order',
        ),
        migrations.DeleteModel(
            name='BacklogAnime',
        ),
        migrations.DeleteModel(
            name='BacklogBook',
        ),
        migrations.DeleteModel(
            name='BacklogGame',
        ),
        migrations.DeleteModel(
            name='BacklogMovieTV',
        ),
        migrations.AddField(
            model_name='backlogitem',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backlog_manager.backlog'),
        ),
        migrations.AlterUniqueTogether(
            name='backlogitem',
            unique_together={('plan', 'order')},
        ),
    ]
