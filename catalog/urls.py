from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    # path('catalog/', include('catalog.urls')),
    path('', views.index, name='index'),
]
