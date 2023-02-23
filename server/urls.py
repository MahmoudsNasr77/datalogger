from django.urls import path
from . import views
app_name="server"
urlpatterns =[
    path("", views.data, name="main-page"),
    path("data/", views.get_data, name="get-data")
]