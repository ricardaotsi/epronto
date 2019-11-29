from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,"eprontosite/index.html")

@login_required
def dashboard_home(request):
    return render(request,"eprontosite/dashboard.html")