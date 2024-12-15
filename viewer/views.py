from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, View, FormView, TemplateView

from viewer.forms import GenreForm
from viewer.models import Genre

# Create your views here.
def hello(request: HttpRequest):
    s1 = request.GET.get('s1', 'This is s1 Default')
    s2 = request.GET.get('s2', 'This is s2 Default')
    return render(
        request, template_name='hello.html',
        context={'adjectives': [s1, "Whatever", "Andrei", s2, "Andre", "Sander", "Aimar"], 'my_object': "My Custom text that is displayed on the website."}
    )

# class GenreView(View):
#   def get(self, request):
#     return render(
#         request,
#         template_name='genre.html',
#         context={ 'object_list': Genre.objects.all() }
#     )
  
class ListGenreView(ListView):
   template_name='genre.html'
   model=Genre

class FormGenreView(FormView):
  template_name='genre-form.html'
  form_class=GenreForm
  success_url=reverse_lazy('genre')

  def form_valid(self, form):

    name = form.cleaned_data['name']

    genre = Genre.objects.create(name=name)
    print(genre)
    return super().form_valid(form)
  

  def form_invalid(self, form):
      print("FOrm is invalid")
      return super().form_invalid(form)