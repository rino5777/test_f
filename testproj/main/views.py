from django.shortcuts import render, redirect
from .forms import SkillForm, AddSkill
from django.contrib.auth import get_user_model
from user.views import account 
from .models import  Skills, Value_skill
from django.contrib.auth import  logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def main_paeg(request):
    truesKills = {}
    User = get_user_model()
    users = User.objects.all()
    skill =  Skills.objects.all()
    #user = request.user
    list_users = []
    for a in users:
        q = (a.username,a.first_name, a.last_name)
        list_users.append(q)
        list2 = []
    for i in skill:
        
        
        two = (str(i.owner),i.name,i.description)
        list2.append(two)


    
        

    return render(request, 'main_page/main.html', {'users':users, 'skill':skill, 'list_users':list_users, 'list2':list2})




def create_skill(request):
    
    form  = Value_skill
    skill = Value_skill.objects.all()
    val_list = [skill]
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES)
        if form.is_valid():
            
            form.save()
            val_list = sorted(set(val_list), key=lambda d: val_list.index(d))
           
            return redirect('user:account')

    return render (request, 'skill_page/skill_form.html', {'form':form, 'skill':skill} )



def addskill(request):
    
    formskil  = Skill
    addskill = Skill.objects.all()
    
    if request.method == 'POST':
        formskil = AddSkill(request.POST, request.FILES)
        if formskil.is_valid():
            
            formskil.save()
            
           
            return redirect('user:account')

    return render (request, 'skill_page/skill_add.html', {'formskil':formskil, 'addskill':addskill} )




def logoutuser(request):
    logout(request)
    return redirect('/')

#___________________________________________________________









def post_single(request):
    skill = Value_skill.objects.all()
    fav = bool
    return render(request, 'skill_page/add_skills.html', {'skill': skill,'fav': fav})




# n ----

@login_required()
def createSkill(request):
    
    profile = request.user.profile
    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
             #skill.owner = skill.owner.set(profile)
            skill.save()
            messages.success(request, 'Skill was added successfully!')
            return redirect('user:account')

    context = {'form': form}
    return render(request, 'skill_page/skill_form1.html', context)
