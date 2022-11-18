from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

import web.forms as forms
from web.models import Sport
from web.views.utils import filter_date_by


@method_decorator(login_required, name="dispatch")
class SportListView(ListView):
    model = Sport
    paginate_by: int = 10
    template_name: str = "sport/list.html"

    def get_queryset(self):
        q = super().get_queryset().select_related("sport").filter(user=self.request.user).order_by("-ocurred_at")
        if not q:
            return Sport.objects.none()
        if search_value := self.request.GET.get("q"):
            q = q.filter(sport__name__icontains=search_value)
        if not q:
            return Sport.objects.none()
        date_to, date_from = filter_date_by(self.request)
        if date_to and date_from:
            q = q.filter(ocurred_at__range=(date_to, date_from))
        return q or None

    def get_paginate_by(self, queryset):
        return self.request.GET.get("show") or self.paginate_by

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allow_date_filter"] = True
        context["page_title"] = "Sport"
        context["create_url"] = "sport_create"
        context["update_url"] = "sport_update"
        context["delete_url"] = "sport_delete"
        context["columns"] = ["Ocurred at", "Sport", "Duration (min)"]
        context["object_fields"] = [
            "ocurred_at",
            "sport__name",
            "duration",
        ]
        return context


@method_decorator(login_required, name="dispatch")
class SportCreateView(CreateView):
    model = Sport
    form_class = forms.SportForm
    success_url = reverse_lazy("sport_list")
    template_name = "common/add.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class SportUpdateView(UpdateView):
    model = Sport
    form_class = forms.SportForm
    success_url = reverse_lazy("sport_list")
    template_name = "common/edit.html"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


@method_decorator(login_required, name="dispatch")
class SportDeleteView(DeleteView):
    model = Sport
    success_url = reverse_lazy("sport_list")
    template_name = "common/delete.html"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
