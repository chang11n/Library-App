
# Import necessary classes
from django.shortcuts import render
from django.http import HttpResponse
from libapp.models import Book, Dvd, Libuser, Libitem, Suggestion
from libapp.forms import SuggestionForm, SearchlibForm, RegisterForm
from django.conf.urls import patterns, url
from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User



# Create your views here.
def index(request):

    # booklist = Book.objects.all() [:10]
    # dvdlist = DVD.objects.all().order_by('-pubyr')[:5]
    # response = HttpResponse()
    # heading1 = '<p>' + 'List of books: ' + '</p>'
    # response.write(heading1)
    # for book in booklist:
    #     para = '<p>' + str(book) + '</p>'
    #     response.write(para)
    #
    # heading2 = '<p>' + 'List of dvds: ' + '</p>'
    # response.write(heading2)
    # for dvd in dvdlist:
    #     para = '<p>' + str(dvd) + str(DVD.objects.values('pubyr').filter(pubyr__contains=dvd.pubyr)) + '</p>'
    #     response.write(para)
    # return response

    itemlist = Libitem.objects.all().order_by('title')[:10]
    return render(request, "libapp/index.html", {'itemlist': itemlist})


def about(request):
    response=HttpResponse()
    response.set_cookie('about_vistis')
    return render(request,'libapp/about.html')


def detail(request, item_id):
    # response = HttpResponse()
    # try:
    #     Book.objects.get(id=str(item_id))
    #     list=Book.objects.values('title', 'duedate', 'author').filter(id=str(item_id))
    # except:
    #     try:
    #         DVD.objects.get(id=str(item_id))
    #         list = DVD.objects.values('title', 'duedate', 'maker').filter(id=str(item_id))
    #     except:
    #         raise Http404
    # response.write(list)
    # return response
    try:
        item = Libitem.objects.get(pk=item_id)
        if item.itemtype == 'Book':
            item = Book.objects.get(pk=item_id)
        else:
            item = DVD.objects.get(pk=item_id)
    except:
        raise Http404
    return render(request, 'libapp/detail.html',{'item': item})


def suggestions(request):
    suggestionlist = Suggestion.objects.all()[:10]
    return render(request, 'libapp/suggestions.html', {'itemlist': suggestionlist})


def newitem(request):
    suggestionss = Suggestion.objects.all()
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.num_interested = 1
            suggestion.save()
            return HttpResponseRedirect(reverse('libapp:suggestions'))
        else:
            return render(request, 'libapp/newitem.html', {'form': form, 'suggestions': suggestionss})
    else:
        form = SuggestionForm()
        return render(request, 'libapp/newitem.html', {'form': form, 'suggestions': suggestionss})


def searchlib(request):
    if request.method == 'GET':
        form = SearchlibForm()
        return render(request, 'libapp/searchlib.html')
    else:
        return HttpResponseRedirect(reverse('libapp:searchlib'))


def result(request):
    if 'q' in request.GET:
        if 'p' in request.GET:
            p = request.GET['p']
            q = request.GET['q']
            books = Book.objects.filter(title__icontains=q).filter(author__icontains=p)
        return render(request,'libapp/result.html', {'books': books, 'title': q, 'author':p})
    else:
        message = 'You submitted an empty form.'
        return HttpResponse(message)


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('libapp:index'))
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        return render(request, 'libapp/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(('libapp:index')))


def myitems(request):
    if request.user.is_authenticated():
        try:
            Libuser.objects.get(username=request.user)
        except:
            return HttpResponse('You are not a Libuser')
        myitem=Libitem.objects.filter(checked_out=True).filter(user=request.user)
        return render(request, 'libapp/myitems.html',{'myitem':myitem})
    else:
        return HttpResponse('login please')


# def register(request):
#     user = User.objects.all()
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.num_interested = 1
#             user.save()
#             return HttpResponseRedirect(reverse('libapp:index'))
#         else:
#             return render(request, 'libapp/register.html', {'form': form, 'users': user})
#     else:
#         form = RegisterForm()
#         return render(request, 'libapp/register.html', {'form': form, 'users': user})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
            firstname=request.POST['first_name']
            lastname=request.POST['last_name']
            user = Libuser.objects.create_user(username, email, password)
            user.last_name=lastname
            user.first_name=firstname
            user.save()
            return HttpResponseRedirect(reverse( 'libapp:index'))
        else:
            return render(request, 'libapp/register.html',{'form':form})
    else:
        form = RegisterForm()
        return render(request,'libapp/register.html',{'form':form})






