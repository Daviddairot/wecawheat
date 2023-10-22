from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('project/', views.project, name='project'),
    path('service/', views.service, name= 'service'),
    path('testimonial', views.testimonial, name = 'testimonial'),
    path('ourterm/', views.ourterm, name = 'ourterm'),
    path('cart/<int:item_id>/', views.cart, name='cart'),
]









if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)