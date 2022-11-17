from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

import web.forms as forms
from web.models import ProsCons
from web.views.utils import filter_date_by


@method_decorator(login_required, name="dispatch")
class ProsConsListView(ListView):
    model = ProsCons
    paginate_by: int = 10
    template_name: str = "common/list.html"

    def get_queryset(self):
        q = super().get_queryset().filter(user=self.request.user).order_by("-created_at")
        if not q:
            return ProsCons.objects.none()
        if search_value := self.request.GET.get("q"):
            q = q.filter(text__icontains=search_value)
        if not q:
            return ProsCons.objects.none()
        date_to, date_from = filter_date_by(self.request)
        if date_to and date_from:
            q = q.filter(created_at__range=(date_to, date_from))
        return q or None

    def get_paginate_by(self, queryset):
        return self.request.GET.get("show") or self.paginate_by

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allow_date_filter"] = True
        context["page_title"] = "Pros - Cons"
        context["create_url"] = "proscons_create"
        context["update_url"] = "proscons_update"
        context["delete_url"] = "proscons_delete"
        context["columns"] = ["Created at", "Type", "Text"]
        context["object_fields"] = [
            "created_at",
            "type",
            "text",
        ]
        return context


@method_decorator(login_required, name="dispatch")
class ProsConsCreateView(CreateView):
    model = ProsCons
    form_class = forms.ProsConsForm
    success_url = reverse_lazy("proscons_list")
    template_name = "common/add.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class ProsConsUpdateView(UpdateView):
    model = ProsCons
    form_class = forms.ProsConsForm
    success_url = reverse_lazy("proscons_list")
    template_name = "common/edit.html"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


@method_decorator(login_required, name="dispatch")
class ProsConsDeleteView(DeleteView):
    model = ProsCons
    success_url = reverse_lazy("proscons_list")
    template_name = "common/delete.html"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
