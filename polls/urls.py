from django.urls import path

from . import views

urlpatterns = [
    # path('form/', views.extract_text_form, name='form'),
    path('form/', views.extract_text_from_image, name='extract_text'),
    path('save_text/', views.save_extracted_text, name='save_text'),
    path('text_saved/', views.text_saved, name='text_saved'),
]