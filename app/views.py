from django.shortcuts import render

# Create your views here.
def pinky(request):
    return render(request,'pinky.html')