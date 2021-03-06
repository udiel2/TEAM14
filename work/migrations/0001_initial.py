# Generated by Django 3.1.7 on 2021-04-05 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[(1, 'Java'), (2, 'C'), (3, 'C++'), (4, 'Python'), (5, 'C#'), (6, 'React'), (7, 'HTML'), (8, 'php'), (9, 'DB')], max_length=100)),
                ('level', models.CharField(choices=[(1, 'Junior'), (2, 'Senior'), ('expert', 3)], default=(1, 'Junior'), max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateField()),
                ('endTime', models.DateField()),
                ('lastUpdate', models.DateTimeField(null=True)),
                ('cost', models.FloatField()),
                ('TaskName', models.CharField(max_length=300)),
                ('Description', models.CharField(max_length=500, null=True)),
                ('encharge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('skillNeed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.skill')),
            ],
        ),
    ]
