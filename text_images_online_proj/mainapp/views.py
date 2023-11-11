from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm
from .models import ImageModel
from .image_to_ascii import image_to_ascii
from .default_images import IMAGE_PIN

# Create your views here.

def main_page(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Save and get the current instance object to display in the template
            img_obj = form.save()
            # Now the image is saved the image can be processed
            img_obj.text_image = image_to_ascii(img_obj.image.path)
            # Update database
            img_obj.save()
            # Render result
            return render(request, 'mainapp/index.html', {'form': form, 'img_obj': img_obj, 'intro_image' : IMAGE_PIN})
    form = ImageForm()
    return render(request, 'mainapp/index.html', {'form': form, 'intro_image' : IMAGE_PIN})


def gallery_page(request):
    """Render the gallery template with all stored images"""
    gallery_images = ImageModel.objects.all()
    context = {'gallery_images' : gallery_images}
    return render(request, "mainapp/gallery.html", context=context)
