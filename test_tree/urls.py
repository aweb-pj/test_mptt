from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get_one/(?P<rname>\w+)$', views.GenreView.as_view()),
    url(r'^get_tree$',views.get_tree),
    url(r'^create_node$',views.create_node),
    url(r'^update_node$',views.update_node)
]