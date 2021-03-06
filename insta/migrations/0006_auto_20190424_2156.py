# Generated by Django 2.2 on 2019-04-24 21:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0005_auto_20190424_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instauser',
            name='profile_pic',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='static/images/profiles'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='static/images/posts'),
        ),
        migrations.CreateModel(
            name='UserConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('following', models.ManyToManyField(related_name='following', to=settings.AUTH_USER_MODEL)),
                ('instaUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connection', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
