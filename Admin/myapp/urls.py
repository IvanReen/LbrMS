from django.urls import path, re_path

from myapp.views import *

app_name = 'myapp'

urlpatterns = [
    path('publisher_list/', publisher_list),
    path('add_publisher/', add_publisher),
    path('drop_publisher/', drop_publisher),
    path('edit_publisher/', edit_publisher),
    path('book_list/', book_list, name='booklist'),
    path('add_book/', add_book),
    path('drop_book/', drop_book),
    path('edit_book/', edit_book),
    path('author_list/', author_list, name='authorlist'),
    path('add_author/', add_author),
    path('drop_author/', drop_author),
    path('edit_author/', edit_author),
    re_path('^$', publisher_list),
]