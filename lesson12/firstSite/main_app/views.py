from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
import asyncio
from django.http import JsonResponse
import httpx
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the index page.")


def about(request):
    coworkers_db = [
        {
            "first_name": "John",
            "last_name": "Johnson",
            "profession": "Manager",
            "salary": "1000$",
        },
        {
            "first_name": "Jack",
            "last_name": "Jackson",
            "profession": "Developer",
            "salary": "800$",
        },
        {
            "first_name": "Jane",
            "last_name": "Janeway",
            "profession": "Developer",
            "salary": "800$",
        },
        {
            "first_name": "Joan",
            "last_name": "Joanson",
            "profession": "Analyst",
            "salary": "900$",
        },
        {
            "first_name": "Jill",
            "last_name": "Jillson",
            "profession": "Tester",
            "salary": "700$",
        },
    ]

    return render(request, './about.html', {'coworkers': coworkers_db})


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you for your message!")
    else:
        form = ContactForm()

    return render(request, './contactPage.html', {'form': form})


def view_contact_data(request):
    contacts = Contact.objects.all()
    return render(request, './getContacts.html', {'contacts': contacts})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration success!")
            return redirect("./auth/login.html")
        messages.error(
            request, "Registration unsuccessful, invaild information!")
    form = NewUserForm()

    return render(request=request, template_name="./auth/register.html", context={"register_form": form})


async def async_view(request):
    # განახორციელებს ასინქრონულ პროცესებს
    print("some stuff")
    await asyncio.sleep(3)
    print("another stuff")
    # return JsonResponse({'message': 'Async view response'})
    return HttpResponse("Async process result")


async def fetch_data_from_api(request):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://pokeapi.co/api/v2/pokemon/151")

        return JsonResponse(response.json())


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                # return redirect("main_app:index")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm()

    return render(request=request, template_name="./auth/login.html", context={"login_form": form})


async def crypto_converter(request):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.coincap.io/v2/assets")
        response = response.json()

        from_crypto = request.POST.get('from')
        to_crypto = request.POST.get('to')
        amount = request.POST.get('amount')

        price_of_from_crypto = 0
        price_of_to_crypto = 0

        for crypto in response["data"]:
            if crypto["name"] == from_crypto:
                price_of_from_crypto = crypto["priceUsd"]

            if crypto["name"] == to_crypto:
                price_of_to_crypto = crypto["priceUsd"]

        converted_amount = float(
            amount) * (float(price_of_from_crypto) / float(price_of_to_crypto))

        return render(request=request, template_name="./cryptoConverter.html", context={"cryptos": response["data"][0:10], "converted_amount": converted_amount})
