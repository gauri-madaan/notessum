from django.urls import path
from .views import createNote, getNote, getNotes, getRoutes, getSummary, lastNote, lastSummary, getSummaries

urlpatterns = [
    path('', getRoutes, name="getRoutes"),
    path('getnotes/', getNotes, name="getNotes"),
    path('getsummaries/', getSummaries, name="getSummaries"),
    path('lastnote/', lastNote, name="lastNote"),
    path('lastsummary/', lastSummary, name="lastSummary"),
    path('getnote/<str:pk>', getNote, name="getNote"),
    path('getsummary/<str:pk>', getSummary, name="getSummary"),
    path('createnote/', createNote, name="createNote"),
    # path('test/<str:pk>', test, name="test"),
]