# Generated by Django 3.2.5 on 2021-08-03 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0002_answer_questioncomponent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='correct',
            new_name='is_correct',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='answer_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='questioncomponent',
            old_name='question_component_text',
            new_name='text',
        ),
    ]
