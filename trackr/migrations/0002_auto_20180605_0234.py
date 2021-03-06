# Generated by Django 2.0.5 on 2018-06-05 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackr', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moodentry',
            name='name',
        ),
        migrations.AddField(
            model_name='moodentry',
            name='selected_mood',
            field=models.CharField(blank=True, choices=[('😄', 'Happy'), ('🙁', 'Unhappy'), ('😀', 'Really Good'), ('😠', 'Angry'), ('\U0001f92c', 'Really Angry'), ('😢', 'Sad'), ('😩', 'Weary'), ('🤢', 'Sick'), ('💩', 'Poop'), ('🤣', 'ROFL')], default='😄', help_text='Select your current Mood', max_length=1),
        ),
    ]
