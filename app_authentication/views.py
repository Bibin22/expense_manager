from django.shortcuts import render
from django.views import View

class RegistrationView(View):
    def get(self, request):
        return render(request, 'app_authentication/register.html')
    