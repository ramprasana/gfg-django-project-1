from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpRequest
from persons_app.models import Person

# Create your views here.
def index_view(request):
    return HttpResponse("<h1>Hello World</h1>")

def person_detail_view(request, person_id):
    try:
        personObj = Person.objects.get(pk=person_id)
    except:
        return JsonResponse({"error": True, "message": "Person does not exist", "status": 404})
    return JsonResponse({
        "id": personObj.id,
        "name": personObj.name,
        "age": personObj.age,
        "status": 200
    })

