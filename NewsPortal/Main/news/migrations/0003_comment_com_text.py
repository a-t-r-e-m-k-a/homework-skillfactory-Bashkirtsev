# Generated by Django 4.2.6 on 2023-10-13 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_comment_create_date_alter_post_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='com_text',
            field=models.TextField(default='...'),
        ),
    ]
