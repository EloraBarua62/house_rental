from django.shortcuts import render
from django.contrib import messages
from .forms import HouseInfoForm, RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import HouseDetails
from django.http import JsonResponse


# Create your views here.
def frontpage(request):
    house_list = HouseDetails.objects.all()
    return render(request, 'frontpage.html', {'house_list': house_list})
    #return render(request, 'frontpage.html')


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
            login(request, user)
            messages.info(request, f"Log In Successfully!!")
    else:
        fm = AuthenticationForm()
    return render(request, 'login.html', {'form': fm})


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
def autosuggest(request):
    query = request.GET.get('term')
    print(request.GET)
    mylist = []
    if query:
        query_set = HouseDetails.objects.filter(location__icontains=query)

        for address in query_set:
            mylist.append(address.location)

    return JsonResponse(mylist, safe=False)


def house_search(request):
    # search = HouseDetails.objects.filter(location=True)
    return render(request, 'house_search.html')


def house_details(request, pk):
    detail = HouseDetails.objects.get(id=pk)
    return render(request, 'details.html', {'detail': detail})
