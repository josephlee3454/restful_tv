from django.urls import path
from . import views	
                    
urlpatterns = [
    path('', views.index),
    path('shows/', views.shows),
    path('add_show',views.add_show),
    path('show_info/<int:show_id>', views.show_info),
    path('delete/<int:show_id>',views.delete_show),
    path('edit/<int:show_id>',views.edit_show)
    
]