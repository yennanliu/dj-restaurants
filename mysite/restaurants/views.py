from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django import template
from django.utils import timezone

from restaurants.models import Restaurant, Food

def menu(request, id):
    if id:
        restaurant = Restaurant.objects.get(id=id)
        return render_to_response("menu.html", locals())
    else:
        return HttpResponseRedirect("/restaurants_list/")

def list_restaurants(request):
    restaurants = Restaurant.objects.all()
    return render_to_response('restaurants_list.html', locals())

def comment(request, id):
    if id:
        r = Restaurant.objects.get(id=id)
    else:
        return HttpResponseRedirect("/restaurants_list/")
    if request.POST:
        visitor = request.POST['visitor']
        content = request.POST['content']
        email = request.POST['email']
        date_time = timezone.localtime(timezone.now())
        Comment.objects.create(
            visitor=visitor,
            email=email,
            content=content,
            date_time=date_time,
            restaurant=r
        )
    return render_to_response('comment.html', locals())

def meta(request):
    values = request.META.items()
    values.sort()
    html = []
    print ("=== meta ===")
    for k, v in values:
        print (k, v)
    print ("=== meta ===")

# def menu(request):
#     path = request.path
#     #restaurants = Restaurant.objects.all()
#     restaurant = Restaurant.objects.get(id=1)
#     print ("restaurant = " + str(restaurant))
#     return render_to_response("menu.html", locals())

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
