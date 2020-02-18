from django.contrib import admin
from .models import Nature, Assignment, Unit

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_nature','unit','due_date')
    list_filter = ('nature', 'due_date')

@admin.register(Unit)
class BookAdmin(admin.ModelAdmin):
    pass
# Register your models here.
admin.site.register(Nature)
admin.site.register(Assignment, AssignmentAdmin)
#admin.site.register(Unit)

