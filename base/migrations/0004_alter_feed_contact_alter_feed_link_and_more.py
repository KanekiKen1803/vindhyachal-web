# Generated by Django 4.0 on 2022-01-05 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_notice_description_alter_post_type_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='contact',
            field=models.TextField(default=0, help_text='leave blank if not event feed', max_length=100),
        ),
        migrations.AlterField(
            model_name='feed',
            name='link',
            field=models.URLField(blank=True, help_text='leave blank if not event feed'),
        ),
        migrations.AlterField(
            model_name='feed',
            name='location',
            field=models.TextField(blank=True, help_text='leave blank if not event feed', max_length=100),
        ),
        migrations.AlterField(
            model_name='feed',
            name='timing',
            field=models.TextField(blank=True, help_text='leave blank if not event feed', max_length=100),
        ),
    ]