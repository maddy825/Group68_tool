from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from sightings.models import Sighting

def sighting_map(request, template_name='map/map.html'):
    sightings = Sighting.objects.all()[:100]
    context = {
            'sightings' : sightings,
    }
    return render(request, template_name, context)
