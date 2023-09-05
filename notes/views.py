from django.shortcuts import render
from django.http import Http404
from .models import Notes
from django.views.generic import DetailView, ListView

# Create your views here.

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    
class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "notes"
    
# u don need to use anything else to handle the exception, cuz DetailView handles everything for u 

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Notes does not exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})
