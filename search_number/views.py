import request as request
from django.shortcuts import render, redirect
from . import forms
from users.forms import CommentForms
from . import models
from django.contrib.auth.decorators import login_required
from users.models import UploadImages
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = forms.SearchForm(request.POST)
        date_form = forms.DateRangeForm(request.POST)
        com_form = CommentForms(request.POST)

        if form.is_valid():
            name= form.cleaned_data["name"]
            return redirect('results', name=name)

        if date_form.is_valid():
            qs = UploadImages.objects.filter(pub_date__range=(
                date_form.cleaned_data['start_date'],
                date_form.cleaned_data['end_date']
                ))
            return render(request, "index.html", {'form': form,
                                                  'images': qs,
                                                  'd_form': date_form})

    else:
        images_list = UploadImages.objects.all()
        paginator = Paginator(images_list, 5)
        page = request.GET.get('page')
        images = paginator.get_page(page)
        form = forms.SearchForm()
        date_form = forms.DateRangeForm()
        com_form = CommentForms(request.POST)
    return render(request, "index.html", {'form' : form,
                                          'images': images,
                                          'd_form':date_form,
                                          'c_form': com_form})


@login_required
def results(request, name):
    peep = models.People.objects.filter(name__contains=name).all()
    return render(request, "resulting.html", {'people':peep})


@login_required
def person(request, id):
    person = models.People.objects.get(id=id)
    return render(request, 'person.html', {'person':person})