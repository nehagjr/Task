# Generated by Django 5.0.4 on 2024-04-11 08:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManagerApp', '0003_alter_task_task_type_alter_user_taskdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='taskDetail',
        ),
        migrations.AddField(
            model_name='user',
            name='tasktype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='TaskManagerApp.task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='Task_Type',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Done', 'Done')], max_length=50),
        ),
    ]
