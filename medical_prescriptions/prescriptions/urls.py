from django.urls import path

from .views import CreatePatient, CreateDoctor, CreatePrescription


urlpatterns = [
    path('', '', name='index'),
    path('create/patient', '', name='create_patient'),
    path('create/doctor', '', name='create_doctor'),
    path('create/prescription', '', name='create_prescription')
]
