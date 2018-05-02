from django.conf.urls import url
from . import views
from django.contrib.auth.views import(
    login, logout, password_reset, password_reset_done, password_reset_confirm,password_reset_complete
)

urlpatterns = [
      url(r'^home/$' , views.home),
      url(r'^signin/$' , login, {'template_name': 'signin/loginform/login.html'}),
      url(r'^signout/$' , logout, {'template_name': 'signin/loginform/logout.html'}),
      url(r'^register/$', views.register, name='register'),
      url(r'^profile/$', views.profile,name='profile'),
      url(r'^profile/edit/$', views.edit_profile, name = 'edit_profile'),
      url(r'^change_password/$', views.change_password, name = 'change_password'),
      url(r'^reset_password/$', password_reset, name = 'password_reset'),
      url(r'^reset_password/done/$', password_reset_done, name = 'password_reset_done'),
      url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm , name = 'password_reset_confirm'),
      url(r'^reset_password/complete/$', password_reset_complete, name = 'password_reset_complete'),
]
