import json

from django.shortcuts import render
from django.contrib import messages
from .forms import HouseInfoForm, RegistrationForm, SearchForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import HouseDetails
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect

# check login and logout
login_res = 1


# Create your views here.
def frontpage(request):
    return render(request, 'frontpage.html')


# index html
def index(request):
    return render(request, 'index.html', {'login_res': login_res})


def house_search(request):
    return render(request, 'house_search.html')


def reg_form(request):
    if request.method == 'POST':
        fm = RegistrationForm(request.POST)
        print(request.POST)
        if fm.is_valid():
            fm.save(commit=True)
            messages.info(request, f"Your account is created")
            # return redirect("/")
    else:
        fm = RegistrationForm()
    return render(request, 'regform.html', {'form': fm})


def login_form(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        # print(request.POST, fm.data)
        username = fm.data['username']
        password = fm.data['password']
        # print(username, password)
        user = authenticate(username=username, password=password)
        # print(user)
        if user is not None:
            global login_res
            login_res = 0
            login(request, user)
            messages.info(request, f"Log In Successfully!!")
            return redirect('/')
    else:
        fm = AuthenticationForm()
    return render(request, 'login.html', {'form': fm})


def logout(request):
    global login_res
    login_res = 1
    logout(request)
    return HttpResponseRedirect('/index/')


def houseinfo(request):
    if request.method == 'POST':
        fm = HouseInfoForm(request.POST, request.FILES)
        print(request.POST)
        if fm.is_valid():
            fm.save(commit=True)
            messages.info(request, f"Your property has been posted")
    else:
        fm = HouseInfoForm()
    # house_record = HouseDetails.objects.all().count()
    # return HttpResponse(house_record)
    return render(request, 'houseinfo.html', {'form': fm})


# def house_listview(request):
#     houselist = HouseDetails.objects.all()
#     # lastimage = HouseDetails.objects.last()
#     # imagefile = lastimage.imagefile
#     return render(request, 'houselist.html', {'houselist': houselist})


# def show_house(request):
#     house_list = HouseDetails.objects.all()
#     return render(request, 'show_house.html', {'house_list': house_list})


# Autocomplete search
# def autosuggest(request):
#     query = request.GET.get('term')
#     print(request.GET)
#     mylist = []
#     if query:
#         query_set = HouseDetails.objects.filter(location__icontains=query)
#
#         for address in query_set:
#             mylist.append(address.location)
#
#     return JsonResponse(mylist, safe=False)

house_list = []


def show_house(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            global house_list
            house_list = HouseDetails.objects.filter(location__icontains=query).order_by('size', 'price')
            return render(request, 'show_house.html',
                          {'house_list': house_list, 'query': query, 'login_res': login_res})
    return HttpResponseRedirect('/')


####### AutoSearch API ######
def auto_house(request):
    if request.is_ajax():
        q = request.GET.get('term')
        places = HouseDetails.objects.filter(location__icontains=q)
        results = []
        for pl in places:
            place_json = {}
            place_json = pl.location
            results.append(place_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def house_details(request, pk):
    detail = HouseDetails.objects.get(id=pk)
    min_range = detail.price-2000
    max_range = detail.price+2000
    global house_list
    house_list = house_list.filter(price__range=[min_range, max_range])
    return render(request, 'details.html', {'detail': detail, 'house_list': house_list})
