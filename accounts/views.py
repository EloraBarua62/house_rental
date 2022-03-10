import json
import folium
import geocoder
from django.db.models import Avg
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import HouseInfoForm, RegistrationForm, SearchForm, HouseRateForm, ShowMapForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import HouseDetails, HouseRate, ShowMap
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect

# check login and logout
login_res = 1


# Create your views here.
def frontpage(request):
    return render(request, 'frontpage.html')


# index html
def index(request):
    print(login_res)
    return render(request, 'index.html', {'login_res': login_res})


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
            print(login_res)
            return redirect('/')
    else:
        fm = AuthenticationForm()
    return render(request, 'login.html', {'form': fm})


def logout_form(request):
    global login_res
    login_res = 1
    logout(request)
    return redirect('/')


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


house_list = []


def show_house(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            global house_list
            house_list = HouseDetails.objects.filter(location__icontains=query).order_by('size', 'price')

            flat = 0
            duplex = 0
            commercial_space = 0
            sublet = 0
            return render(request, 'show_house.html',
                          {'house_list': house_list, 'query': query, 'login_res': login_res, 'flat': flat,
                           'duplex': duplex, 'commercial_space': commercial_space, 'sublet': sublet})
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
    print(detail, 'detail')
    min_range = detail.price - 2000
    max_range = detail.price + 2000
    global house_list
    house_list = house_list.filter(price__range=[min_range, max_range])
    return render(request, 'details.html', {'house_list': house_list, 'detail': detail})


def submit_review(request, p_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            print(url, p_id)
            reviews = HouseRate.objects.get(user__id=request.user.id, product__id=p_id)
            form = HouseRateForm(request.POST, instance=reviews)
            print(12)
            form.save()
            messages.success(request, 'Thank you! Your review has been updated')
            return redirect(reverse_lazy(url))
        except HouseRate.DoesNotExist:
            form = HouseRateForm(request.POST)
            if form.is_valid():
                data = HouseRate()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.p_id = p_id
                data.user_id = request.user.id
                data.save()

                messages.success(request, 'Thank you!Your data in stored')
                return redirect(url)
    return redirect(url)


def mapview(request):
    # location = geocoder.osm('UK')
    # lat = location.lat
    # lng = location.lng
    # country = location.country
    # # create map object
    # m = folium.Map(location=[19, -12], zoom_start=2)
    # folium.Marker([5.594, -0.219], tooltip='CLick for more', popup='Ghana').add_to(m)
    # folium.Marker([lat, lng], tooltip='CLick for more', popup=country).add_to(m)
    # m = m._repr_html_()
    # context = {
    #     'm': m
    # }

    if request.method == 'POST':
        form = ShowMapForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/map')
    else:
        form = ShowMapForm()

        # geocoder code
    address = ShowMap.objects.all().last()

    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country

    # correct area na dily data ty add hobe na
    # if lat == None or lng == None:
    #     address.delete()
    #     return HttpResponse('Your location input is invalid')

    # create map for bangladesh lat,lng and location num ok

    m = folium.Map(location=[23.684994, 90.356331], zoom_start=4)

    folium.Marker([lat, lng], tooltip='click for more', icon=folium.Icon(color='green', icon='cloud'),
                  popup="<strong>Bangladesh</strong>").add_to(m)

    # we can want to add 8 division marker map to our creat map
    folium.Marker(location=[24.903561, 91.873611], tooltip='click for more',
                  icon=folium.Icon(color='red', icon='envelope'),
                  popup="<strong>Sylhet</strong>").add_to(m)
    folium.Marker(location=[24.098379, 90.328712], tooltip='click for more',
                  icon=folium.Icon(color='red', icon='cloud'),
                  popup="<strong>Dhaka</strong>").add_to(m)
    # baki gula per day ty nity hobe
    folium.Marker(location=[24.376930, 88.603073], tooltip='click for more',
                  icon=folium.Icon(color='red', icon='envelope'),
                  popup="<strong>Rajshahi</strong>").add_to(m)
    folium.Marker(location=[22.841930, 89.558060], tooltip='click for more',
                  icon=folium.Icon(color='red', icon='cloud'),
                  popup="<strong>Khulna</strong>").add_to(m)
    folium.Marker(location=[22.700411, 90.374992], tooltip='click for more',
                  icon=folium.Icon(color='red', icon='envelope'),
                  popup="<strong>Barishal</strong>").add_to(m)
    folium.Marker(location=[22.330370, 91.832626], tooltip='click for more',
                  icon=folium.Icon(color='red', icon='cloud'),
                  popup="<strong>Chittagong</strong>").add_to(m)
    folium.Marker(location=[24.744221, 90.403008], tooltip='click for more',
                  icon=folium.Icon(color='red', icon='envelope'),
                  popup="<strong>Mymensingh</strong>").add_to(m)
    folium.Marker(location=[25.740580, 89.261139], tooltip='click for more',
                  icon=folium.Icon(color='red', icon='cloud'),
                  popup="<strong>Rangpur</strong>").add_to(m)

    m = m._repr_html_()
    context = {
        'm': m,
        'form': form,
    }

    return render(request, 'map.html', context)
