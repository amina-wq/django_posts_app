# Generated by Django 4.2.1 on 2023-08-25 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField(verbose_name='comments to the post')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField(verbose_name='comment')),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
            ],
            options={
                'verbose_name': 'Post comment',
                'verbose_name_plural': 'Post comments',
                'ordering': ('-date_time', 'post_id'),
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('description', models.TextField(verbose_name='description')),
                ('is_moderate', models.BooleanField(default=False, verbose_name='is moderated')),
            ],
            options={
                'verbose_name': 'Publication',
                'verbose_name_plural': 'Publication',
                'ordering': ('-date_time', 'title'),
            },
        ),
        migrations.CreateModel(
            name='PostRatings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default='False')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.posts')),
            ],
            options={
                'verbose_name': 'Post rating',
                'verbose_name_plural': 'Posts ratings',
                'ordering': ('-post', 'author'),
            },
        ),
    ]