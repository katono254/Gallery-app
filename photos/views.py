from django.shortcuts import render
from .models import Image, Location


def welcome(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    print(locations)
    return render(request, 'Render/index.html', {'images': images[::-1], 'locations': locations})



def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'Render/location.html', {'location_images': images})
