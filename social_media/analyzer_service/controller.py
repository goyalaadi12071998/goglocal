import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

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
        breakpoint()
        return Response(json.dumps(response.__dict__))
    except Exception as e:
        return Response(status_code=400)


@api_view(['GET'])
def analysis(request):
    post_id = request.params
    user_id = request.headers.get('X-USER-ID')

    if not user_id:
        Response(status_code=400, data='Unauthorized User')

    try:
        service