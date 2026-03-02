
from django.urls import path
from . import views

urlpatterns = [
    path("", views.bus_list, name="bus_list"),
    path("create/",views.bus_create, name="bus_create"),
    path("update/<int:id>/", views.bus_update, name="bus_update"),
    path("delete/<int:id>/", views.bus_delete, name="bus_delete"),
    path('register/',views.register, name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('log_out/',views.log_out,name='log_out'),
     path('search_bus/', views.search_bus, name='search_bus'),
]
