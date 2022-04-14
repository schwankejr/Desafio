import email        
from rest_framework.views import APIView
from ..service import UserService
from rest_framework.response import Response
from ..models import Usuario, User
from .serializers import UsuarioSerializer


class GetUsuario(APIView):
    def get(self, request,  id):
        try:
            response = UserService.get_usuario(id)
            return Response(response, 200)
        except Exception as ex:
            return Response({'erro': str(ex)}, 400)


class RegisterUsuario(APIView):
    def post(self, request):
        try:
            usuario  = Usuario.objects.create(
                email = request.data.get('email'),
                password = request.data.get('password'),
                cpf_cnpj= request.data.get('cpf_cnpj'),
                nome_completo = request.data.get('nome_completo'),
                data_nascimento = request.data.get('data_nascimento'),
            )
            

            user_model = User.objects.create(

                username = usuario.cpf_cnpj 
            )

            user_model.save()

            usuario.user.system = user_model
            usuario.save()

            return Response(UsuarioSerializer(usuario).data, 200)

        except Exception as ex:
            return Response({'error': str(ex)}, 400)        