from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("birds/", views.birds_index, name="index"),
    path("birds/<int:bird_id>/", views.birds_detail, name="detail"),
    path("birds/create/", views.BirdCreate.as_view(), name="bird_create"),
    path("birds/<int:pk>/update", views.BirdUpdate.as_view(), name="bird_update"),
    path("birds/<int:pk>/delete", views.BirdDelete.as_view(), name="bird_delete"),
    path('birds/<int:bird_id>/add_feeding/', views.add_feeding, name="add_feeding"),
    path('birds/<int:pk>/assoc_toy/<int:toy_pk>/', views.assoc_toy, name="assoc_toy"),
    path('toys/', views.ToyList.as_view(), name='toy_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toy_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy_delete'),
    path('birds/<int:pk>/remove_toy/<int:toy_pk>/', views.remove_toy, name='remove_toy'),
    path('birds/<int:bird_id>/add_photo/', views.add_photo, name='add_photo'),
]

