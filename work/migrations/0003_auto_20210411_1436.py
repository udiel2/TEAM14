# Generated by Django 3.1.7 on 2021-04-11 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='level',
            field=models.CharField(choices=[(1, 'Junior'), (2, 'Senior'), (3, 'expert')], default=(1, 'Junior'), max_length=6),
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateField()),
                ('endTime', models.DateField()),
                ('allTasks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.task')),
            ],
        ),
    ]
