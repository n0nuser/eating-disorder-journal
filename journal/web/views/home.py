from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from web.models import Journal, Thought, Sport, Measurements, Food, ForTheBetterLife, HealReasons, ProsCons

def get_first(queryset, user):
    return queryset.filter(user=user).order_by("-ocurred_at").first().ocurred_at

@method_decorator(login_required, name="dispatch")
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dates"] = {
            "journal": get_first(Journal.objects, self.request.user)
            if Journal.objects.filter(user=self.request.user).exists()
            else None,
            "thought": get_first(Thought.objects, self.request.user)
            if Thought.objects.filter(user=self.request.user).exists()
            else None,
            "sport": get_first(Sport.objects, self.request.user)
            if Sport.objects.filter(user=self.request.user).exists()
            else None,
            "measurements": get_first(Measurements.objects, self.request.user)
            if Measurements.objects.filter(user=self.request.user).exists()
            else None,
            "food": get_first(Food.objects, self.request.user)
            if Food.objects.filter(user=self.request.user).exists()
            else None,
        }
        return context
