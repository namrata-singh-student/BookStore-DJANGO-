from django.urls import path
from . import views
urlpatterns=[
  path('index1',views.index1),
  path('form/',views.form, name='form'),
  path('userForm/', views.userForm, name='userForm'),
  path('store',views.store),
  path('del/<int:id>',views.dele),
  path('loginn/',views.loginn, name='loginn'),
  path('logcodee',views.logcodee, name='logcodee'),
  path('contact/',views.contact, name='contact'),
]