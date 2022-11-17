from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from web.models import Measurements
from web.views.utils import filter_date_by
import web.forms as forms


@method_decorator(login_required, name="dispatch")
class MeasurementsListView(ListView):
    model = Measurements
    paginate_by: int = 10
    template_name: str = "common/list.html"

    def get_queryset(self):
        q = super().get_queryset().filter(user=self.request.user).order_by("-created_at")
        if not q:
            return Measurements.objects.none()
        date_to, date_from = filter_date_by(self.request)
        if date_to and date_from:
            q = q.filter(created_at__range=(date_to, date_from))
        return q or Measurements.objects.none()

    def get_paginate_by(self, queryset):
        return self.request.GET.get("show") or self.paginate_by

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allow_date_filter"] = True
        context["page_title"] = "Measurements"
        context["create_url"] = "measurements_create"
        context["update_url"] = "measurements_update"
        context["delete_url"] = "measurements_delete"
        context["columns"] = ["Created at", "Height", "Weight", "BMI", "BMI Evaluation"]
        context["object_fields"] = [
            "created_at",
            "height",
            "weight",
            "bmi",
            "bmi_evaluation",
        ]
        return context


@method_decorator(login_required, name="dispatch")
class MeasurementsCreateView(CreateView):
    model = Measurements
    form_class = forms.MeasurementsForm
    success_url = reverse_lazy("measurements_list")
    template_name = "common/add.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class MeasurementsUpdateView(UpdateView):
    model = Measurements
    form_class = forms.MeasurementsForm
    success_url = reverse_lazy("measurements_list")
    template_name = "common/edit.html"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


@method_decorator(login_required, name="dispatch")
class MeasurementsDeleteView(DeleteView):
    model = Measurements
    success_url = reverse_lazy("measurements_list")
    template_name = "common/delete.html"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
