from django.shortcuts import render


from django.views import View
from django.shortcuts import render
from django.contrib import messages

from .models import Address
import requests


    
class Validate(View):
    template_name = "tools/validate_address.html"
    context = {}
    def get(self, request):
        return render(request, self.template_name,self.context)

    def post(self,request):
        address = request.POST.get("address",None)
        url = "https://blockchain.info/rawaddr/" + address.strip()
        r   = requests.get(url)

        if not address:
            messages.add_message(request, messages.INFO, '%s *有效*' % address)
        if r.status_code == 200:
            messages.add_message(request, messages.INFO, '%s *有效*' % address)
        else:
            messages.add_message(request, messages.INFO, '%s *无效*' % address)
        return render(request, self.template_name,self.context)
