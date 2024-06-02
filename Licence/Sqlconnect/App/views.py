from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .utils import log_action
from .filters import LogFilter
from django.utils import timezone
from datetime import datetime, timedelta
from django.http import JsonResponse, HttpResponseRedirect
from .forms import CustomAuthenticationForm, ClientForm,  LicenceForm, LicencestatusForm
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import CreClients, CreClientLicense, CreLicenseStatus, CreLogs


def login_view(request):

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:

                login(request, user)

                log_action(user, 'Authentication', 'Login')

                # Redirect to the desired page after login
                next_url = request.GET.get('next')
                print("NEXT Url:", next_url)
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('client')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})


@login_required(login_url='login')
def client_view(request):

    # users_data = CreClients.objects.all()
    users_data = CreClients.objects.filter(bitistrashed=False)
    context = {'users_data': users_data}

    # log_action(request.user, 'Client Management', 'View Clients')

    return render(request, 'client.html', context)


@login_required(login_url='login')
def edit_client(request, client_id):
    client = get_object_or_404(CreClients, intid=client_id)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.updated_at = timezone.now()
            form.save()

            log_action(request.user, 'Client Management', 'Edit Client', client=client)

            return redirect('client')

    else:
        form = ClientForm(instance=client)

    return render(request, 'edit_client.html', {'form': form, 'client': client})


def delete_client(request, client_id):
    client = get_object_or_404(CreClients, intid=client_id)
    client.bitistrashed = True
    client.save()

    log_action(request.user, 'Client Management', 'Delete Client', client=client)
    return JsonResponse({'success': True})


@login_required(login_url='login')
def client_add_view(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            new_client = form.save()
            log_action(request.user, 'Client Management', 'Add Client')
            return redirect('client')
    else:
        form = ClientForm()

    context = {'form': form}

    return render(request, 'client_form.html', context)


def logout_view(request):
    # logout(request)
    log_action(request.user, 'Authentication', 'Logout')
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def licence_view(request, client_id):
    # Retrieve data from the database
    client = CreClients.objects.get(intid=client_id)
    data = CreClientLicense.objects.select_related('crelicensestatus').filter(intclientid=client_id, bitistrashed=False)
    # data = CreClientLicense.objects.all()

    log_action(request.user, 'License Management', 'View Licenses', client=client)
    context = {'data': data, 'client': client}

    return render(request, 'licence_view.html', context)


def delete_licence(request, client_id):
    client = get_object_or_404(CreClientLicense, intid=client_id)
    client.bitistrashed = True
    client.save()

    log_action(request.user, 'License Management', 'Delete License', license=client)
    return JsonResponse({'success': True})


@login_required(login_url='login')
def license_add_view(request, intclientid):
    client = CreClients.objects.get(intid=intclientid)
    if request.method == 'POST':
        form = LicenceForm(request.POST)
        if form.is_valid():
            # Save the form without committing to the database
            client_license = form.save(commit=False)
            # Set intclientid from the URL
            client_license.intclientid_id = intclientid
            # Do additional processing if needed before saving
            # Save to the database
            client_license.save()

            log_action(request.user, 'License Management', 'Add License', client=client)
            return redirect('licence', client_id=form.instance.intclientid_id)  # Redirect to a success page
    else:
        # If it's a GET request, create a form without initial values
        form = LicenceForm()

    context = {'form': form, 'client': client}
    return render(request, 'licence_form.html', context)


@login_required(login_url='login')
def licence_edit(request, intclientid):
    # Retrieve the existing license instance
    client_license = get_object_or_404(CreClientLicense, intid=intclientid)
    # client = CreClients.objects.get(intid=intclientid)

    # Store the previous page URL in the session
    # referring_page = request.session.get('referring_page')
    # if not referring_page:
    #     referring_page = request.META.get('HTTP_REFERER', None)
    #     request.session['referring_page'] = referring_page
    #     print("Referring page set:", referring_page)

    referring_page = request.POST.get('referring_page')
    if request.method == 'POST':
        form = LicenceForm(request.POST, instance=client_license)
        if form.is_valid():
            print("Form is valid")
            form.save()

            log_action(request.user, 'License Management', 'Edit License',  license=client_license)#, client=client)

            if referring_page:
                return redirect(referring_page)
            else:
                # return redirect('licence')
            # return redirect(request.META.get('HTTP_REFERER', 'licence'))  # Redirect to 'home' if referring page is not available
                return redirect('licence', client_id=form.instance.intclientid_id)  # Redirect to a success page
        else:
            print("Form errors:", form.errors)
    else:
        form = LicenceForm(instance=client_license)

    context = {'form': form, 'client_license': client_license}#, 'client': client}

    return render(request, 'licence_edit.html', context)


@login_required(login_url='login')
def remote(request, client_id):
    client = CreClients.objects.get(intid=client_id)
    # data = CreClientLicense.objects.select_related('crelicensestatus').filter(intclientid=client_id, bitistrashed=False)
    data = CreClientLicense.objects.filter(intclientid=client_id, bitistrashed=False)

    # log_action(request.user, 'License Management', 'View Licenses', license=data)
    context = {'data': data, 'client': client}

    return render(request, 'remote.html', context)


@login_required(login_url='login')
def logs_view(request):
    logs_data = CreLogs.objects.all()

    # today = datetime.now().date()
    # logs_data = logs_data.filter(dtdatetime__date=today)

    log_filter = LogFilter(request.GET, queryset=logs_data)

    context = {'logs_data': log_filter.qs, 'log_filter': log_filter}

    return render(request, 'logs_view.html', context)
