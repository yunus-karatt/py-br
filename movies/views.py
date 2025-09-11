from django.shortcuts import render
from .models import MovieInfo
from . forms import MovieForm

# Create your views here.


def create(request):
    if request.POST:
        frm = MovieForm(request.POST)
        if frm.is_valid():
            frm.save()
    else:
        frm = MovieForm()
    return render(request, 'create.html', {'frm': frm})


def list(request):
    movie_set = MovieInfo.objects.all()
    return render(request, 'list.html', {'movies': movie_set})


def edit(request, pk):
    instance_to_be_edited = MovieInfo.objects.get(pk=pk)
    if (request.POST):
        title = request.POST.get('title')
        year = request.POST.get('year')
        summary = request.POST.get('summary')
        instance_to_be_edited.title = title
        instance_to_be_edited.year = year
        instance_to_be_edited.summary = summary
        instance_to_be_edited.save()
    edit_form = MovieForm(instance=instance_to_be_edited)
    return render(request, 'create.html', {'frm': edit_form})


def delete(request, pk):
    MovieInfo.objects.filter(id=pk).delete()
    movie_set = MovieInfo.objects.all()
    return render(request, 'list.html', {'movies': movie_set})
