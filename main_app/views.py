from django.shortcuts import render, redirect
from .models import Bird, Toy, Photo
from .forms import FeedingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'thefinchcollector'

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def birds_index(request):
    birds = Bird.objects.all()
    return render(request, "birds/index.html", {'birds': birds})

def birds_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    toys = Toy
    id_list = bird.toys.all().values_list('id')
    toys_bird_doesnt_have = Toy.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, "birds/detail.html", {'bird': bird, 'feeding_form': feeding_form, 'toys': toys_bird_doesnt_have})

def add_photo(request, bird_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, bird_id=bird_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', bird_id=bird_id)


class BirdCreate(CreateView):
    model = Bird
    fields = ['name', 'image', 'scientific_name', 'size', 'wingspan', 'description']

class BirdUpdate(UpdateView):
    model = Bird
    fields = ['image', 'description']

class BirdDelete(DeleteView):
    model = Bird
    fields = '__all__'
    success_url = "/birds/"

def add_feeding(request, bird_id):
    form = FeedingForm(request.POST)

    if form.is_valid():
      new_feeding = form.save(commit=False)
      new_feeding.bird_id = bird_id
      new_feeding.save()
    return redirect('detail', bird_id = bird_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys'

def assoc_toy(request, pk, toy_pk):
  Bird.objects.get(id=pk).toys.add(toy_pk)
  return redirect('detail', bird_id=pk)

def remove_toy(request, pk, toy_pk):
  Bird.objects.get(id=pk).toys.remove(toy_pk)
  return redirect('detail', bird_id=pk)