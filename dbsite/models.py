# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Bibliorefer(models.Model):
    organismid = models.IntegerField(db_column='OrganismID')  # Field name made lowercase.
    referencenumber = models.CharField(db_column='ReferenceNumber', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BiblioRefer'
        unique_together = (('organismid', 'referencenumber'),)


class Bibliography(models.Model):
    referencenumber = models.CharField(db_column='ReferenceNumber', primary_key=True, max_length=250)  # Field name made lowercase.
    authors = models.CharField(db_column='Authors', max_length=400, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=450, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=450, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bibliography'


class Comments(models.Model):
    organismid = models.IntegerField(db_column='OrganismID')  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Comments'
        unique_together = (('organismid', 'comments'),)


class Commonname(models.Model):
    organismid = models.IntegerField(db_column='OrganismID')  # Field name made lowercase.
    commonname = models.CharField(db_column='CommonName', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CommonName'
        unique_together = (('organismid', 'commonname'),)


class Distribution(models.Model):
    organismid = models.IntegerField(db_column='OrganismID')  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Distribution'
        unique_together = (('organismid', 'location'),)


class Links(models.Model):
    organismid = models.IntegerField(db_column='OrganismID')  # Field name made lowercase.
    links = models.CharField(db_column='Links', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Links'
        unique_together = (('organismid', 'links'),)


class Master(models.Model):
    organismid = models.AutoField(db_column='OrganismID', primary_key=True)  # Field name made lowercase.
    highertaxa = models.TextField(db_column='HigherTaxa', blank=True, null=True)  # Field name made lowercase.
    genus = models.TextField(db_column='Genus', blank=True, null=True)  # Field name made lowercase.
    species = models.TextField(db_column='Species', blank=True, null=True)  # Field name made lowercase.
    authors = models.TextField(db_column='Authors', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    parantheses = models.TextField(db_column='Parantheses', blank=True, null=True)  # Field name made lowercase.
    synonyms = models.TextField(db_column='Synonyms', blank=True, null=True)  # Field name made lowercase.
    subspecies = models.TextField(db_column='Subspecies', blank=True, null=True)  # Field name made lowercase.
    commonnames = models.TextField(db_column='CommonNames', blank=True, null=True)  # Field name made lowercase.
    location = models.TextField(db_column='Location', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    photourl = models.TextField(db_column='PhotoURL', blank=True, null=True)  # Field name made lowercase.
    referencenumber = models.TextField(db_column='ReferenceNumber', blank=True, null=True)  # Field name made lowercase.
    etymology = models.TextField(db_column='Etymology', blank=True, null=True)  # Field name made lowercase.
    ncbi = models.TextField(db_column='NCBI', blank=True, null=True)  # Field name made lowercase.
    reproduction = models.TextField(db_column='Reproduction', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MASTER'


class Organism(models.Model):
    organismid = models.IntegerField(db_column='OrganismID', primary_key=True)  # Field name made lowercase.
    highertaxa = models.TextField(db_column='HigherTaxa', blank=True, null=True)  # Field name made lowercase.
    genus = models.TextField(db_column='Genus', blank=True, null=True)  # Field name made lowercase.
    species = models.TextField(db_column='Species', blank=True, null=True)  # Field name made lowercase.
    authors = models.TextField(db_column='Authors', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    parantheses = models.TextField(db_column='Parantheses', blank=True, null=True)  # Field name made lowercase.
    etymology = models.TextField(db_column='Etymology', blank=True, null=True)  # Field name made lowercase.
    ncbi = models.TextField(db_column='NCBI', blank=True, null=True)  # Field name made lowercase.
    reproduction = models.TextField(db_column='Reproduction', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Organism'


class SubspeciesName(models.Model):
    organismid = models.IntegerField(db_column='OrganismID')  # Field name made lowercase.
    subspecies_name = models.CharField(db_column='Subspecies_name', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Subspecies_Name'
        unique_together = (('organismid', 'subspecies_name'),)


class Synonym(models.Model):
    organismid = models.CharField(db_column='OrganismID', max_length=11)  # Field name made lowercase.
    synonym_name = models.CharField(db_column='Synonym_Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Synonym'
        unique_together = (('synonym_name', 'organismid'),)


class Types(models.Model):
    organismid = models.CharField(db_column='OrganismID', max_length=11)  # Field name made lowercase.
    types = models.CharField(db_column='Types', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Types'
        unique_together = (('organismid', 'types'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
