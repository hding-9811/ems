from rest_framework import exceptions
from rest_framework.serializers import ModelSerializer
from index.models import User, Employee


class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        extra_kwargs = {
            "username": {
                "required": True,
                "min_length": 1,

                "error_messages": {
                    "required": "用户名不能为空",
                    "min_length": "用户名长度的不够",

                }
            }
        }

    def validate(self, attrs):
        username = attrs.get("username")
        user = User.objects.filter(username=username).first()
        if user:
            raise exceptions.ValidationError("用户名已存在")
        return attrs


class EmpolyeeModelSerializers(ModelSerializer):
    class Meta:
        model = Employee
        fields = ("emp_name","img","salary","age","img_name","id")
        extra_kwargs = {
            "username": {
                "required": True,
                "min_length": 1,

                "error_messages": {
                    "required": "用户名不能为空",
                    "min_length": "用户名长度的不够",
                }
            }
        }
