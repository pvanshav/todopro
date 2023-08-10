from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('tlvhome/',views.TaskLV.as_view(),name='tlvhome'),
    path('tdv/<int:pk>/',views.TaskDV.as_view(),name='tdv'),
    path('tuv/<int:pk>',views.TaskUV.as_view(),name='tuv'),
    path('tdelv/<int:pk>',views.TaskDelV.as_view(),name='tdelv'),

]