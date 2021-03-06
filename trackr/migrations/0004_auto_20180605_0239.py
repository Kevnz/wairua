# Generated by Django 2.0.5 on 2018-06-05 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackr', '0003_auto_20180605_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moodentry',
            name='selected_mood',
            field=models.CharField(blank=True, choices=[('😄', '😄 Happy'), ('🙁', '🙁 Unhappy'), ('😀', '😀 Really Good'), ('😠', '😠 Angry'), ('\U0001f92c', '\U0001f92c Really Angry'), ('😢', '😢 Sad'), ('😩', '😩 Weary'), ('🤢', '🤢 Sick'), ('💩', '💩 Poop'), ('🤣', '🤣 ROFL')], default='😄', help_text='Select your current Mood', max_length=1),
        ),
    ]
