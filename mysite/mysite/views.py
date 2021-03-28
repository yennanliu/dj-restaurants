from django.http import HttpResponse

def here(request):
    return HttpResponse("helloooo! i am here !!")

def add(request, a, b):
    s = int(a) + int(b)
    return HttpResponse(str(s))