from django.shortcuts import render, redirect, get_object_or_404
from core.models import Gallery
from core.forms import GalleryForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def gallery_list(request):
    galleries = request.user.galleries.all()
    return render(request, "core/gallery_list.html", {"galleries": galleries})

@login_required
def gallery_detail(request, pk):
    gallery = get_object_or_404(Gallery, pk=pk)
    return render(request, 'core/gallery_detail.html', {"gallery": gallery})

@login_required
def gallery_delete(request, pk):
    gallery = get_object_or_404(Gallery, pk=pk)

    if request.method == "POST":
        gallery.delete()
        return redirect("gallery_list")

    return render(request, "core/gallery_delete", {"gallery": gallery})

@login_required
def gallery_create(request):
    if request.method == "GET":
        form = GalleryForm()
    else:
        form =GalleryForm(data=request.POST)
        if form.is_valid():
            gallery = form.save(commit=False)
            gallery.user = request.user
            gallery.save()
            return redirect('gallery_list')

    return render(request, 'core/gallery_create.html', {'form': form})



         



