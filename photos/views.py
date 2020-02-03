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
    return render(request, 'Render/welcome.html', {'location_images': images})

def search_results(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'Render/show_tell.html', {"message": message, "images": searched_images})
    else:
        message = "PLease check spelling of your search results"
        return render(request, 'render/show_tell.html', {"message": message})