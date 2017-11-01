from django.http import JsonResponse


class GeneralResponse(JsonResponse):
    def __init__(self, status=True, payload=None):
        ret = {}
        if status is False:
            ret['status'] = 'error'
        else:
            ret['status'] = 'success'
        ret['payload'] = payload
        JsonResponse.__init__(self, data=ret, safe=False)