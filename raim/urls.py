from django.urls import path,include
from . import views
from .views import UserUpdate,UserDelete,UserDetail,User_Manage,TaskCreate,TaskDelete,TaskUpdate,Dashboard
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.Dashboard,name='admin'),
    path('users/',views.User_Manage, name='users'),
    path('dashboad/',views.Dashboard,name="dashboard"),
    path('delete-user/<int:pk>/ ' , UserDelete.as_view(template_name ='raim/user_confirm_delete.html') ,name="delete-user"),
    path('task/<int:pk>/', UserDetail.as_view(), name="user"),
    path('tasks/',views.Task_Manage,  name="tasks1"),
    path('logout/',LogoutView.as_view(next_page='login' ),name='logout1'),
    path('create-task/',TaskCreate.as_view( template_name='raim/task_form.html'),name='create-task1'),
    path('task-update/<int:pk>/ ' , TaskUpdate.as_view( template_name='raim/task_form.html' ) ,name="update-task1"),
    path('task-delete/<int:pk>/ ' , TaskDelete.as_view(template_name ='raim/task_confirm_delete.html') ,name="delete-task1"),
    path('update-user/<int:pk>/ ' , UserUpdate.as_view( template_name='raim/user_form.html' ) ,name="update-user"),
]