from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django import template
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from restaurants.permissions import user_can_comment

from django.utils.decorators import method_decorator
from django.utils import timezone

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import FormView

from restaurants.models import Restaurant, Food, Comment
from restaurants.forms import CommentForm



# def menu(request):
#     """retrun a menu response
#     :request: client request
#     :returns: http response
#     """
#     if 'id' in request.GET and request.GET['id'] != '':
#         restaurant = Restaurant.objects.get(id=request.GET['id'])
#         return render_to_response('menu.html', locals())
#     else:
#         return HttpResponseRedirect("/restaurants_list/")

class MenuView(DetailView):

    model = Restaurant
    template_name = 'menu.html'
    context_object_name = 'restaurant'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(MenuView, self).dispatch(request, *args, **kwargs)

    # overwrite get method
    def get(self, request, pk, *args, **kwargs):
        try:
            return super(MenuView, self).get(self, request, pk=pk, *args, **kwargs)
        except Http404:
            return HttpResponseRedirect('/restaurants_list/')

# @login_required
# def list_restaurants(request):
#     restaurants = Restaurant.objects.all()
#
#     print (request.user.user_permissions.all())
#     # try to storage object via session
#     request.session['restaurants'] = restaurants
#     return render_to_response('restaurants_list.html', RequestContext(request, locals()))

class RestaurantView(ListView):

    model = Restaurant
    template_name = 'restaurants_list.html'
    context_object_name = "restaurants"



class CommentView(FormView, SingleObjectMixin):

    """View associated with form"""

    form_class = CommentForm
    template_name = 'comment.html'
    success_url = '/comment/'
    initial = {'content': u'I have no idea'}
    model = Restaurant
    context_object_name = 'r'

    def form_valid(self, form):
        """form is validated, so use form data to create comment
        :form: validated form
        :returns: origin form_valid
        """
        Comment.objects.create(
            visitor=form.cleaned_data['visitor'],
            email=form.cleaned_data['email'],
            content=form.cleaned_data['content'],
            date_time=timezone.localtime(timezone.now()),
            restaurant=self.get_object()
        )
        return self.render_to_response(self.get_context_data(
                form=self.form_class(initial=self.initial))
        )

    def get_context_data(self, **kwargs):
        """ assign attribute "object" that indicates the query object
        :returns: origin context get from get_context_data with additional object parameter
        """
        self.object = self.get_object()
        return super(CommentView, self).get_context_data(object=self.object, **kwargs)

    @method_decorator(user_passes_test(user_can_comment, login_url='/accounts/login/'))
    def dispatch(self, request, *args, **kwargs):
        """ return decorated dispatch
        :request: request
        :returns: return origin dispatch
        """
        return super(CommentView, self).dispatch(request, *args, **kwargs)

def meta(request):
    values = request.META.items()
    values.sort()
    html = []
    print ("=== meta ===")
    for k, v in values:
        print (k, v)
    print ("=== meta ===")


# @permission_required('restaurants.can_comment', login_url='/accounts/login/')
# def comment(request, id):
#     if id:
#         r = Restaurant.objects.get(id=id)
#     else:
#         return HttpResponseRedirect("/restaurants_list/")
#     if request.POST:
#         f = CommentForm(request.POST)
#         if f.is_valid():
#             visitor = f.cleaned_data['visitor']
#             content = f.cleaned_data['content']
#             email = f.cleaned_data['email']
#             date_time = timezone.localtime(timezone.now())
#             c = Comment.objects.create(
#                 visitor=visitor,
#                 email=email,
#                 content=content,
#                 date_time=date_time,
#                 restaurant=r
#                 )
#             f = CommentForm()

#     else:
#         f = CommentForm()

#     return render_to_response('comment.html', RequestContext(request, locals())) 

# def menu(request, id):
#     if id:
#         restaurant = Restaurant.objects.get(id=id)
#         return render_to_response("menu.html", locals())
#     else:
#         return HttpResponseRedirect("/restaurants_list/")

# def comment(request, id):
#     errors = []
#     if id:
#         r = Restaurant.objects.get(id=id)
#     else:
#         return HttpResponseRedirect("/restaurants_list/")
#     if request.POST:
#         visitor = request.POST['visitor']
#         content = request.POST['content']
#         email = request.POST['email']
#         date_time = timezone.localtime(timezone.now())

#         # error handling
#         if any(not request.POST[k] for k in request.POST):
#             errors.append('* there is some blank field, plz fill again')

#         if '@' not in email:
#             errors.append('* email format not correct, plz fill again')

#         if not errors:
#             Comment.objects.create(
#                 visitor=visitor,
#                 email=email,
#                 content=content,
#                 date_time=date_time,
#                 restaurant=r
#             )
#             #visitor, email, content = ('', '', '')
#     f = CommentForm()
#     return render_to_response('comment.html', RequestContext(request, locals()))

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
