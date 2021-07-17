from django.urls import path,include
from . import views
from .views import loginPage,registerPage,TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', views.loginPage,name='login'),
    path('register/',views.registerPage, name='register'),
    path('admin-home/',include('raim.urls')),
    path('logout/',LogoutView.as_view(next_page='login' ),name='logout'),
    path('', TaskList.as_view(), name="tasks"),
    path('task/<int:pk>/', TaskDetail.as_view(), name="task"),
    path('create-task/', TaskCreate.as_view(), name="create-task" ),
    path('update-task/<int:pk>/ ' , TaskUpdate.as_view() ,name="update-task"),
    path('delete-task/<int:pk>/ ' , TaskDelete.as_view() ,name="delete-task"),



    
    

]