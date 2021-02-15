from .models import Patient, Doctor, Prescription
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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


class Patients(ListView):
    model = Patient


class Doctors(ListView):
    model = Doctor


class Prescriptions(ListView):
    model = Prescription


class DetailPatient(DetailView):
    model = Patient


class DetailDoctor(DetailView):
    model = Doctor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctor = context['doctor']
        amount_prescriptions = doctor.prescription_set.count()
        context['amount_prescriptions'] = amount_prescriptions
        return context


class DetailPrescription(DetailView):
    model = Prescription
