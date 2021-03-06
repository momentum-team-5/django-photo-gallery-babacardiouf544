from django.shortcuts import render, redirect, get_object_or_404
from core.models import Gallery, Photo
from core.forms import GalleryForm, PhotoForm
from django.contrib.auth.decorators import login_required
# Create your views here.

#@login_required
def gallery_list(request):
    galleries = request.user.galleries.all()
    return render(request, "core/gallery_list.html", {"galleries": galleries})

#@login_required
def gallery_detail(request, pk):
    gallery = get_object_or_404(Gallery, pk=pk)
    return render(request, 'core/gallery_detail.html', {"gallery": gallery})

@login_required
def gallery_delete(request, pk):
    gallery = get_object_or_404(Gallery, pk=pk)

    if request.method == "POST":
        gallery.delete()
        return redirect(to = "gallery_list")

    return render(request, "core/gallery_delete.html", {"gallery": gallery})

@login_required
def gallery_create(request):
    if request.method == "GET":
        form = GalleryForm()
    else:
        form = GalleryForm(data=request.POST)
        if form.is_valid():
            gallery = form.save(commit=False)
            gallery.user = request.user
            gallery.save()
            return redirect('gallery_list')

    return render(request, 'core/gallery_create.html', {'form': form})



@login_required
def list_photo(request):
    photos = request.user.photos.all()
    return render(request, 'core/list_photo.html', {'photos': photos})

@login_required
def add_photo(request, pk):
    gallery = get_object_or_404(request.user.galleries, pk=pk)

    if request.method == 'POST':
        form = PhotoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.gallery = gallery
            photo.save()
            return redirect('gallery_detail', pk=pk)            
    else:
        form = PhotoForm(data=request.POST)
    
    return render(request, 'core/add_photo.html', {'form': form, 'gallery': gallery})

@login_required
def delete_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == "GET":
        photo.delete()
        return redirect('gallery_list')
    return render (request, 'core/delete_photo.html', {'photo': photo})



         



