from django.urls import path
from brmapp import views



urlpatterns = [
    path('view-books/', views.view_books, name="view_books"),
    path('edit-book/', views.edit_book, name="edit_book"),
    path('delete-book/', views.delete_book, name="delete_book"),
    path('search-book/', views.searchbook, name="searchbook"),
    path('new-book/', views.new_book, name="new_book"),
    path('add/', views.add_book, name="add_book"),
    path('search/', views.search, name="search"),
    path('edit/', views.edit, name="edit"),
    # path('login/', views.user_login, name="user_login"),
    # path('logout/', views.user_logout, name="user_logout"),



]    
