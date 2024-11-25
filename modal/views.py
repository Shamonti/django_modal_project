from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Person
import json

@csrf_exempt
def update_row_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        person_id = data.get('id')
        name = data.get('name')
        age = data.get('age')

        try:
            person = Person.objects.get(id=person_id)
            person.name = name
            person.age = age
            person.save()

            return JsonResponse({'success': True, 'message': 'Row updated successfully'})
        except Person.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Person not found'})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})

def get_table_data(request):
    persons = Person.objects.all()
    data = list(persons.values('id', 'name', 'age'))  # Serialize data for JSON response
    return JsonResponse({'data': data})

def table(request):
    people = Person.objects.all()
    return render(request, 'modal.html', {'people': people})