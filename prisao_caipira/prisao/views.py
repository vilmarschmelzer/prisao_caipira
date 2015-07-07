# coding:utf-8

from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
from django.conf import settings
from .models import Prisioneiro
import json
from django.template.loader import render_to_string

class IndexView(View):

    template_name = 'index.html'

    def render(self, request):
        presos_livres = [(i + 1) for i in range(settings.CAPACIDADE)]

        presos = Prisioneiro.objects.get_presos()
        soltar_presos = Prisioneiro.objects.get_soltar_presos()

        for preso in soltar_presos:
            Prisioneiro.objects.soltar(preso.prisioneiro_id)

        for preso in presos:
            presos_livres.remove(preso.prisioneiro_id)

        return render(request, self.template_name, {'presos_livres': presos_livres, 'presos': presos,'soltar': soltar_presos})

    def get(self, request):
        return self.render(request)


class PrenderView(View):

    template_name = 'index.html'

    def post(self, request):

        if 'prender' not in request.POST or request.POST['prender'] == '':
            json_ = json.dumps({'success': False, 'msg': 'Informe o numero do prisioneiro!'}, ensure_ascii=False)
            return HttpResponse(json_)

        prisioneiro_id = int(request.POST['prender'])

        presos_livres = [(i + 1) for i in range(settings.CAPACIDADE)]

        if prisioneiro_id in presos_livres:

            Prisioneiro.objects.prender(prisioneiro_id)

            presos = Prisioneiro.objects.get_presos()
            soltar_presos = Prisioneiro.objects.get_soltar_presos()

            for preso in soltar_presos:
                Prisioneiro.objects.soltar(preso.prisioneiro_id)

            for preso in presos:
                presos_livres.remove(preso.prisioneiro_id)

            presos_livres_html = render_to_string('presos_livres.html', {'presos_livres': presos_livres})
            soltar_presos_html = render_to_string('presos_soltar.html', {'soltar': soltar_presos})
            tb_presos_html = render_to_string('tb_presos.html', {'presos': presos})

            json_ = json.dumps({'success': True, 'presos_livres_html': unicode(presos_livres_html), 'presos_html': unicode(tb_presos_html),'soltar_presos_html': unicode(soltar_presos_html)}, ensure_ascii=False)
            return HttpResponse(json_)
        else:
            json_ = json.dumps({'success': False, 'msg': 'Prisioneiro inválido'}, ensure_ascii=False)
            return HttpResponse(json_)


class SoltarView(View):

    template_name = 'index.html'

    def post(self, request):

        if 'soltar' not in request.POST or request.POST['soltar'] == '':
            json_ = json.dumps({'success': False, 'msg': 'Informe o numero do prisioneiro!'}, ensure_ascii=False)
            return HttpResponse(json_)

        prisioneiro_id = int(request.POST['soltar'])

        soltar_presos = []
        soltar_prisi = Prisioneiro.objects.soltar(prisioneiro_id)
        if soltar_prisi:
            soltar_presos.append(soltar_prisi)

        presos_livres = [(i + 1) for i in range(settings.CAPACIDADE)]

        presos = Prisioneiro.objects.get_presos()


        for preso in Prisioneiro.objects.get_soltar_presos():
            soltar_presos.append(Prisioneiro.objects.soltar(preso.prisioneiro_id))

        for preso in presos:
            presos_livres.remove(preso.prisioneiro_id)

        presos_livres_html = render_to_string('presos_livres.html', {'presos_livres': presos_livres})
        soltar_presos_html = render_to_string('presos_soltar.html', {'soltar': soltar_presos})
        tb_presos_html = render_to_string('tb_presos.html', {'presos': presos})

        json_ = json.dumps({'success': True, 'presos_livres_html': unicode(presos_livres_html), 'presos_html': unicode(tb_presos_html),'soltar_presos_html': unicode(soltar_presos_html)}, ensure_ascii=False)
        return HttpResponse(json_)


class AtualizarView(View):

    def get(self, request):
        presos_livres = [(i + 1) for i in range(settings.CAPACIDADE)]

        presos = Prisioneiro.objects.get_presos()
        soltar_presos = Prisioneiro.objects.get_soltar_presos()

        for preso in soltar_presos:
            Prisioneiro.objects.soltar(preso.prisioneiro_id)

        for preso in presos:
            presos_livres.remove(preso.prisioneiro_id)

        presos_livres_html = render_to_string('presos_livres.html', {'presos_livres': presos_livres})
        soltar_presos_html = render_to_string('presos_soltar.html', {'soltar': soltar_presos})
        tb_presos_html = render_to_string('tb_presos.html', {'presos': presos})

        json_ = json.dumps({'success': True, 'presos_livres_html': unicode(presos_livres_html), 'presos_html': unicode(tb_presos_html),'soltar_presos_html': unicode(soltar_presos_html)}, ensure_ascii=False)
        return HttpResponse(json_)
