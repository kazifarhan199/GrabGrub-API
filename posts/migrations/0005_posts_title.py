# Generated by Django 4.1.3 on 2022-11-25 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_posts_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='title',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]