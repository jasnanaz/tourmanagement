from django.shortcuts import render
# Create your views here.
def design(request):
    return render(request,"firstapp/kt.html")
# Create your views here.
# def designedit(request):
#     return render(request,"firstapp/ktedit.html")
def destinations(request):
    return render(request,"firstapp/destinations.html")