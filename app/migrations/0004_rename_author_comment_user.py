# Generated by Django 4.1.5 on 2023-02-27 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_comment_author_alter_comment_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='user',
        ),
    ]
