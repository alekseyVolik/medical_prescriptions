from django.urls import path

from .views import CreatePatient, CreateDoctor, CreatePrescription
from .views import Patients, Doctors, Prescriptions
from .views import PrescriptionIndex
from .views import DetailPatient, DetailDoctor, DetailPrescription


urlpatterns = [
    path('', PrescriptionIndex.as_view(), name='index'),
    path('create/patient', CreatePatient.as_view(), name='create_patient'),
    path('create/doctor', CreateDoctor.as_view(), name='create_doctor'),
    path('create/prescription', CreatePrescription.as_view(), name='create_prescription'),
    path('show/patients', Patients.as_view(), name='show_patients'),
    path('show/doctors', Doctors.as_view(), name='show_doctors'),
    path('show/prescriptions', Prescriptions.as_view(), name='show_prescriptions'),
    path('detail/patient/<int:pk>/', DetailPatient.as_view(), name='detail_patient'),
    path('detail/doctor/<int:pk>/', DetailDoctor.as_view(), name='detail_doctor'),
    path('detail/prescription/<int:pk>/', DetailPrescription.as_view(), name='detail_doctor'),
]
