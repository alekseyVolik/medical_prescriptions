from django.urls import path

from .views import CreatePatient, CreateDoctor, CreatePrescription
from .views import PrescriptionIndex


urlpatterns = [
    path('', PrescriptionIndex.as_view(), name='index'),
    path('create/patient', CreatePatient.as_view(), name='create_patient'),
    path('create/doctor', CreateDoctor.as_view(), name='create_doctor'),
    path('create/prescription', CreatePrescription.as_view(), name='create_prescription'),
]
