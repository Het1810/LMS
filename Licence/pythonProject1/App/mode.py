# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    intactionid = models.ForeignKey('CreActions', models.DO_NOTHING, db_column='intActionId')  # Field name made lowercase.
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
