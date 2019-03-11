# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from app import views

from .views import (
    HomePageView,
    FormHorizontalView,
    FormInlineView,
    PaginationView,
    FormWithFilesView,
    DefaultFormView,
    MiscView,
    DefaultFormsetView,
    DefaultFormByFieldView,
    FormValidationView,
    GridView,
    FormEditorView,
    FormWizardsView,
    FormUIElementsView,
    FormTableSortableResizableView,
    FormTableDynamicView,
    FormTableStaticView, FormWidgetsView, Page403View, Page404View, Page405View, Page500View, Page503View, LoginView,
    OfflineView, FileManagerView, TypographyView, CalendarView, GalleryView)

urlpatterns = [
    url(r"^$", HomePageView.as_view(), name="home"),
    url(r"^formset$", DefaultFormsetView.as_view(), name="formset_default"),
    url(r"^form$", DefaultFormView.as_view(), name="form_default"),
    url(r"^form_by_field$", DefaultFormByFieldView.as_view(), name="form_by_field"),
    url(r"^form_horizontal$", FormHorizontalView.as_view(), name="form_horizontal"),
    url(r"^form_inline$", FormInlineView.as_view(), name="form_inline"),
    url(r"^form_with_files$", FormWithFilesView.as_view(), name="form_with_files"),
    url(r"^pagination$", PaginationView.as_view(), name="pagination"),
    url(r"^misc$", MiscView.as_view(), name="misc"),
    url(r'^form_validation', FormValidationView.as_view(), name='form_validation'),
    url(r'^charts$', views.chartsview, name='charts'),
    url(r'^grid$', GridView.as_view(), name='grid'),
    url(r'^widgets$', FormWidgetsView.as_view(), name='widgets'),
    url(r'^form_editor$', FormEditorView.as_view(), name='form_editor'),
    url(r'^form_wizards$', FormWizardsView.as_view(), name='form_wizards'),
    url(r'^ui_elements$', FormUIElementsView.as_view(), name='ui_elements'),
    url(r'^table_static$', FormTableStaticView.as_view(), name='table_static'),
    url(r'^table_dynamic$', FormTableDynamicView.as_view(), name='table_dynamic'),
    url(r'^table_sortable_resizable$', FormTableSortableResizableView.as_view(), name='table_sortable_resizable'),
    url(r'^403$', Page403View.as_view(), name='403'),
    url(r'^404$', Page404View.as_view(), name='404'),
    url(r'^4035', Page405View.as_view(), name='405'),
    url(r'^500$', Page500View.as_view(), name='500'),
    url(r'^503$', Page503View.as_view(), name='503'),
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^offline$', OfflineView.as_view(), name='offline'),
    url(r'^file_manager$', FileManagerView.as_view(), name='file_manager'),
    url(r'^typography$', TypographyView.as_view(), name='typography'),
    url(r'^calendar$', CalendarView.as_view(), name='calendar'),
    url(r'^gallery$', GalleryView.as_view(), name='gallery'),
]
