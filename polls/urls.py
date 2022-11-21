from django.urls import path
from . import views


urlpatterns = [
    path('detail/<int:question_id>', views.detailView, name='detail'),
    path('<int:question_id>', views.vote, name='vote'),
    path('list/', views.viewlist, name='view_list'),
    path('', views.index, name='index'),
]
