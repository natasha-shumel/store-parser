from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='selections'),
    path('view/<int:selection_id>', views.view_selection, name='view_selection'),
    path('parse', views.parse, name='parse'),
    # path('', views.add_record, name='add_record'),
]