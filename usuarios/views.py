from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import UsuarioForm
import requests
import xml.etree.ElementTree as ET
from .models import Usuario
from django.contrib import messages


class cadastro(View):
    template_name = 'cadastro.html'
    form_class = UsuarioForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            codinome = self._get_codinome(form.cleaned_data['grupo'])
            if codinome:
                obj = form.save(commit=False)
                obj.codinome = codinome
                obj.save()
                return render(request, 'cadastro_realizado.html')
            else:
                return HttpResponse('Não há codinomes disponíveis para o grupo selecionado.')

        return render(request, self.template_name, {'form': form})

    def _get_codinome(self, grupo):
        if grupo == 'V':
            response = requests.get('https://raw.githubusercontent.com/uolhost/test-backEnd-Java/master/referencias/vingadores.json')
            data = response.json()
            codinomes = [i['codinome'] for i in data['vingadores']]
        elif grupo == 'LJ':
            response = requests.get('https://raw.githubusercontent.com/uolhost/test-backEnd-Java/master/referencias/liga_da_justica.xml')
            root = ET.fromstring(response.content)
            codinomes_element = root.find('codinomes')
            codinomes = [codinome.text for codinome in codinomes_element.findall('codinome')]
        else:
            return None
        codinomes_usados = Usuario.objects.values_list('codinome', flat=True)
        codinomes_disponiveis = set(codinomes) - set(codinomes_usados)

        if not codinomes_disponiveis:
            return None

        return list(codinomes_disponiveis)[0]