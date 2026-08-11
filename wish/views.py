from rest_framework import generics, mixins

from .models import Teachers
from .serializers import TeacherSerializer


# using mixin
class TeacherListDeleteView(
    mixins.RetrieveModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView
):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer

    # GET /teachers/<pk>/
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    # DELETE /teachers/<pk>/
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


# without using mixin using
class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer