from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from .forms import RegisterUserForm, CreateListForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import UserList
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponseForbidden

class Login(LoginView):
    template_name = "users/accounts/login.html"

class Logout(LogoutView):
    next_page = "/"


class RegisterUser(FormView):
    template_name = "users/accounts/register.html"
    form_class = RegisterUserForm
    success_url = "/"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

@login_required
def profile(request):
    user = request.user
    user_lists = UserList.objects.filter(user=user)
    
    return render(request, "users/accounts/profile.html", {"user":user,
                                                           "user_lists":user_lists})

@login_required
def create_list(request):
    user = request.user
    if request.method == "POST":
        form = CreateListForm(request.POST)
        
        if form.is_valid():
            user_list = form.save(commit=False)
            user_list.user = user
            user_list.save()
            
            user_lists = UserList.objects.filter(user=user)
            
            return render(request, "users/lists/partials/_user_lists.html",
                          {"user_lists":user_lists})
        return render(request, "users/lists/partials/_create_list_form.html", {"form":form}, status=400)
            
            
        
    form = CreateListForm()
    return render(request, "users/lists/partials/_create_list_form.html", {"form":form})

@login_required
def delete_list(request, list_id):
    user_list = get_object_or_404(UserList, id=list_id, user=request.user)
    if request.method == "POST":
        user_list.delete()
        user_lists = UserList.objects.filter(user= request.user)
        return render(request, "users/lists/partials/_user_lists.html",
                          {"user_lists":user_lists})
    return HttpResponseForbidden
    
    