from django.http import HttpResponse
from django import template
#from django.template.loader import get_template
from django.shortcuts import render_to_response

def here(request):
    return HttpResponse("helloooo! i am here !!")

def add(request, a, b):
    a = int(a)
    b = int(b)
    s = a + b 
    d = a - b
    p = a * b
    q = a / b
    return render_to_response(
        'math.html',
        {'s': s, 'd' : d, 'p': p, 'q': q}
    )
    #t = get_template('math.html')
    #t = template.Template('<html>sum= {{s}}<br>dif = {{d}}<br>pro={{p}} <br> quo = {{q}} </html>')
    #c = template.Context({'s': s, 'd' : d, 'p': p, 'q': q})
    #return HttpResponse(t.render(c))
    # s = int(a) + int(b)
    # return HttpResponse(str(s))