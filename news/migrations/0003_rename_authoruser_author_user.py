# Generated by Django 5.0.6 on 2024-06-19 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_remove_category_subscribers_alter_comment_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='authorUser',
            new_name='user',
        ),
    ]
