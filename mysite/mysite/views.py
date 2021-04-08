from django.http import HttpResponse
from django import template
#from django.template.loader import get_template
from django.shortcuts import render_to_response

#from restaurants.models import Restaurant, Food

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

def welcome(request):
    if 'user_name' in request.GET and request.GET['user_name'] != '':
        return HttpResponse('welcome !!!' + request.GET['user_name'])
    else:
        return render_to_response('welcome.html', locals())

# def menu(request):
#     food1 = {'name': 'hamburger',
#             'price' : 199,
#             'comment' : 'great!',
#             'is_spicy' : False
#     }
#     food2 = {'name': 'fries',
#             'price' : 30,
#             'comment' : 'yummy!',
#             'is_spicy' : True
#     }
#     food3 = {'name': 'steak',
#             'price' : 500,
#             'comment' : 'awesome !!!!',
#             'is_spicy' : False
#     }
#     # django will pass foods to menu.html, and for loop all food via jinja syntax
#     foods = [food1, food2, food3]  
#     # locals() will return all local vars in this method
#     return render_to_response('menu.html', locals())


# def menu(request):
#     restaurants = Restaurant.objects.all()
#     return render_to_response("menu.html", locals())
