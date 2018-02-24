from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.generic import View
import PyOpenWorm as P


# from formtools.wizard.views import SessionWizardView

def Landing(request):
    return render(request, 'pyopenworm/landing.html')


def index(request):
    return render(request, 'pyopenworm/landing.html')


class SearchSuggestion(View):

    Allcells = []

    def __init__(self):
        self.Allcells = []
        for neuron in P.Neuron().load():
            self.Allcells.append(str(neuron.name()))
        for muscle in P.Muscle().load():
            self.Allcells.append(str(muscle.name()))

    def get(self, request, format=None):

        cellname = self.request.GET.get('term', '')
        Suggestion = []
        if cellname is None:
            Suggestion = []
        else:
            Suggestion = filter(lambda k: cellname in k, self.Allcells)

        data = json.dumps(Suggestion)
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)
