from Nation_Portalapp.forms.auth import*
from django.shortcuts import *
from django.views import *
from  django.urls import reverse
from django.contrib.auth.admin import *
from django.contrib.auth import login,logout,get_user_model,authenticate
from Nation_Portalapp.forms.auth import *

class SignUpView(View):
     def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(
            request=request,
            template_name="Nation_Portalapp/signup.html",
            context={"form": form}
        )

     def post(self, request, *args, **kwargs):
        # import ipdb
        # ipdb.set_trace()
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            # user.save()
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('login'))
                    # redirect("/nation_portal/index")
            else:
                return redirect('nation_portal/home/register/')

def register_view(request):
    form=RegisterForm(request.POST or None)
    context={
        'form':form
    }
    return render(request,'Nation_Portalapp/signup.html',context)

def login_user(request):
    # print(request.user.is_authenticated())
    title="Login|Nation_Portal"
    form=LoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        login(request,user)
        return  HttpResponseRedirect(reverse('user'))
    return render(request,"Nation_Portalapp/login.html",{"form":form ,"title":title} )
    # if(request.method=="POST"):
    #     username=request.POST.get('username')
    #     password=request.POST.get('password')
    #     user=authenticate(request,username=username,password=password)
    #     if user is not None:
    #         login(request,user)
    #         return  HttpResponseRedirect(reverse('post_view'))
    #                 # redirect("/nation_portal/index")
    #     else:
    #         messages.error(request,"Wrong Username or password")
    # return render(request,'Nation_Portalapp/login.html',{})




def Logout_user(request):
    logout(request)
    return redirect("/nation_portal/home/")