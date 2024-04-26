# Generated by Django 5.0.4 on 2024-04-26 13:28

import django.db.models.deletion
import universities_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities_app', '0004_alter_subject_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_file', models.FileField(upload_to='Assignments/', verbose_name='Assignment file')),
                ('description', models.TextField(verbose_name='Description')),
                ('deadline', models.DateTimeField(verbose_name='Deadline')),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universities_app.lecturer', verbose_name='Lecturer')),
            ],
            options={
                'verbose_name': 'Assignment',
                'verbose_name_plural': 'Assignments',
            },
        ),
        migrations.CreateModel(
            name='AssignmentResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_note', models.TextField(verbose_name='Student Note')),
                ('submit_date', models.DateTimeField(verbose_name='Submit Date')),
                ('assignment_file', models.FileField(upload_to=universities_app.models.user_directory_path, verbose_name='Assignment file')),
                ('parent_assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universities_app.assignment', verbose_name='Parent assignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universities_app.student', verbose_name='Student')),
            ],
            options={
                'verbose_name': 'Assignment response',
                'verbose_name_plural': 'Assignment responses',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('attended', models.BooleanField(default=False, verbose_name='Attended')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universities_app.student', verbose_name='Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universities_app.subject', verbose_name='Subject')),
            ],
        ),
    ]
