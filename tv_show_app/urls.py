from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shows/new', views.new_show, name='new_show'),
    path('shows/create', views.create_show, name='create_show'), 
    path('shows/<int:show_id>', views.show_info, name='show_info'),
    path('shows', views.all_shows, name='all_shows'),
    path('shows/<int:show_id>/edit', views.edit_show, name='edit_show'),
    path('shows/<int:show_id>/update', views.update_show, name='update_show'),
    path('shows/<int:show_id>/destroy', views.delete_show, name='delete_show')
]