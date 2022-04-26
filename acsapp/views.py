from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Citizen
from json import dumps


def validate_pin(pin_to_validate: str) -> bool:
    """
    Function validates PIN.
    :param pin_to_validate: str
    """
    if pin_to_validate.isdigit() and len(pin_to_validate) == 11:
        return True
    return False


def index(request):
    """
    Main function that corresponds to main page.
    It gets a PIN from a form and presents address back to main page.
    """
    address = ''
    name_surename = ''

    if request.method == 'GET' and ('pin' in request.GET):
        pin = request.GET['pin']

        if validate_pin(pin):
            try:
                citizen = get_object_or_404(Citizen, pin=str(pin))
                citizen = citizen.get_address()
                name_surename = citizen['first_name'] + ' ' + citizen['last_name']
                address = citizen['address']
            except Http404:
                address = f"No address for PIN {pin}"
        else:
            address = f"{pin} is invalid PIN !"

    context = {'name_surename': name_surename, 'address': address}

    return render(request, 'acsapp/index.html', context)


def api_get_address(request, pin):
    """
    Function that work as API. It gets pin from an url
    and puts citizen's information with address.
    """
    if validate_pin(pin):
        try:
            citizen = get_object_or_404(Citizen, pin=str(pin))
        except Http404:
            return HttpResponse(f"No address for PIN {pin}")
    else:
        return HttpResponse(f"{pin} is invalid PIN !")

    return HttpResponse(dumps(citizen.get_address()))


def info(request):
    """
    Function for the info page.
    """
    return render(request, 'acsapp/info.html')
