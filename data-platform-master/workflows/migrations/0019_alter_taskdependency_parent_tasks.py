# Generated by Django 3.2.6 on 2021-08-25 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflows', '0018_taskdependency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdependency',
            name='parent_tasks',
            field=models.ManyToManyField(blank=True, related_name='_workflows_taskdependency_parent_tasks_+', to='workflows.TaskDependency'),
        ),
    ]
