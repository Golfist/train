from django.urls import path
from . import views

app_name = 'duku'
urlpatterns = [
    path('', views.KenobyView.as_view(), name='kenoby'),
    #detail
    path('<int:pk>/', views.FlagshipView.as_view(), name='flagship'),
    #results
    path('<int:pk>/status/', views.StatusView.as_view(), name='status'),
    #vote
    path('<int:cruiser_id>/instructions/', views.instructions, name='instructions'),

]