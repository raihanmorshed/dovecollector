from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Dove, Toy
from .forms import FeedingForm
# Create your views here.
# Define the home view
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid credentials - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class DoveCreate(LoginRequiredMixin, CreateView):
  model = Dove
  fields = '__all__'

  def form_valid(self, form):
    # Assign the logged in user
    form.instance.user = self.request.user
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class DoveUpdate(UpdateView):
  model = Dove
  # Let's disallow the renaming of a dove by excluding the name field!
  fields = ['breed', 'description', 'age']

class DoveDelete(DeleteView):
  model = Dove
  success_url = '/doves/'


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')
#   return HttpResponse('<h1>About Dove Collector<h1>')

@login_required
def doves_index(request):
  doves = Dove.objects.filter(user=request.user)
  # You could also retrieve the logged in user's doves like this
  # doves = request.user.dove_set.all()
  return render(request, 'doves/index.html', { 'doves': doves })
  # doves = Dove.objects.all()
  # return render(request, 'doves/index.html', { 'doves': doves})

@login_required
def doves_detail(request, dove_id):
  dove = Dove.objects.get(id=dove_id)
  # Get the toys the cat doesn't have
  toys_dove_doesnt_have = Toy.objects.exclude(id__in = dove.toys.all().values_list('id'))
  # Instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  return render(request, 'doves/detail.html', {
    # Pass the cat and feeding_form as context 
    'dove': dove, 'feeding_form': feeding_form,
    # Add the toys to be displayed
    'toys': toys_dove_doesnt_have
    })

@login_required
def add_feeding(request, dove_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.dove_id = dove_id
    new_feeding.save()
  return redirect('detail', dove_id=dove_id)

@login_required
def assoc_toy(request, dove_id, toy_id):
  Dove.objects.get(id=dove_id).toys.add(toy_id)
  return redirect('detail', dove_id=dove_id)

@login_required
def unassoc_toy(request, dove_id, toy_id):
  Dove.objects.get(id=dove_id).toys.remove(toy_id)
  return redirect('detail', dove_id=dove_id)

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
  success_url = '/toys/'

