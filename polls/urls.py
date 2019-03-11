from django.urls import path

from . import views

app_name = 'polls'

#urlpatterns = [
#    # ex: /poles/
#    path('', views.index, name='index'),
#    # ex: /poles/5/
#    path('<int:question_id>/', views.detail, name='detail'),
#    # ex: /poles/5/results/
#    path('<int:question_id>/results/', views.results, name='results'),
#    # ex: /poles/5/vote/
#    path('<int:question_id>/vote/', views.vote, name='vote'),
#]

urlpatterns = [
    # ex: /poles/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /poles/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /poles/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /poles/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

