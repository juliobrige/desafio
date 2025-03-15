from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import UsuarioForm
import requests
import xml.etree.ElementTree as ET
from .models import Usuario


class cadastro (View):
    template_name = 'cadastro.html'
    form_class = UsuarioForm


    def get(self, request):
        return render (request, self.template_name, {'form': self.form_class()})
    def post (self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            codinome = self._get_codinome(form.cleaned_data['grupo'])
            obj = form.save()
            return HttpResponse('Cadastro realizado com sucesso')

        return render (request, self.template_name, {'form':form})    

    def _get_codinome(self, grupo):
        if grupo == 'V':
            response = requests.get('https://raw.githubusercontent.com/uolhost/test-backEnd-Java/master/referencias/vingadores.json')
            codinomes =[i['codinome']for i in response['vingadores']]
        elif grupo =='LJ':
            response = requests.get('https://raw.githubusercontent.com/uolhost/test-backEnd-Java/master/referencias/liga_da_justica.xml') 
            root = ET.fromstring(response.content)
            codinomes_element = root.find('codinomes')
            codinomes = [codinomes.text for codinome in codinomes_element.findall('codinome')]
 
        codinomes_usados = Usuario.objects.value_list('codinomes', flat=True)