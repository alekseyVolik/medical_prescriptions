from .models import Patient, Doctor, Prescription
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy


class CreatePatient(CreateView):
    model = Patient
    fields = ('first_name', 'last_name', 'father_name', 'phone_number')
    template_name_suffix = '_create'
    success_url = reverse_lazy('index')


class CreateDoctor(CreateView):
    model = Doctor
    fields = ('first_name', 'last_name', 'father_name', 'specialization')
    template_name_suffix = '_create'
    success_url = reverse_lazy('index')


class CreatePrescription(CreateView):
    model = Prescription
    fields = ('description', 'patient', 'doctor', 'validity', 'priority')
    template_name_suffix = '_create'
    success_url = reverse_lazy('index')


class PrescriptionIndex(TemplateView):
    template_name = 'prescriptions/index.html'
