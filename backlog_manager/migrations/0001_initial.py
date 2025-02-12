# Generated by Django 3.1.6 on 2021-02-17 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('comment', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Backlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GameGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='MovieTV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('comment', models.TextField(null=True)),
                ('genre', models.ManyToManyField(to='backlog_manager.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('comment', models.TextField(null=True)),
                ('genre', models.ManyToManyField(to='backlog_manager.GameGenre')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('comment', models.TextField(null=True)),
                ('genre', models.ManyToManyField(to='backlog_manager.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='BacklogMovieTV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('p', 'Planned'), ('o', 'Ongoing'), ('d', 'Done')], default='p', max_length=1)),
                ('movie_tv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backlog_manager.movietv')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backlog_manager.backlog')),
            ],
        ),
        migrations.CreateModel(
            name='BacklogGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('p', 'Planned'), ('o', 'Ongoing'), ('d', 'Done')], default='p', max_length=1)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backlog_manager.games')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backlog_manager.backlog')),
            ],
        ),
        migrations.CreateModel(
            name='BacklogBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('p', 'Planned'), ('o', 'Ongoing'), ('d', 'Done')], default='p', max_length=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backlog_manager.books')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backlog_manager.backlog')),
            ],
        ),
        migrations.CreateModel(
            name='BacklogAnime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('p', 'Planned'), ('o', 'Ongoing'), ('d', 'Done')], default='p', max_length=1)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backlog_manager.anime')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backlog_manager.backlog')),
            ],
        ),
        migrations.AddField(
            model_name='backlog',
            name='anime',
            field=models.ManyToManyField(through='backlog_manager.BacklogAnime', to='backlog_manager.Anime'),
        ),
        migrations.AddField(
            model_name='backlog',
            name='books',
            field=models.ManyToManyField(through='backlog_manager.BacklogBook', to='backlog_manager.Books'),
        ),
        migrations.AddField(
            model_name='backlog',
            name='games',
            field=models.ManyToManyField(through='backlog_manager.BacklogGame', to='backlog_manager.Games'),
        ),
        migrations.AddField(
            model_name='backlog',
            name='movies_tv',
            field=models.ManyToManyField(through='backlog_manager.BacklogMovieTV', to='backlog_manager.MovieTV'),
        ),
        migrations.AddField(
            model_name='backlog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='anime',
            name='genre',
            field=models.ManyToManyField(to='backlog_manager.Genre'),
        ),
    ]
