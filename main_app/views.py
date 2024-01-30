from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

class Bird: 
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

birds = [
  Bird('Lolo', 'tabby', 'foul little demon', 3),
  Bird('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Bird('Raven', 'black tripod', '3 legged Bird', 4)
]

def birds_index(request):
    return render(request, "birds/index.html", {'birds': birds})