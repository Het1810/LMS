# utils.py
from .models import CreLogs, CreModules, CreActions
from django.utils import timezone
# from pytz import timezone as pytz_timezone


def log_action(user, module_name, action_name, client=None, license=None):
    # Create and save a log entry
    module, created_module = CreModules.objects.get_or_create(nvarname=module_name)
    action, created_action = CreActions.objects.get_or_create(nvarname=action_name)

    # Get the current time in the local timezone
    # local_tz = pytz_timezone('Asia/Kolkata')
    # local_time = timezone.localtime(timezone.now(), local_tz)

    # if user.id is not None:
    log_entry = CreLogs.objects.create(
        intuserid=user,
        intmoduleid=module,
        intactionid=action,
        dtdatetime=timezone.now()#local_time
        )

    if client:
        log_entry.intclientid = client
    if license:
        log_entry.intlicenseid = license

    log_entry.save()
