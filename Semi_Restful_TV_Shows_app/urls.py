from django.urls import path
from . import views


#render
urlpatterns = [
    path('shows', views.all_show),
    path('shows/new', views.index),
    path('shows/<int:show_id>', views.display_show),
    path('shows/<int:show_id>/edit', views.update_page),
    path('shows/<int:show_id>/delete', views.delete_show),


#action / process** routes
    path('shows/create', views.create_show),
    path('shows/<int:show_id>/update', views.update_show),
]
