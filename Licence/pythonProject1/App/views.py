from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from .models import Client, Licence
from .forms import ClientForm, LicenseForm

# Create your views here.


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('client')

                # return redirect(request.GET.get('next', 'client'))
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


@login_required(login_url='login')
def edit_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.updated_at = timezone.now()
            form.save()
            return redirect('client')

    else:
        form = ClientForm(instance=client)

    return render(request, 'edit_client.html', {'form': form, 'client': client})


def delete_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    client.is_flagged = True
    client.save()

    return JsonResponse({'success': True})


@login_required(login_url='login')
def client_view(request):
    # Retrieve data from the database
    data = Client.objects.filter(is_flagged=False)

    context = {'data': data}

    return render(request, 'client.html', context)


@login_required(login_url='login')
def client_add_view(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client')
    else:
        form = ClientForm()

    context = {'form': form}

    return render(request, 'client_form.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def licence_view(request, client_id):
    # Retrieve data from the database
    client = Client.objects.get(client_id=client_id)
    data = Licence.objects.get(client=client)

    context = {'data': data}

    return render(request, 'licence_view.html', context)


@login_required(login_url='login')
def edit_license(request, client_id):
    client = get_object_or_404(Licence, id=client_id)

    if request.method == 'POST':
        form = LicenseForm(request.POST, instance=client)
        if form.is_valid():
            # instance = form.save(commit=False)
            # instance.updated_at = timezone.now()
            form.save()
            return redirect('client')

    else:
        form = LicenseForm(instance=client)

    return render(request, 'edit_license.html', {'form': form, 'client': client})
