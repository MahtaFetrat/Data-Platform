# Generated by Django 3.2.6 on 2021-08-17 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflows', '0010_auto_20210816_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='workflow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflow'),
        ),
    ]