from django.http.response import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from appraisal.models import Manufacturer, Vehicle
from .forms import AttachmentPicForm, ManufacturerForm, UserRegisterForm, VehicleBasicFilterForm, VehicleForm
from django.contrib import messages
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
    )
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

# Create your views here.
def home(request):
    return redirect('dashboard')

def dashboard(request):
    form = VehicleBasicFilterForm()
    return render(request, 'appraisal/dashboard.html', {'form':form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            messages.success(request, f'Account Created for {username}!')
            return redirect("my-profile-detail")
    else:
        form = UserRegisterForm()
    
    
    return render(request, 'accounts/register.html', {'form':form})

class VehicleCreateView(LoginRequiredMixin, CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = "vehicle/vehicle-form.html"

class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicle
    form_class = VehicleForm    
    template_name = "vehicle/vehicle-form.html"

class VehicleDetailView(LoginRequiredMixin, DetailView):
    model = Vehicle
    template_name = "vehicle/vehicle-detail.html"

class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = "vehicle/vehicles.html"

class VehicleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Vehicle
    permission_required = 'vehicle.delete_document' 
    template_name = "vehicle/vehicle-delete.html"

    def get_success_url(self):
        return reverse('vehicle_list')

class ManufacturerDetailView(LoginRequiredMixin, DetailView):
    model = Manufacturer
    template_name = "manufacturer/manufacturer-detail.html"

class ManufacturerCreateView(LoginRequiredMixin, CreateView):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = 'manufacturer/manufacturer-form.html'

class ManufacturerUpdateView(LoginRequiredMixin, UpdateView):
    model = Manufacturer
    form_class = ManufacturerForm    
    template_name = 'manufacturer/manufacturer-form.html'

class ManufacturerListView(LoginRequiredMixin, ListView):
    model = Manufacturer
    template_name = "manufacturer/manufacturers.html"
    
class ManufacturerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Manufacturer
    permission_required = 'manufacturer.delete_document' 
    template_name = "manufacturer/manufacturer-delete.html"
    
    def get_success_url(self):
        return reverse('manufacturer_list')


def add_manufacturer(request):
    if request.method == 'POST':
        form = ManufacturerForm(request.POST)
        pic_form = AttachmentPicForm(request.POST, request.FILES)
        if form.is_valid():
            if(pic_form.is_valid()):
                manu = form.save(commit=False)
                pic = pic_form.save(commit=False)
                pic.title = manu.name + " Brand Image"
                pic.save()
                pic_form.save_m2m()
                manu.pic = pic
                manu.save()
                form.save_m2m()
                return redirect("dashboard")
    else:
        form = ManufacturerForm()
        pic_form = AttachmentPicForm()
    
    return render(request, 'manufacturer/manufacturer-form.html', {'form':form, 'pic_form':pic_form})

def edit_manufacturer(request,pk):
    try:
        manu = get_object_or_404(Manufacturer, pk=pk)     
        if request.method == 'POST':
            form = ManufacturerForm(request.POST, instance=manu)
            if(manu.pic):
                pic_form = AttachmentPicForm(request.POST, request.FILES, instance=manu.pic)
            else:
                pic_form = AttachmentPicForm(request.POST, request.FILES)
            if form.is_valid():
                if(pic_form.is_valid()):
                    manu = form.save()
                    pic = pic_form.save()
                    if(not manu.pic):
                        manu.pic = pic
                        manu.save()
                    return redirect("dashboard")
        else:
            form = ManufacturerForm(instance=manu)
            pic_form = AttachmentPicForm(instance=manu.pic)

    except Manufacturer.DoesNotExist:
        raise Http404("User does not exist")



    return render(request, 'manufacturer/manufacturer-form.html', {'object':manu, 'form':form, 'pic_form':pic_form})


def filter_vehicles(request):
    object_list = Vehicle.objects.all()
    if request.method == 'GET':
        form = VehicleBasicFilterForm(request.GET)
        if form.is_valid():
            manufacturer = form.cleaned_data.get('manufacturer')
            chassis_no = form.cleaned_data.get('chassis_no')
            model = form.cleaned_data.get('model')
            if(manufacturer):
                object_list = object_list.filter(manufacturer__pk=manufacturer)
            if(chassis_no):
                object_list = object_list.filter(chassis_no__contains=chassis_no)
            if(model):
                object_list = object_list.filter(model__contains=model)


    else:
        form = VehicleBasicFilterForm()
    
    return render(request, 'vehicle/vehicles.html', {'form':form, 'object_list': object_list})