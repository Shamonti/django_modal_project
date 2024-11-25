from django.shortcuts import render
from django.http import JsonResponse
from .models import Person
import json

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

def table(request):
    people = Person.objects.all()
    return render(request, 'modal.html', {'people': people})