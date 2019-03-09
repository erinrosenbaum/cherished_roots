from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
    path('doula_support/', views.DoulaSupportPageView.as_view(), name='doula_support'),
    path('nutrition_coaching/', views.NutritionCoachingPageView.as_view(), name='nutrition_coaching'),
    path('other_services/', views.OtherServicesPageView.as_view(), name='other_services'),
    path('testimonials/', views.TestimonialsPageView.as_view(), name='testimonials'),
]
