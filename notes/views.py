# Create your views here.

from django.shortcuts import redirect

def get_out(request):
    return redirect("main.views.home")
