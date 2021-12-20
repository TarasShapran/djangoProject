from rest_framework.response import Response
from rest_framework.views import APIView


class MyVie(APIView):
    def get(self, *args, **kwargs):
        params = self.request.query_params
        print(params)
        return Response({'msg': 'Hello from GET'})

    def post(self, *args, **kwargs):
        data = self.request.data
        print(data)
        return Response({'msg': 'Hello from POST'})

    def put(self, *args, **kwargs):
        return Response({'msg': 'Hello from PUT'})

    def putch(self, *args, **kwargs):
        return Response({'msg': 'Hello from PUTCH'})

    def delete(self, *args, **kwargs):
        return Response({'msg': 'Hello from DELETE'})
