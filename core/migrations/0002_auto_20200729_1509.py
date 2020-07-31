# Generated by Django 3.0.8 on 2020-07-29 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='favorited_by',
            field=models.ManyToManyField(blank=True, related_name='favorite_photos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo_photos/'),
        ),
        migrations.AddField(
            model_name='photo',
            name='public',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('public', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to=settings.AUTH_USER_MODEL)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='core.Photo')),
            ],
        ),
    ]
