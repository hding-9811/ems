from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, RetrieveModelMixin
from rest_framework.views import APIView

from index.models import User, Employee
from utils.response import APIResponse
from index.serializers import UserSerializers, EmpolyeeModelSerializers


class UserAPIView(APIView):

    def post(self, request, *args, **kwargs):
        """
        前端注册逻辑处理
        :param request: 前端发送的注册信息
        :param args:
        :param kwargs:
        :return:
        """

        serializer = UserSerializers(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return APIResponse(200, True, "注册成功")

    def get(self, request, *args, **kwargs):
        username = request.query_params.get("username")
        password = request.query_params.get('password')
        user = User.objects.filter(username=username, password=password).first()

        if user:
            return APIResponse(200, True, results=UserSerializers(user).data)

        return APIResponse(400, False)


class EmployeeAPIView(ListModelMixin, GenericAPIView, CreateModelMixin, DestroyModelMixin, RetrieveModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmpolyeeModelSerializers
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        if "id" in kwargs:
            user = self.retrieve(request, *args, **kwargs)
            return APIResponse(200, True, results=user.data)
        else:

            user = self.list(request, *args, **kwargs)

            return APIResponse(200, True, results=user.data)

    def post(self, request, *args, **kwargs):
        user = self.create(request, *args, **kwargs)

        return APIResponse(200, True, results=user.data)

    def delete(self, request, *args, **kwargs):
        user = self.destroy(request, *args, **kwargs)
        try:
            if user:
                return APIResponse(200, True, "删除成功")
        except:
            return APIResponse(400, results="删除失败")


class UpdateAPIView(GenericAPIView, CreateModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmpolyeeModelSerializers
    lookup_field = 'id'

    def post(self, request, *args, **kwargs):
        Employee.objects.filter(emp_name=self.get_object()).delete()
        user = self.create(request,*args,**kwargs)


        return APIResponse(200, True, results="修改成功")
