from django.shortcuts import render
from .models import Event
# Create your views here.
def events(request):
	context = {'events': Event.objects.all()}
	return render(request, 'events/events.html', context)

def event_detail(request, id):
	context = {'event_details': Event.objects.get(id=id)}
	return render(request, 'events/event_detail.html', context)