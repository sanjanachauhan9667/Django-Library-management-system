from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add_book,name='add'),
    path('search',views.search_book,name='search'),
    path('issue',views.issue_book,name="issue"),
    path('return',views.return_book,name='return'),
    path('delete',views.delete_book,name='delete'),
]
