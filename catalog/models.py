from django.db import models
from django.urls import reverse
# Create your models here.
class Nature(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter either group or individual')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Assignment(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    unit = models.ForeignKey('Unit', on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=1000, help_text='Enter a brief description of the assignment')
   
    
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    nature = models.ManyToManyField(Nature, help_text='Enter either group or individual')
    due_date = models.DateField(null=True, blank=True)
    
    def display_nature(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(nature.name for nature in self.nature.all()[:3])
    
    display_nature.short_description = 'Nature'

    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('assignment-detail', args=[str(self.id)])

class Unit(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('unit-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}'

