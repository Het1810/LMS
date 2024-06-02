# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aspnetroles(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=256, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspNetRoles'


class Aspnetuserclaims(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Aspnetusers', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
    claimtype = models.TextField(db_column='ClaimType', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    claimvalue = models.TextField(db_column='ClaimValue', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspNetUserClaims'


class Aspnetuserlogins(models.Model):
    loginprovider = models.CharField(db_column='LoginProvider', primary_key=True, max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (LoginProvider, ProviderKey, UserId) found, that is not supported. The first column is selected.
    providerkey = models.CharField(db_column='ProviderKey', max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    userid = models.ForeignKey('Aspnetusers', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspNetUserLogins'
        unique_together = (('loginprovider', 'providerkey', 'userid'),)


class Aspnetuserroles(models.Model):
    userid = models.OneToOneField('Aspnetusers', models.DO_NOTHING, db_column='UserId', primary_key=True)  # Field name made lowercase. The composite primary key (UserId, RoleId) found, that is not supported. The first column is selected.
    roleid = models.ForeignKey(Aspnetroles, models.DO_NOTHING, db_column='RoleId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspNetUserRoles'
        unique_together = (('userid', 'roleid'),)


class Aspnetusers(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=256, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    emailconfirmed = models.BooleanField(db_column='EmailConfirmed')  # Field name made lowercase.
    passwordhash = models.TextField(db_column='PasswordHash', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    securitystamp = models.TextField(db_column='SecurityStamp', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.TextField(db_column='PhoneNumber', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phonenumberconfirmed = models.BooleanField(db_column='PhoneNumberConfirmed')  # Field name made lowercase.
    twofactorenabled = models.BooleanField(db_column='TwoFactorEnabled')  # Field name made lowercase.
    lockoutenddateutc = models.DateTimeField(db_column='LockoutEndDateUtc', blank=True, null=True)  # Field name made lowercase.
    lockoutenabled = models.BooleanField(db_column='LockoutEnabled')  # Field name made lowercase.
    accessfailedcount = models.IntegerField(db_column='AccessFailedCount')  # Field name made lowercase.
    username = models.CharField(db_column='UserName', unique=True, max_length=256, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspNetUsers'


class CreActions(models.Model):
    intid = models.IntegerField(db_column='intId', primary_key=True)  # Field name made lowercase.
    nvarname = models.CharField(db_column='nvarName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRE_Actions'


class CreClientLicense(models.Model):
    intid = models.AutoField(db_column='intId', primary_key=True)  # Field name made lowercase.
    intclientid = models.ForeignKey('CreClients', models.DO_NOTHING, db_column='intClientId')  # Field name made lowercase.
    nvarkey = models.CharField(db_column='nvarKey', max_length=300, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    intvalidity = models.IntegerField(db_column='intValidity')  # Field name made lowercase.
    bitactive = models.BooleanField(db_column='bitActive')  # Field name made lowercase.
    nvarreference = models.CharField(db_column='nvarReference', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bitistrashed = models.BooleanField(db_column='bitIsTrashed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRE_Client_License'


class CreClients(models.Model):
    intid = models.AutoField(db_column='intId', primary_key=True)  # Field name made lowercase.
    nvarname = models.CharField(db_column='nvarName', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    nvaremail = models.CharField(db_column='nvarEmail', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nvaraddress = models.CharField(db_column='nvarAddress', max_length=300, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nvarcontact = models.CharField(db_column='nvarContact', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bitistrashed = models.BooleanField(db_column='bitIsTrashed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRE_Clients'


class CreLicenseStatus(models.Model):
    intlicenseid = models.OneToOneField(CreClientLicense, models.DO_NOTHING, db_column='intLicenseId', primary_key=True)  # Field name made lowercase.
    nvarmacaddress = models.CharField(db_column='nvarMacAddress', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    dtstartdate = models.DateTimeField(db_column='dtStartDate')  # Field name made lowercase.
    dtenddate = models.DateTimeField(db_column='dtEndDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRE_License_Status'


class CreLogs(models.Model):
    intid = models.BigAutoField(db_column='intId', primary_key=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserId')  # Field name made lowercase.
    intmoduleid = models.ForeignKey('CreModules', models.DO_NOTHING, db_column='intModuleId')  # Field name made lowercase.
    intactionid = models.ForeignKey(CreActions, models.DO_NOTHING, db_column='intActionId')  # Field name made lowercase.
    dtdatetime = models.DateTimeField(db_column='dtDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRE_Logs'


class CreModules(models.Model):
    intid = models.IntegerField(db_column='intId', primary_key=True)  # Field name made lowercase.
    nvarname = models.CharField(db_column='nvarName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRE_Modules'


class CreUsers(models.Model):
    intid = models.AutoField(db_column='intId', primary_key=True)  # Field name made lowercase.
    nvarusername = models.CharField(db_column='nvarUsername', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    nvarpassword = models.CharField(db_column='nvarPassword', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    bitactive = models.BooleanField(db_column='bitActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRE_Users'
