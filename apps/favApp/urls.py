from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^books$', views.books),
    url(r'^books/(?P<num>\d+)$', views.specificBook),
    url(r'^addBook$', views.addBook),
    url(r'^addFavorite$', views.addFavorite),
    url(r'^unfavorite$', views.unfavorite),
    url(r'^update$', views.update)
        # deleteBook

]