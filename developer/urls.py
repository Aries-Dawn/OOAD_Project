from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.developer_home, name='developer home'),
    path('modify', views.modify_developer_message, name='modify developer message'),
    path('select', views.game_select, name='game select'),
    path('dlc_branch', views.dlc_select, name='dlc select'),
    # path('<str:developer_name>', views.developer_message, name='developer message'),

]
