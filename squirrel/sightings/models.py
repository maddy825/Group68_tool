from django.db import models
from django.utils.translation import gettext as _

class Sighting(models.Model):

    longitude = models.DecimalField(
            max_digits=16,
            decimal_places=13,
    )

    latitude = models.DecimalField(
            max_digits=16,
            decimal_places=13,
    )

    squirrel_id = models.CharField(
            primary_key=True,
            max_length=200,
	    help_text=("Unique Squirrel ID"),
    )

    AM,PM='AM','PM'

    SHIFT_CHOICES=(
            (AM,"AM"),
	    (PM,"PM"),
    )

    shift = models.CharField(
	    max_length=200,
	    choices=SHIFT_CHOICES,
	    default=AM,
    )

    date = models.DateField(
    )

    ADULT = "adult"
    JUVENILE = "juvenile"

    AGE_CHOICES =(
	    (ADULT,"Adult"),
	    (JUVENILE,"Juvenile"),
    )

    age = models.CharField(
	    max_length=200,
	    choices=AGE_CHOICES,
	    default=ADULT,
    )

    GRAY="gray"
    BLACK="black"
    CINNAMON="cinnamon"

    FUR_CHOICES=(
            (GRAY,"Gray"),
	    (BLACK,"Black"),
	    (CINNAMON,"Cinnamon"),
    )

    primary_fur_color = models.CharField(
            max_length=200,
	    choices=FUR_CHOICES,
	    default=GRAY,
    )

    GROUND_PLANE="ground_plane"
    ABOVE_GROUND="above_ground"

    LOCATION_CHOICES=(
	    (GROUND_PLANE,"Ground_Plane"),
	    (ABOVE_GROUND,"Above_Ground"),
    )

    location = models.CharField(
	    max_length=200,
	    choices=LOCATION_CHOICES,
	    default=GROUND_PLANE,
    )

    specific_location = models.CharField(
	    max_length=200,
            blank=True,
    )

    running = models.NullBooleanField()

    chasing = models.NullBooleanField()

    climbing = models.NullBooleanField()

    eating = models.NullBooleanField()

    foraging = models.NullBooleanField()

    other_activities = models.CharField(
	    max_length=200,
            blank=True,
    )

    kuks = models.NullBooleanField()

    quaas = models.NullBooleanField()

    moans = models.NullBooleanField()

    tail_flags = models.NullBooleanField()

    tail_twitches = models.NullBooleanField()

    approaches = models.NullBooleanField()

    indifferent = models.NullBooleanField()

    runs_from = models.NullBooleanField() 
