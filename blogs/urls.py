from django.urls import path
from .views import BlogListView,BlogDetailView
urlpatterns = [
    
path('blogs/', BlogListView.as_view(),name='blogs_list'),
path('blogs/<pk>', BlogDetailView.as_view(),name='blogs_details'),
]