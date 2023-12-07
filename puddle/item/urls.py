from django.urls import path
from . import views 

app_name = 'item'

urlpatterns = [
    path('',views.items, name='items'),
    path('new/', views.new, name='new'),  # Added trailing slashes for consistency
    path('<int:pk>/delete/', views.delete, name='delete'),  # Moved delete before detail for specificity
    path('<int:pk>/edit/', views.edit, name='edit'),  # Moved edit before detail for specificity
    path('<int:pk>/', views.detail, name='detail'),  # Moved detail to the end
    ]