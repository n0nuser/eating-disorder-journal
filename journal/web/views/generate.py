from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from web.tests.factories import (
    JournalFactory,
    ThoughtFactory,
    SportTypeFactory,
    SportFactory,
    MeasurementsFactory,
    FoodFactory,
    ForTheBetterLifeFactory,
    HealReasonsFactory,
    ProsConsFactory,
)


@login_required
def generate_fake_data(request):
    for _ in range(10):
        JournalFactory.create(user=request.user)
        ThoughtFactory.create(user=request.user)
        SportTypeFactory.create(user=request.user)
        SportFactory.create(user=request.user)
        MeasurementsFactory.create(user=request.user)
        FoodFactory.create(user=request.user)
        ForTheBetterLifeFactory.create(user=request.user)
        HealReasonsFactory.create(user=request.user)
        ProsConsFactory.create(user=request.user)

    return HttpResponseRedirect(reverse_lazy("home"))
