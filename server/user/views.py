from django.contrib.auth import authenticate, login

from rest_framework import views, status, generics
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, CreateRequestSerializer, LoginSerializer

class SuggestUniqueUsername(views.APIView):
    def get(self, request, format=None):
        first_name = request.query_params.get('first_name', None)
        if first_name is None:
            return self._missing_param_response('first_name')
        last_name = request.query_params.get('last_name', None)
        if last_name is None:
            return self._missing_param_response('last_name')
        suggest_name = '{0}.{1}'.format(str(first_name).lower(), str(last_name).lower())

        try: 
            User.objects.get(username=suggest_name)
        except User.DoesNotExist:
            return Response(status=200, data={'username': suggest_name})

        names_like = (
            User.objects
                .filter(username__startswith=suggest_name)
                .values_list('username', flat=True)
        )
        max_id = 0
        for name in names_like:
            maybe_id = name[len(suggest_name):]  
            try:
                id = int(maybe_id)
            except ValueError:
                continue
            max_id = max(id, max_id) 
        return Response(status=200, data={'username': suggest_name + str(max_id + 1)})

    def _missing_param_response(self, param_name):
        return Response(
            status=status.HTTP_400_BAD_REQUEST, 
            data="Expected `{0}` in query parameters"
        )

class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateRequestSerializer 

class LoginUser(views.APIView):
    def put(self, request):
        login_serializer = LoginSerializer(data=request.data)
        login_serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=login_serializer.validated_data['username'],
            password=login_serializer.validated_data['password']
        )
        if user is None:
            return Response(data={
                'password': 'Invalid password'
            }, status=403)

        login(request, user)
        user_serializer = UserSerializer(user)
        return Response(data=user_serializer.data, status=200) 

class InitializeContext(views.APIView):
    queryset = User.objects.all()

    def get(self, request):
        if request.user.is_anonymous():
            return Response(status=401, data={})

        serializer = UserSerializer(request.user)
        return Response(status=200, data=serializer.data)







