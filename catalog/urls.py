from django.urls import path
import catalog.views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('^book/(?P<pk>\d+)', views.BookDetailView.as_view(), name='book-detail'),
]