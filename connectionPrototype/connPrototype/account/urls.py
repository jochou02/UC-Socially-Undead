from rest_framework.authtoken import views as auth_views
from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('token_auth/', auth_views.obtain_auth_token, name='token_auth'),
    path('foo/', views.foo.as_view(), name='foo'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('get_user_info/', views.GetUserInfoView.as_view(), name='get_info'),
    path('delete_user/', views.DeleteUserView.as_view(), name='delete'),

    #地図: test
    path('add_karma/', views.AddKarmaView.as_view(),
    name='karma'),

    path('gen_auth/', views.GenEmailAuth.as_view(), name='gen_auth'),
    path('update_password/', views.UpdatePassword.as_view(), name='update_pword'),
]