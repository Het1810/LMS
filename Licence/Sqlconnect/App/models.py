from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from datetime import datetime

# Create your models here.


class CreUsers(AbstractUser):
    intid = models.AutoField(db_column='intId', primary_key=True)  # Field name made lowercase.
    nvarusername = models.CharField(db_column='nvarUsername', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    nvarpassword = models.CharField(db_column='nvarPassword', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    bitactive = models.BooleanField(db_column='bitActive')  # Field name made lowercase.

    groups = models.ManyToManyField('auth.Group', related_name='cre_users_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='cre_users_permissions', blank=True)

    def __str__(self):
        return self.nvarusername

    class Meta:
        managed = False
        db_table = 'CRE_Users'


class CreActions(models.Model):
    intid = models.IntegerField(db_column='intId', primary_key=True)  # Field name made lowercase.
    nvarname = models.CharField(db_column='nvarName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    def __str__(self):
        return self.nvarname

    class Meta:
        managed = False
        db_table = 'CRE_Actions'


class CreClientLicense(models.Model):
    intid = models.AutoField(db_column='intId', primary_key=True)  # Field name made lowercase.
    intclientid = models.ForeignKey('CreClients', models.DO_NOTHING, db_column='intClientId')  # Field name made lowercase.
    nvarkey = models.CharField(db_column='nvarKey', max_length=300, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    intvalidity = models.IntegerField(db_column='intValidity')  # Field name made lowercase.
    bitactive = models.BooleanField(db_column='bitActive', default=False)  # Field name made lowercase.
    intremoteid = models.IntegerField(db_column='intRemoteid')

    nvarremotepass = models.CharField(db_column='nvarRemotepass', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    nvarreference = models.CharField(db_column='nvarReference', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bitistrashed = models.BooleanField(db_column='bitIsTrashed', default=False)  # Field name made lowercase.

    def __str__(self):
        return str(self.intclientid_id)

    class Meta:
        managed = False
        db_table = 'CRE_Client_License'


class CreClients(models.Model):
    intid = models.AutoField(db_column='intId', primary_key=True)  # Field name made lowercase.
    nvarname = models.CharField(db_column='nvarName', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    nvaremail = models.EmailField(db_column='nvarEmail', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nvaraddress = models.CharField(db_column='nvarAddress', max_length=300, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nvarcontact = models.CharField(db_column='nvarContact', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    # created_at = models.DateTimeField(db_column='created_at', auto_now_add=True)
    # updated_at = models.DateTimeField(db_column='updated_at', auto_now=True)
    bitistrashed = models.BooleanField(db_column='bitIsTrashed', default=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRE_Clients'


class CreLicenseStatus(models.Model):

    intlicenseid = models.OneToOneField('CreClientLicense', models.DO_NOTHING, db_column='intLicenseId', primary_key=True)  # Field name made lowercase.
    nvarmacaddress = models.CharField(db_column='nvarMacAddress', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    dtstartdate = models.DateTimeField(db_column='dtStartDate', default=datetime(2024,1,1))  # Field name made lowercase.
    dtenddate = models.DateTimeField(db_column='dtEndDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRE_License_Status'


class CreLogs(models.Model):
    intid = models.BigAutoField(db_column='intId', primary_key=True)  # Field name made lowercase.
    intuserid = models.ForeignKey('CustomUser', models.DO_NOTHING, db_column='intUserId')  # Field name made lowercase.
    intmoduleid = models.ForeignKey('CreModules', models.DO_NOTHING, db_column='intModuleId')  # Field name made lowercase.
    intactionid = models.ForeignKey('CreActions', models.DO_NOTHING, db_column='intActionId')  # Field name made lowercase.
    intclientid = models.ForeignKey('CreClients', models.DO_NOTHING, db_column='intclientid', null=True, blank=True)
    intlicenseid = models.ForeignKey('CreClientLicense', models.DO_NOTHING, db_column='intlicenseid', null=True, blank=True)
    dtdatetime = models.DateTimeField(db_column='dtDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRE_Logs'


class CreModules(models.Model):
    intid = models.AutoField(db_column='intId', primary_key=True)  # Field name made lowercase.
    nvarname = models.CharField(db_column='nvarName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    def __str__(self):
        return self.nvarname

    class Meta:
        managed = False
        db_table = 'CRE_Modules'


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
