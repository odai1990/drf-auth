
from django.urls import path
from .views import *
urlpatterns = [
    path('', MoviesList.as_view(),name='movies'),
    path('<int:pk>/',MoviesDetials.as_view(),name='movies_detials'),  
    path('create/',MoviesCreate.as_view(),name='movies_create'),
    path('all_access/<int:pk>/',MoviesAllOpreations.as_view(),name='movies_detials_all_access'),
]
