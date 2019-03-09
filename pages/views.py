from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

class DoulaSupportPageView(TemplateView):
    template_name = 'doula_support.html'

class NutritionCoachingPageView(TemplateView):
    template_name = 'nutrition_coaching.html'

class OtherServicesPageView(TemplateView):
    template_name = 'other_services.html'

class TestimonialsPageView(TemplateView):
    template_name = 'testimonials.html'
