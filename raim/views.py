from django.shortcuts import render,redirect
from account.forms import GetUser,CreateUserForm
from account.models import Task
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView

def Dashboard(request):
    tasks = Task.objects.all()
    customers= User.objects.all()[1:]
    t=0
    c=0
    for task in tasks:
        t=t+1
    for customer in customers:
        c=c+1


    context={
        'task':t,
        'user':c
    }
    return render(request,'raim/dashboard.html',context)




def Task_Manage(request,**kwargs):

   tasks = Task.objects.all()
   all_task=[]
   count=1
   
        

   for task in tasks:
       all_tasks={
           'id':task.id,
           'count':count,
           'user':task.user,
           'title':task.title,
           'time':task.create,
           'complete':task.complete




       }
       count=count+1
       all_task.append(all_tasks)
   
  

 
   context={
        'tasks':all_task
        
    }

   return render(request,'raim/tasks.html',context)


def User_Manage(request):
    context={}

    customers= User.objects.all()[1:]
    


    all_info=[]
    count=1
    
    for customer  in customers:
       
        
        all_info1={
                'id':customer.id,
                'count':count,
                'username':customer.username,
                'first_name':customer.first_name,
                'last_name':customer.last_name
            
            }
        count=count+1
        all_info.append(all_info1)

    context={
        'all_info':all_info
    }    

   

    return render(request,'raim/users.html',context)

def Admin(request):
    context={}
    return render(request, 'raim/admin_home.html' ,context)  





class UserUpdate(LoginRequiredMixin,UpdateView):
    model=User
    
    fields=['username','email','first_name','last_name']
    success_url=reverse_lazy('users') 




class UserDelete(LoginRequiredMixin,DeleteView):
    model = User
    context_object_name = "user"
    success_url=reverse_lazy('users')


class UserDetail(LoginRequiredMixin,DetailView):
    model=User
    context_object_name="user"   




class TaskCreate(LoginRequiredMixin ,CreateView):
    model = Task
    
    fields = ['user','title','description','complete']
    success_url = reverse_lazy('tasks1') 




      



class TaskUpdate(LoginRequiredMixin,UpdateView):
    model=Task
    

    fields=['user','title','description','complete']
    success_url = reverse_lazy('tasks1') 

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    
    context_object_name = "task"
    success_url = reverse_lazy('tasks1') 
    

