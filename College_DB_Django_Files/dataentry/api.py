from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from . serializers import *

class StudentList(APIView):
    def get(self,request):
        model = Student.objects.all()
        serializer = StudentSerializer(model,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        
            
        
class AttendanceList(APIView):
    def get(self,request):
        model = Attendance.objects.all()
        serializer = AttendanceSerializer(model,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    
class MarksList(APIView):
    def get(self,request):
        model = Marks.objects.all()
        serializer = MarksSerializer(model,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = MarksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    
class AadharList(APIView):
    def get(self,request):
        model = Aadhar.objects.all()
        serializer = AadharSerializer(model,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = AadharSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
class FeesList(APIView):
    def get(self,request):
        model = Fees.objects.all()
        serializer = FeesSerializer(model,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        model = Fees.objects.all()
        serializer = FeesSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    
class DepartmentList(APIView):
    def get(self,request):
        model = Department.objects.all()
        serializer = DepartmentSerializer(model,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    
    
class HostelList(APIView):
    def get(self,request):
        model = Hostel.objects.all()
        serializer = HostelSerializer(model,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = HostelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    
class ImpInfoList(APIView):
    def get(self,request):
        model = ImpInfo.objects.all()
        serializer = ImpInfoSerializer(model,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ImpInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    
class TeacherList(APIView):
    def get(self,request):
        model = Teacher.objects.all()
        serializer = TeacherSerializer(model,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
class BacklogsList(APIView):
    def get(self,request):
        model = Backlogs.objects.all()
        serializer = BacklogsSerializer(model,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = BacklogsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)