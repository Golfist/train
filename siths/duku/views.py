from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Weapon, Cruiser
from django.views import generic
from django.utils import timezone



class KenobyView(generic.ListView):
    template_name = 'duku/index.html'
    context_object_name = 'armada'

    def get_queryset(self):
        return Cruiser.objects.filter(
        build_date__lte=timezone.now()
    ).order_by('-build_date')[:5]

class FlagshipView(generic.DetailView):
    model = Cruiser
    template_name = 'duku/detail.html'

class StatusView(generic.DetailView):
    model = Cruiser
    template_name = 'duku/results.html'

def instructions(request, cruiser_id):
    cruiser = get_object_or_404(Cruiser, pk=cruiser_id)
    try:
        selected_weapon = cruiser.weapon_set.get(pk=request.POST['weapon'])
    except (KeyError, Weapon.DoesNotExist):
        return render(request, 'duku/detail.html', {
            'cruiser': cruiser,
            'error_message': "You didn't select a weapon.",
        })
    else:
        selected_weapon.shot += 1
        selected_weapon.save()
        return HttpResponseRedirect(reverse('duku:status', args=(cruiser.id,)))

