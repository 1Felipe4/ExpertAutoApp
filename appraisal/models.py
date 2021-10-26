from django.db import models
# A new class is imported. ##
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.deletion import SET_NULL
from django.utils.translation import ugettext as _
from django.core.validators import FileExtensionValidator
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django_countries.fields import CountryField
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('Email Address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year()+10)(value)

class Vehicle(models.Model):
    model = models.CharField(max_length=255)
    year = models.PositiveSmallIntegerField(
        default=current_year(), validators=[MinValueValidator(1900), max_value_current_year], blank=True)
    selling_price = models.DecimalField(_("Selling Price Range"), max_digits= 10, decimal_places=2)
    manufacturer = models.ForeignKey('appraisal.Manufacturer', null= True, on_delete=models.SET_NULL, blank=True)
    engine = models.CharField(_("Engine"), max_length=255, blank=True)
    engine_no = models.CharField(_("Engine #"), max_length=255, blank=True)
    chassis_no = models.CharField(_("Chassis #"), max_length=255, blank=True)
    manufacture_year = models.PositiveSmallIntegerField(
        _("Year of Manufacture"),
        default=current_year(), validators=[MinValueValidator(1900), max_value_current_year], blank=True)
    engine_and_trans = models.CharField(_("Engine and Transmission"), max_length=255, blank=True)
    interior = models.CharField(_("Interior"), max_length=255, blank=True)
    exterior = models.CharField(_("Exterior"), max_length=255, blank=True)
    suspension = models.CharField(_("Suspension"), max_length=255, blank=True)
    safety = models.CharField(_("Safety"), max_length=255, blank=True)
    other_features = models.CharField(_("Other Features"), max_length=255, blank=True)
    pics = models.ManyToManyField("appraisal.Pic", verbose_name=_("Pictures"), blank=True)
    documents = models.ManyToManyField("appraisal.Document", verbose_name=_("Documents"), blank=True)
    
    def __str__(self):
        name = self.model
        if(self.manufacturer):
            name = f'{self.manufacturer} {name}' 
        if(self.manufacture_year):
            name = f'{name} {self.year}'   
        return name  
    
    def get_absolute_url(self):
        return reverse('vehicle_detail', kwargs={'pk': self.pk})

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = CountryField()
    pic = models.ImageField(blank=True, null=True)
    def __str__(self):
            return f'{self.name}'   
    def get_absolute_url(self):
        return reverse('manufacturer_detail', kwargs={'pk': self.pk})

class Pic(models.Model):
    title = models.CharField(_("Image Title"), max_length=50, blank=True, null=True)
    file = models.ImageField(blank=True, null=True)

class Document(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(validators=[
        FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'jpg', 'jpeg', 'png'])], blank=False)
    date_posted = models.DateTimeField(default=timezone.now)


class Note(models.Model):
    text = models.TextField(_("Note"))
    attachment = models.ForeignKey("appraisal.Document", verbose_name=_(""), null= True, on_delete=models.SET_NULL)