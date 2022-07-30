from django.http import HttpResponse

from education.serializers import *
from education.models import School
import json


def schools(request):
    if request.method == 'GET':
        return HttpResponse(json.dumps([
            {
                "id":school.id,
                "address":school.address,
                "name":school.name
            } for school in School.objects.all()
        ]))
    if request.method == 'POST':
        # Нужно извлечь параметы из тела запроса
        json_params = json.loads(request.body)

        school = School.objects.create(
            name=json_params['name'],
            address=json_params['address']
        )
        return HttpResponse(json.dumps({
            "id":school.id,
            "name":school.name,
            "school":school.name
        }))


def school_id(request, school_id):
    school = School.objects.get(id=school_id)
    if request.method == 'GET':
        return HttpResponse(json.dumps(
             {
                "id":school.id,
                "address":school.address,
                "name":school.name
            }))
    json_params = json.loads(request.body)
    if request.method == 'PUT':
        school.address = json_params['address']
        school.name = json_params['name']
        school.save()
        return HttpResponse(json.dumps({
            "id":school.id,
            "name":school.name,
            "school":school.name
        }))
    if request.method == 'PATCH':
        school.address = json_params.get('address',school.address)
        school.name = json_params.get('name',school.name)
        school.save()
        return HttpResponse(json.dumps({
            "id":school.id,
            "name":school.name,
            "school":school.name
        }))
    if request.method == 'DELETE':
        school.delete();
        return HttpResponse(json.dumps({}))
