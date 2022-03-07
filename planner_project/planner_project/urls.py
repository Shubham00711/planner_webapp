from django.contrib import admin
from django.urls import path
from planner_app.views import home	#, planner
from auapp.views import user_signup, user_login, user_logout, user_fp, user_cp
from weather_app.views import check_weather
from todo_app.views import add_todo, show_todo, delete_todo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    	#path('planner', planner, name="planner"),
    path('user_signup', user_signup, name="user_signup"),
    path('user_login', user_login, name="user_login"),
    path('user_logout', user_logout, name="user_logout"),
    path('user_fp', user_fp, name="user_fp"),
    path('user_cp', user_cp, name="user_cp"),
    path('check_weather', check_weather, name="check_weather"),
    path('add_todo', add_todo, name="add_todo"),
    path('show_todo', show_todo, name="show_todo"),
    path('delete_todo/<str:id>/<str:dl>/<str:ts>', delete_todo, name="delete_todo"),
]
