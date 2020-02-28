from django.shortcuts import render
from django.views import generic

# Create your views here.
from catalog.models import Nature, Assignment, Unit

class AssignmentListView(generic.ListView):
    model = Assignment
    queryset = Assignment.objects.order_by('-due_date')

class UnitListView(generic.ListView):
    model = Unit

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_assignments = Assignment.objects.all().count()
    num_units = Unit.objects.all().count()
    
    # Available books (status = 'a')
    group_assignments = Assignment.objects.filter(nature__name='group').count()
    individual_assignments = Assignment.objects.filter(nature__name='individual').count()
    unit_list = Unit.objects.all()
      
  
    
    context = {
        'num_assignments': num_assignments,
        'num_units': num_units,
        'group_assignments':group_assignments,
        'individual_assignments': individual_assignments,
        'unit_list': unit_list
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class AssignmentDetailView(generic.DetailView):
    model = Assignment


class UnitDetailView(generic.DetailView):
    model = Unit

