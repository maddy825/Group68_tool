# Generated by Django 2.2.7 on 2019-12-08 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('longitude', models.FloatField(help_text='Longitude')),
                ('latitude', models.FloatField(help_text='Latitude')),
                ('squirrel_id', models.CharField(help_text='Unique Squirrel ID', max_length=32, primary_key=True, serialize=False)),
                ('shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', help_text='Shift', max_length=10)),
                ('date', models.DateField(help_text='Date')),
                ('age', models.CharField(choices=[('adult', 'Adult'), ('juvenile', 'Juvenile'), ('', '')], default='adult', help_text='Age', max_length=10, null=True)),
                ('primary_fur_color', models.CharField(choices=[('gray', 'Gray'), ('black', 'Black'), ('cinnamon', 'Cinnamon'), ('', '')], default='gray', help_text='Primary fur color', max_length=10)),
                ('location', models.CharField(choices=[('ground_plane', 'Ground_Plane'), ('above_ground', 'Above_Ground'), ('', '')], default='ground_plane', help_text='Location', max_length=20, null=True)),
                ('specific_location', models.CharField(blank=True, help_text='Specific location', max_length=20, null=True)),
                ('running', models.BooleanField(default=False)),
                ('chasing', models.BooleanField(default=False)),
                ('climbing', models.BooleanField(default=False)),
                ('eating', models.BooleanField(default=False)),
                ('foraging', models.BooleanField(default=False)),
                ('other_activities', models.CharField(blank=True, help_text='Other activity', max_length=20, null=True)),
                ('kuks', models.BooleanField(default=False)),
                ('quaas', models.BooleanField(default=False)),
                ('moans', models.BooleanField(default=False)),
                ('tail_flags', models.BooleanField(default=False)),
                ('tail_twitches', models.BooleanField(default=False)),
                ('approaches', models.BooleanField(default=False)),
                ('indifferent', models.BooleanField(default=False)),
                ('runs_from', models.BooleanField(default=False)),
            ],
        ),
    ]