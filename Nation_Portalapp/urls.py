from  django.urls import path
from Nation_Portalapp.views import SignUpView,login_user,Logout_user
from . import  views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

appname='Nation_Portalapp'

urlpatterns=[
    path('home/',views.homepage_view,name='home'),
    path('user/create/',views.create_post,name="create"),
    path('user/index/',views.post_view,name="post_view"),
    path('user/<int:id>/',views.detail,name="detail"),
    path('user/',views.user_view,name="user"),
    path('home/about',views.about_view,name='about'),
    path('user/<int:id>/edit',views.update_post,name="update"),
    path('user/<int:id>/delete/',views.delete_post,name="delete"),
    path('home/register/',SignUpView.as_view(),name="signup"),
    path('home/reg/',views.register_view,name='register'),
    path('home/login/',views.login_user,name="login"),
    path('user/logout/',Logout_user,name="logout"),
    ]

urlpatterns+=staticfiles_urlpatterns()