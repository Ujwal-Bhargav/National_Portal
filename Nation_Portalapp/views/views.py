from django.shortcuts import render, redirect
from django.http import *
# Create your views here.
from Nation_Portalapp.forms.auth import PostForm, reverse
from Nation_Portalapp.models import Post
from django.shortcuts import get_object_or_404
from  django.contrib import  messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render


def homepage_view(request):
    return render(request,'Nation_Portalapp/home.html')

def user_view(request):
    return render(request,'Nation_Portalapp/user_home.html')

def about_view(request):
    return render(request,'Nation_Portalapp/about.html')
def create_post(request):
    # if not request.user.is_staff or not request.user.is_superuser:
    if request.user.is_authenticated:
    #     # return render(request, 'Nation_Portalapp/home.html')
        form=PostForm(request.POST or None,request.FILES or None)
        if(form.is_valid()):
            instance=form.save(commit=False)
            instance.save()
            messages.success(request,"Successfully Created")
            return HttpResponseRedirect(instance.get_absolute_url())
        context={
            "form":form,
        }
        return render(request,'Nation_Portalapp/create.html',context)
    else:
        return  HttpResponseRedirect(reverse('home'))


def post_view(request):
    if  request.user.is_authenticated:
        # return render(request, 'Nation_Portalapp/home.html')
        QuerySet_list=Post.objects.all()
        paginator=Paginator(QuerySet_list,5)
        page_request_var='page'
        page=request.GET.get(page_request_var)
        try:
            QuerySet=paginator.page(page)
        except PageNotAnInteger:
            QuerySet=paginator.page(1)
        except EmptyPage:
            QuerySet=paginator.page(paginator.num_pages)
        context={
            "object_list":QuerySet,
            "issue":"List",
            'page_request_var':page_request_var
        }
        return  render(request,"Nation_Portalapp/base.html",context)
    else:
        return HttpResponseRedirect(reverse('home'))

    # try:
    #     post=Post.objects.all.get(pk=Post_id)
    # except  Post.DoesNotExist:
    #     raise Http404("Post doesnt exist")
    # return  render(request,"index.html",{'post':post})
   # return HttpResponse("<h1> In Nation's Portal finally ::::))))) </h1>")

def detail(request,id):
    if request.user.is_authenticated:
        instance = get_object_or_404(Post, id=id)
        context = {
            "issue": instance.issue,
            "instance":instance,
            "location":instance.location
        }
        return render(request, "Nation_Portalapp/detail.html", context)
    else:
        return HttpResponseRedirect(reverse('home'))

def update_post(request,id):
    if request.user.is_authenticated:
        # return render(request, 'Nation_Portalapp/home.html')
        instance=get_object_or_404(Post,id=id)
        form = PostForm(request.POST or None,request.FILES or None,instance=instance)
        if(form.is_valid()):
            instance=form.save(commit=False)
            instance.save()
            messages.success(request,'Saved')
            return HttpResponseRedirect(instance.get_absolute_url())
        context={
            'issue':'Update',
            'instance':instance,
            'form':form,
        }
        return render(request,'Nation_Portalapp/create.html',context)
    else:
        return HttpResponseRedirect(reverse('home'))

def delete_post(request,id=None):
    if  request.user.is_superuser:
        # return render(request, 'Nation_Portalapp/home.html')
        instance=get_object_or_404(Post,id=id)
        instance.delete()
        #messages.success(request, "Successfully Deleted")
        QuerySet = Post.objects.all
        context = {
            "object_list": QuerySet,
            "issue": "List"
        }
        return render(request, "Nation_Portalapp/base.html", context)
    else:
        return HttpResponseRedirect(reverse('home'))

