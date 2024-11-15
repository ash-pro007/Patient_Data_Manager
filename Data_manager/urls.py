from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('home/signout', views.signout, name='signout'),
    path('home/', views.home, name='home'),
    path('home/home', views.home, name='home'),

    path('register_patient/', views.register_patient, name='register_patient'),
    path('register_patient/patient_details', views.patient_details, name='patient_detials'),
    path('register_patient/home', views.home, name='home'),


    path('patient_details', views.patient_details, name='patient_details'),
    path('home/patient_details', views.patient_details, name='patient_details'),

    path('show_searched_patient', views.show_searched_patient, name='show_searched_patient'),
    path('show_searched_patient_for_remove_patient', views.show_searched_patient_for_remove_patient, name='show_searched_patient_for_remove_patient'),
    path('show_searched_patient_by_due', views.show_searched_patient_by_due, name='show_searched_patient_by_due'),

    path('show_searched_patient_by_date_range', views.show_searched_patient_by_date_range, name='show_searched_patient_by_date_range'),

    path('save_treatment_details', views.save_treatment_details, name='save_treatment_details'),
    path('home/show_searched_patient', views.show_searched_patient, name='show_searched_patient'),
    path('home/show_searched_patient_for_remove_patient', views.show_searched_patient_for_remove_patient, name='show_searched_patient_for_remove_patient'),

    path('remove_patient', views.remove_patient, name='remove_patient'),
    path('home/remove_patient', views.remove_patient, name='remove_patient'),


    path('remove_patient_from_db', views.remove_patient_from_db, name='remove_patient_from_db'),
    path('home/remove_patient_from_db', views.remove_patient_from_db, name='remove_patient_from_db'),

    path('delete_treatment_detail', views.delete_treatment_detail, name='delete_treatment_detail'),

    path('change_patient_details', views.change_patient_details, name='change_patient_details'),

    path('change_treatment_details', views.change_treatment_details, name='change_treatment_details'),

    path('change_treatment_details_in_db', views.change_treatment_details_in_db, name='change_treatment_details_in_db'),

    path('print_receipt', views.print_receipt, name='print_receipt' ),

    path('clear_all_dues', views.clear_all_dues, name='clear_all_dues'),

    path('about', views.about, name='about')
]