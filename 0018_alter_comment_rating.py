# Generated by Django 4.2 on 2023-05-09 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_alter_comment_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
