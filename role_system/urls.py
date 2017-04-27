from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^student_login/(?P<studentid>\w+)/(?P<password>\w+)',views.student_login),
]