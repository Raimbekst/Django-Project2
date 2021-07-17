from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from account.models import Task
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.contrib import messages


class TaskList(LoginRequiredMixin,ListView):
    model=Task
    context_object_name="tasks"
    
    
    def get_context_data(self,**kwargs):

        context = super().get_context_data(**kwargs)
        
        context['tasks']  = context['tasks'].filter(user=self.request.user)

        context['count'] = context['tasks'].filter(complete=False).count()
        

        search_input = self.request.GET.get("search-area") or ''
        
        
        
        if search_input:
            context['tasks']=context['tasks'].filter(title__startswith  = search_input )


        context['search_input'] = search_input 
               

        return context 










def registerPage(request):
    form = CreateUserForm()

    if request.method=='POST':
        form =CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+user)
            return redirect('login')
        

            




    context={'form':form}
    return render(request, 'account/register.html',context)


def loginPage(request):
    if request.method=='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
        
            username=request.POST.get('username')
            password=request.POST.get('password')
            
            user = authenticate(request,username=username,password=password)
            if user is not None:
                if(username=="Raimbekst" and password=="raimbeklove"):
                    login(request,user)
                    return redirect('admin')
                
                login(request,user)
                return redirect('tasks')
        
       
                   

       
    form =AuthenticationForm()

    context={
        'login_form':form
    }


    return render(request,'account/login.html',context)





class TaskDetail(LoginRequiredMixin,DetailView):
    model=Task 

    context_object_name="task"   


class TaskCreate(LoginRequiredMixin ,CreateView):
    model=Task

    fields = ['title','description','complete']
    success_url = reverse_lazy('tasks')


    def form_valid(self, form):
        form.instance.user = self.request.user  


        return super(TaskCreate,self).form_valid(form)


           





class TaskUpdate(LoginRequiredMixin,UpdateView):
    model=Task
    fields=['title','description','complete']
    success_url=reverse_lazy('tasks')





class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = "task"
    success_url=reverse_lazy('tasks')











