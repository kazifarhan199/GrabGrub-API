# Generated by Django 4.0.2 on 2022-11-14 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_tracklikes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracklikes',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.posts'),
        ),
    ]
