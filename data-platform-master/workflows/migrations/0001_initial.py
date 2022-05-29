# Generated by Django 3.2.6 on 2021-08-07 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('none', 'none'), ('running', 'running'), ('failed', 'failed'), ('stopped', 'stopped')], max_length=10)),
            ],
        ),
    ]
