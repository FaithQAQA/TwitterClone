from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('profile_list',views.profile_list, name='profile_list'),
    path('profile/<int:pk>',views.profile, name='profile'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('register/',views.register_user, name='register'),
    path('update_user/',views.update_user, name='update_user'),
    path('meep_likes/<int:pk>',views.meep_likes, name='meep_like'),
    path('meep_show/<int:pk>',views.meep_show, name='meep_show'),
    path('unfollow/<int:pk>', views.unfollow, name="unfollow"),
    path('create_reply/<int:meep_id>', views.create_reply, name="create_reply"),
    path('meep/<int:meep_id>/', views.meep_detail, name='meep_detail'),
    path('follow/<int:pk>', views.follow, name="follow"),
    path('profile/followers/<int:pk>', views.followers, name='followers'),
    path('profile/follows/<int:pk>', views.follows, name='follows'),
    path('delete_meep/<int:pk>', views.delete_meep, name='delete'),
    path('edit_meep/<int:pk>', views.edit_meep, name='edit_meep'),
    path('search/',views.search, name='search'),
    path('search_user/',views.search_user, name='search_user'),
    path('meep_detail/<int:pk>', views.meep_detail, name='meep_detail'),





]
