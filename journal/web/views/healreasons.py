from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

import web.forms as forms
from web.models import HealReasons
from web.views.utils import filter_date_by


@method_decorator(login_required, name="dispatch")
class HealReasonsListView(ListView):
    model = HealReasons
    paginate_by: int = 10
    template_name: str = "common/list.html"

    def get_queryset(self):
        q = super().get_queryset().filter(user=self.request.user).order_by("-created_at")
        if not q:
            return HealReasons.objects.none()
        if search_value := self.request.GET.get("q"):
            q = q.filter(reason__icontains=search_value)
        if not q:
            return HealReasons.objects.none()
        date_to, date_from = filter_date_by(self.request)
        if date_to and date_from:
            q = q.filter(created_at__range=(date_to, date_from))
        return q or None

    def get_paginate_by(self, queryset):
        return self.request.GET.get("show") or self.paginate_by

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allow_date_filter"] = True
        context["page_title"] = "Heal Reasons"
        context["create_url"] = "healreasons_create"
        context["update_url"] = "healreasons_update"
        context["delete_url"] = "healreasons_delete"
        context["columns"] = ["Created at", "Reason"]
        context["object_fields"] = [
            "created_at",
            "reason",
        ]
        return context


@method_decorator(login_required, name="dispatch")
class HealReasonsCreateView(CreateView):
    model = HealReasons
    form_class = forms.HealReasonsForm
    success_url = reverse_lazy("healreasons_list")
    template_name = "common/add.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class HealReasonsUpdateView(UpdateView):
    model = HealReasons
    form_class = forms.HealReasonsForm
    success_url = reverse_lazy("healreasons_list")
    template_name = "common/edit.html"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


@method_decorator(login_required, name="dispatch")
class HealReasonsDeleteView(DeleteView):
    model = HealReasons
    success_url = reverse_lazy("healreasons_list")
    template_name = "common/delete.html"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
