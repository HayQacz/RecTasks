from django.shortcuts import render

from .forms import PeselForm
from .utils import get_pesel_info

def validate_pesel_view(request):
    context = {
        'form': PeselForm(),
        'is_valid': None,
        'info': None
    }

    if request.method == 'POST':
        form = PeselForm(request.POST)

        if form.is_valid():
            pesel = form.cleaned_data.get('pesel')

            info = get_pesel_info(pesel)

            context['is_valid'] = True
            context['info'] = info
        else:
            context['is_valid'] = False

        context['form'] = form

    return render(request, 'peselVal/validate.html', context)
