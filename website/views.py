from django.shortcuts import render


def home(request):
    return render(request,'website/index.html')

def resume(request):
    return render(request,'website/resume.html')

def projects(request):
    return render(request,'website/projects.html')

def contact(request):
    return render(request,'website/contact.html')