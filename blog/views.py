from django.shortcuts import render

# Create your views here.
#修改一下
def home(request):
    return render(request, 'home.html')
