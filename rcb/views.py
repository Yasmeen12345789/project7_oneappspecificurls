from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return render(request,'rcb.html')

def chahal (request):
    return HttpResponse("chahal is best bowler")
 
