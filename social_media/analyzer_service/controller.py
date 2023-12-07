from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse

from . import service
from . import validator

@api_view(['POST'])
def create_new_post(request):
    payload = request.data
    headers = request.headers
    user_id = headers.get('X-USER-ID')
    try:
        validator.validate_request_data(payload)
        response = service.create_post(payload, user_id)
        return JsonResponse(response, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)},status=400)


@api_view(['GET'])
def analysis(request, id):
    user_id = request.headers.get('X-USER-ID')
    if not user_id:
       return JsonResponse({"message":"Unauthorized User"}, status=400)

    try:
        resp = service.get_analysis_data(id, user_id)
        return JsonResponse(resp,status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)