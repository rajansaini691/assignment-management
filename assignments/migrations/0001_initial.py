# Generated by Django 3.2.5 on 2021-08-28 06:52

import assignments.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssignmentTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema', models.JSONField(default=assignments.models.assignment_default, max_length=3000)),
                ('title', models.CharField(default='title', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema', models.JSONField(default=assignments.models.assignment_default, max_length=3000)),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.assignmenttemplate')),
            ],
        ),
    ]
