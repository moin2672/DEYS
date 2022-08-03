from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('post/<int:pk>', views.PostDetailView.as_view(), name="detail"),
    path('addpost/', views.PostCreateView.as_view(), name="addpost"),
    path('updatepost/<int:pk>', views.PostUpdateView.as_view(), name="updatepost"),
    path('deletepost/<int:pk>', views.PostDeleteView.as_view(), name="deletepost"),
    path('addcategory/', views.CategoryCreateView.as_view(), name="addcategory"),
    path('category/<str:cats>/', views.CategoryView, name="category"),
    path('categorylist', views.CategoryListView, name="categorylist"),
]
