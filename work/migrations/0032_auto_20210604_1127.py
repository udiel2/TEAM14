# Generated by Django 3.1.7 on 2021-06-04 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0031_remove_comment_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='Description',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='sprint',
            name='Descripion',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='Description',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='Description',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
