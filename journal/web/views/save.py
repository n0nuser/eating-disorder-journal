from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from web.models import Journal, Thought, Sport, Measurements, Food, ForTheBetterLife, HealReasons, ProsCons
from web.views.utils import CSV, PDF


@method_decorator(login_required, name="dispatch")
class SaveView(TemplateView):
    template_name = "save/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["journal"] = Journal.objects.exists()
        context["thought"] = Thought.objects.exists()
        context["sport"] = Sport.objects.exists()
        context["measurements"] = Measurements.objects.exists()
        context["food"] = Food.objects.exists()
        context["forthebetterlife"] = ForTheBetterLife.objects.exists()
        context["healreasons"] = HealReasons.objects.exists()
        context["proscons"] = ProsCons.objects.exists()
        return context

@login_required
def JournalCSV(request):
    fields = ["id", "ocurred_at", "number_of_times", "situation_emotion", "afterwards_feeling"]
    return CSV("journal", fields, 1, True, Journal, request.user)


@login_required
def JournalPDF(request):
    fields = ["id", "ocurred_at", "number_of_times", "situation_emotion", "afterwards_feeling"]
    return PDF("journal", fields, 1, True, Journal, request.user, "journal/report-pdf.html")

#######################################################################################################################

@login_required
def ThoughtCSV(request):
    fields = ["id", "ocurred_at", "journal", "thought"]
    return CSV("thought", fields, 1, True, Thought, request.user)


@login_required
def ThoughtPDF(request):
    fields = ["id", "ocurred_at", "journal", "thought"]
    return PDF("thought", fields, 1, True, Thought, request.user, "thought/report-pdf.html")

#######################################################################################################################

@login_required
def SportCSV(request):
    fields = ["id", "ocurred_at", "sport__name", "duration"]
    return CSV("sport", fields, 1, True, Sport, request.user)


@login_required
def SportPDF(request):
    fields = ["id", "ocurred_at", "sport__name", "duration"]
    return PDF("sport", fields, 1, True, Sport, request.user, "sport/report-pdf.html")

#######################################################################################################################

@login_required
def MeasurementsCSV(request):
    fields = ["id", "ocurred_at", "weight", "height"]
    return CSV("measurements", fields, 1, True, Measurements, request.user)


@login_required
def MeasurementsPDF(request):
    fields = ["id", "ocurred_at", "weight", "height"]
    return PDF("measurements", fields, 1, True, Measurements, request.user, "measurements/report-pdf.html")

#######################################################################################################################

@login_required
def FoodCSV(request):
    fields = ["id", "ocurred_at", "meal", "food", "amount"]
    return CSV("food", fields, 1, True, Food, request.user)


@login_required
def FoodPDF(request):
    fields = ["id", "ocurred_at", "meal", "food", "amount"]
    return PDF("food", fields, 1, True, Food, request.user, "food/report-pdf.html")

#######################################################################################################################

@login_required
def HealReasonsCSV(request):
    fields = ["id", "reason"]
    return CSV("healreasons", fields, 1, False, HealReasons, request.user)


@login_required
def HealReasonsPDF(request):
    fields = ["id", "reason"]
    return PDF("healreasons", fields, 1, False, HealReasons, request.user, "healreasons/report-pdf.html")

#######################################################################################################################

@login_required
def ProsConsCSV(request):
    fields = ["id", "type", "text"]
    return CSV("proscons", fields, 1, False, ProsCons, request.user)


@login_required
def ProsConsPDF(request):
    fields = ["id", "type", "text"]
    return PDF("proscons", fields, 1, False, ProsCons, request.user, "proscons/report-pdf.html")

#######################################################################################################################

@login_required
def ForTheBetterLifeCSV(request):
    fields = ["id", "text"]
    return CSV("forthebetterlife", fields, 1, False, ForTheBetterLife, request.user)


@login_required
def ForTheBetterLifePDF(request):
    fields = ["id", "text"]
    return PDF("forthebetterlife", fields, 1, False, ForTheBetterLife, request.user, "forthebetterlife/report-pdf.html")

