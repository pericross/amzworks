# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.storage import default_storage

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.views.generic   import TemplateView

from .forms import ContactForm, FilesForm, ContactFormSet


# http://yuji.wordpress.com/2013/01/30/django-form-field-in-initial-data-requires-a-fieldfile-instance/
class FakeField(object):
    storage = default_storage


fieldfile = FieldFile(None, FakeField, "dummy.txt")


class HomePageView(TemplateView):
    template_name = "app/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        messages.info(self.request, "hello http://example.com")
        return context


class DefaultFormsetView(FormView):
    template_name = "app/formset.html"
    form_class = ContactFormSet


class DefaultFormView(FormView):
    template_name = "app/forms.html"
    form_class = ContactForm


class DefaultFormByFieldView(FormView):
    template_name = "app/form_by_field.html"
    form_class = ContactForm


class FormHorizontalView(FormView):
    template_name = "app/form_horizontal.html"
    form_class = ContactForm


class FormInlineView(FormView):
    template_name = "app/form_inline.html"
    form_class = ContactForm


class FormValidationView(FormView):
    template_name = "app/form_validation.html"
    form_class = ContactForm


class FormEditorView(FormView):
    template_name = "app/form_editor.html"
    form_class = ContactForm


class FormWizardsView(FormView):
    template_name = "app/form_wizards.html"
    form_class = ContactForm


class FormUIElementsView(FormView):
    template_name = "app/ui_elements.html"
    form_class = ContactForm


class FormTableStaticView(FormView):
    template_name = "app/table_static.html"
    form_class = ContactForm


class FormTableDynamicView(FormView):
    template_name = "app/table_dynamic.html"
    form_class = ContactForm


class FormTableSortableResizableView(FormView):
    template_name = "app/table_sortable_resizable.html"
    form_class = ContactForm


class FormWidgetsView(FormView):
    template_name = "app/widgets.html"
    form_class = ContactForm


class Page403View(FormView):
    template_name = "app/403.html"
    form_class = ContactForm


class Page404View(FormView):
    template_name = "app/404.html"
    form_class = ContactForm


class Page405View(FormView):
    template_name = "app/405.html"
    form_class = ContactForm


class Page500View(FormView):
    template_name = "app/500.html"
    form_class = ContactForm


class Page503View(FormView):
    template_name = "app/503.html"
    form_class = ContactForm


class LoginView(FormView):
    template_name = "app/login.html"
    form_class = ContactForm


class OfflineView(FormView):
    template_name = "app/offline.html"
    form_class = ContactForm


class FileManagerView(FormView):
    template_name = "app/file_manager.html"
    form_class = ContactForm


class TypographyView(FormView):
    template_name = "app/typography.html"
    form_class = ContactForm


class CalendarView(FormView):
    template_name = "app/calendar.html"
    form_class = ContactForm


class GalleryView(FormView):
    template_name = "app/gallery.html"
    form_class = ContactForm


def chartsview(request):
    return render(request, "app/charts.html")


class FormWithFilesView(FormView):
    template_name = "app/form_with_files.html"
    form_class = FilesForm

    def get_context_data(self, **kwargs):
        context = super(FormWithFilesView, self).get_context_data(**kwargs)
        context["layout"] = self.request.GET.get("layout", "vertical")
        return context

    def get_initial(self):
        return {"file4": fieldfile}


class PaginationView(TemplateView):
    template_name = "app/pagination.html"

    def get_context_data(self, **kwargs):
        context = super(PaginationView, self).get_context_data(**kwargs)
        lines = []
        for i in range(200):
            lines.append("Line %s" % (i + 1))
        paginator = Paginator(lines, 10)
        page = self.request.GET.get("page")
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            show_lines = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            show_lines = paginator.page(paginator.num_pages)
        context["lines"] = show_lines
        return context


class MiscView(TemplateView):
    template_name = "app/misc.html"


class GridView(TemplateView):
    template_name = "app/grid.html"
