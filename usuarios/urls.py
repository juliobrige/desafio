
from django.urls import path
from . import views

urlpatterns = [
    path ('cadastro/', views.cadastro.as_view(), name="cadastro" )
]
