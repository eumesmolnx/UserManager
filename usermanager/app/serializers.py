from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import re

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['cpf'] = user.cpf
        return token

class UserSerializer(serializers.HyperlinkedModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    def validate(self,data):
        roles = ('ADMIN','COMMON')
        #t = (10, 4, 5, 6, 8); n=6
        x=[i for i in roles if i==data['role']]
        if not x:
            raise serializers.ValidationError('The role is not valid.')
        
        # validar CPF
        entrada = re.findall("\d", data['cpf'])
        
        if len(data['cpf']) > 14 or len(entrada) < 11 or len(entrada) > 11:
            print('CPF INVÁLIDO')
        else:
            valid = 0
            for dig in range(0, 11):
                valid += int(entrada[dig])
                dig += 1
            if int(entrada[0]) == valid / 11:
                print("CPF INVÁLIDO")
            else:
                # verificação do 10º dígito verificador
                soma = 0
                count = 10
                for i in range(0, len(entrada)-2):
                    soma = soma + (int(entrada[i])*count)
                    i+=1
                    count-=1
                dg1 = 11-(soma%11)
                if dg1 >= 10:
                    dg1 = 0
                # verificação do 11º dígito verificador
                soma = 0
                count = 10
                for j in range(1, len(entrada)-1):
                    soma = soma + (int(entrada[j])*count)
                    j+=1
                    count-=1
                dg2 = 11-(soma%11)
                if dg2 >= 10:
                    dg2 = 0
                # mensagem ao usuário
                if int(entrada[9]) != dg1 or int(entrada[10]) != dg2:
                    raise serializers.ValidationError('CPF is invalid')

        return data

    class Meta:
        model = User
        fields = ('id','name','cpf','password','role')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        instance.password = make_password(validated_data.get('password',instance.password))
        instance.save()
        return instance