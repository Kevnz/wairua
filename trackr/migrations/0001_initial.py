# Generated by Django 2.0.5 on 2018-06-05 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoodEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter your mood', max_length=100)),
                ('details', models.CharField(help_text='Enter details about your mood', max_length=500)),
                ('enteredOn', models.DateField()),
            ],
            options={
                'ordering': ['-enteredOn'],
            },
        ),
    ]
