from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import UsuarioForm
import requests


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
        elif grupo =='LJ':
            response = request.get('https://raw.githubusercontent.com/uolhost/test-backEnd-Java/master/referencias/liga_da_justica.xml') 
            root = ET.fromstring(response.content)
            codinomes_element = root.find('codinomes')
            codinomes = [codinomes.text for codinomes in codinomes_element.findall('codinome')]

