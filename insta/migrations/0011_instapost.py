# Generated by Django 2.2.1 on 2019-05-02 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0010_auto_20190427_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstaPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='')),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='insta_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
