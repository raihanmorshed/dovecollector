from django.shortcuts import render
from django.http import HttpResponse

class Dove:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

doves = [
  Dove('Tom', 'Goura Victoria', 'the rarest', 1),
  Dove('Lilly', 'Columbidae', 'gentle and quiet', 3),
  Dove('Sara', 'Columbidae', 'rocky attitude', 0),
  Dove('Raven', 'Coomon Wood Pegion', 'curious little one', 4),
  Dove('Jasper', 'European Turtle Dove', 'curious cat',2)
]

# Create your views here.
# Define the home view
def home(request):
  return HttpResponse('<h1>Hello Doves...</h1>')

def about(request):
  return render(request, 'about.html')
#   return HttpResponse('<h1>About Dove Collector<h1>')

def doves_index(request):
  return render(request, 'doves/index.html', { 'doves': doves})