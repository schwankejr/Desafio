from logging import exception
from user.models import Usuario


class UserService:
    @staticmethod
    def create(cpf_cnpj, nome_completo, data_nascimento):
        try:
            user = Usuario.objects.create(
                cpf_cnpj= cpf_cnpj,
                nome_completo = nome_completo,
                data_nascimento = data_nascimento,
            )
            user.save()
            return user
        except Exception as ex:
            raise ex    
    @staticmethod
    def update(cpf_cnpj, nome_completo, data_nascimento):
        try:
            user = Usuario.objects.filter(id=id)
            user.update(
                cpf_cnpj = cpf_cnpj,
                nome_completo = nome_completo,
                data_nascimento = data_nascimento
            )
            user.save()
            return user
        except Exception as ex:
            raise ex   
    @staticmethod
    def delete(id):
        try:
            user = Usuario.objects.filter(id=id).first()
            user.delete()
            return str(f'usuario com ID {id} Deletado')
        except Exception as ex:
            raise ex    
    @staticmethod
    def get_usuario(id):
        try:
            usuario = Usuario.objects.filter(id=id).first()
            if usuario:
                return usuario
            raise Exception ("user not found")
        except Exception as ex:
            raise ex
    @staticmethod
    def get_all_usuarios():
        try:
            return Usuario.objects.all()
        except Exception as ex:
            raise ex            