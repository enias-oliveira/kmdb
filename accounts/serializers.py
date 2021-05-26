from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import APIException


class UnauthorizedLogin(APIException):
    status_code = 401
    default_detail = "Unable to log in with provided credentials."
    default_code = "unauthorize"


class CustomAuthTokenSerializer(AuthTokenSerializer):
    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        if username and password:
            user = authenticate(
                request=self.context.get("request"),
                username=username,
                password=password,
            )

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                raise UnauthorizedLogin()
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop("fields", None)

        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "is_superuser",
            "is_staff",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
