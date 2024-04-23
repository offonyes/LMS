# Generated by Django 5.0.4 on 2024-04-22 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='subjects',
        ),
        migrations.AddField(
            model_name='subject',
            name='subjects',
            field=models.ManyToManyField(blank=True, limit_choices_to={'id__lte': 7}, to='universities_app.subject', verbose_name='Subject'),
        ),
    ]
