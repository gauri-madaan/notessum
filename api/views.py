from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializers import NoteSerializer, SummarySerializer
from .models import Note, Summary
from .nlp import sentences


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/getnotes/',
            'method': ["GET"],
            'body': None,
            'description': 'Returns all notes in the database'
        },
        {
            'Endpoint': '/getnote/id',
            'method': ["GET"],
            'body': None,
            'description': 'Returns the note associated with the id'
        }
        ]

    return Response(routes)

# get all
@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSummaries(request):
    summary = Summary.objects.all()
    serializer = SummarySerializer(summary, many=True)
    return Response(serializer.data)

# get last
@api_view(['GET'])
def lastNote(request):
    last_note = Note.objects.latest('created')
    serializer = NoteSerializer(last_note, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def lastSummary(request):
    last_note = Note.objects.latest('created')
    last_summary = last_note.summary
    serializer = SummarySerializer(last_summary, many=False)
    return Response(serializer.data)

# get specific
@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getSummary(request, pk):
    note = Note.objects.get(id=pk)
    summary = note.summary
    serializer = SummarySerializer(summary, many=False)
    return Response(serializer.data)

# create
@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(body=data['body'])
    summary = note.summary
    serializer = SummarySerializer(summary, many=False)
    return Response(serializer.data)

# @api_view(['GET'])
# def test(request, pk):
#     note = Note.objects.get(id=pk)
#     sent = sentences(note=note.body)
#     return Response(note.body)