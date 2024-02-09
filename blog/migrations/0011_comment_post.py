# Generated by Django 5.0.2 on 2024-02-08 21:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
            preserve_default=False,
        ),
    ]