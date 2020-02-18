from django.urls import path
from . import views

urlpatterns = [

path('', views.index, name='index'),
path('assignments/', views.AssignmentListView.as_view(), name='assignments'),
path('assignment/<int:pk>', views.AssignmentDetailView.as_view(), name='assignment-detail'),
path('units/', views.UnitListView.as_view(), name='units'),
path('unit/<int:pk>', views.UnitDetailView.as_view(), name='unit-detail'),
]