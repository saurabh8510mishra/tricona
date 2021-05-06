from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def dashboard(request):
    return render(request,'index.html')

def dashboard2(request):
    return render(request,'index-2.html')
