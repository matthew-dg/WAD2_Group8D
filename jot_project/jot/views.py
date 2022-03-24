from math import floor
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Q
from datetime import datetime

#call the upload function in Forms
from .forms import BookForm
from django.conf import settings

from .models import Book
from .models import Users

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

def index(request):
    model = Book
    model = Users
    keyword = request.GET.get('q')
    chosen_category = request.GET.get('chosen_category')
    visitor_cookie_handler(request)
    context_dict = {}
    if chosen_category == "user":
        print(chosen_category)
        print(keyword)
        if keyword:
            # author
         users_list = Users.objects.filter(username__icontains = keyword)
         print(users_list)

         context_dict['users_list'] = users_list



    if chosen_category == "book":
        if keyword:
            # author
         books_list = Book.objects.filter(book_title__icontains = keyword)
         print(books_list)

         context_dict['books_list'] = books_list
    #    context_dict['author_list'] = author_list
    context_dict['visits'] = request.session['visits']
    #    return render(request, 'jot/index.html', context=context_dict)
    return render(request, 'jot/index.html', context=context_dict)


def about(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'jot/about.html', context=context_dict)

def contactus(request):
    #maybe a dictionary of our information would be useful
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'jot/contactus.html', context=context_dict)

def categories(request):
    #we will need to collect the categories here, this will require a context dict
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'jot/categories.html', context=context_dict)

def surpriseme(request):
    #this will take an argument of a page fetched at random

    #potentually get rid of all of this and in the return return a page.html response??
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'jot/surpriseme.html', context=context_dict)

def book(request):
    #this will take an argument of a page fetched at random
    #fetch book here
    
    context_dict = {}

    rating = 3.41564455554345345345 #grab this from the book data/ api
    rating = floor(rating+0.5)

    test_star_colour = ['#f4f4f4'] * rating
    for count in range(rating):
        context_dict['star'+str(count+1)] = '#ffd800'

    visitor_cookie_handler(request)

    context_dict['visits'] = request.session['visits']

    return render(request, 'jot/book.html', context=context_dict)

def searchresults(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'jot/searchresults.html', context=context_dict)

# Not a view, this is just a helper function
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits += 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits
#i
#required login?
def upload_books(request):
    if request.method == 'POST' :
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()
        
    return render(request,'jot/addbook.html',{'form': form})

