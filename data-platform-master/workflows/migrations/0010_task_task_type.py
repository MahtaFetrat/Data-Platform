# Generated by Django 3.2.6 on 2021-08-17 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflows', '0009_alter_task_workflow'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_type',
            field=models.CharField(choices=[('N', 'None'), ('DC', 'Docker'), ('PY', 'Python')], default='N', max_length=2),
        ),
    ]
