# Generated by Django 3.2.23 on 2024-01-30 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20231228_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/defalt.jpg', upload_to='blog/'),
        ),
    ]