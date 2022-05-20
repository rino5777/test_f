from django.shortcuts import redirect, render, get_object_or_404

from django.http import request
from .forms import UserRegistrationForm, ProfileForm

from django.contrib import messages
import time
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile
from django.urls import reverse
from django.views.generic import TemplateView
from main.models import Skill, Value_skill, Skills


def account(request ):
    skill =  Skills.objects.all()
    truesKills = {}
    user_info = Profile.objects.all()
    user = request.user
    profile = request.user.profile

    for i in skill:
        if str(i.owner) == user.username:
            truesKills[i.name] = i.description
            print('True' , truesKills)
        else:
            print('False',)

    return render (request, 'user_pages/account-profile.html', { "user_info":user_info, 'skill':skill, 'user':user,'profile':profile, 'truesKills':truesKills })




def authorization(request):
     # Создаём форму
    form = UserRegistrationForm(request.POST)
    data = {}
    if request.method == 'POST':
        
        # Валидация данных из формы
        
        if form.is_valid():
            form.save(commit='FALSE')
            form.changed_data
            time.sleep(1)
            #users = User.objects.all().select_related('Profile')
            # Рендаринг страницы
            return render(request, 'user_pages/account-log.html',  { 'form':form,} )
    else: # Иначе
        
        return render(request, 'user_pages/account-login.html',{ 'form':form } ,)
    return render(request, 'user_pages/account-login.html',{ 'form':form })


class LoginView(TemplateView):
    
    template_name = 'user_pages/account-log.html'

    def dispatch(self, request, *args, **kwargs):
        error_dict = {}
        #Profile.objects.get_or_create(user=request.user)
        if request.method == 'POST':
		
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user:account')
            else:
                 messages.success(request, 'Username/Password Invalid')

	    
        return render(request, self.template_name, error_dict)



