from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import customuser
from.serializers import customuserserializer,userbyidserializer

# Create your views here.

@csrf_exempt
def showusers(request):
    if request.method=='GET':
        reqobj=customuser.objects.all()
        reqobj_x=customuserserializer(reqobj,many=True)
        return JsonResponse(reqobj_x.data,safe=False)
    return JsonResponse({'message':'failed to fetch only GET method Allowed'})

@csrf_exempt
def signup(request):
    if request.method=='POST':
        data=JSONParser().parse(request)
        if(data.get("fn") !=None and data.get("ln")!=None and data.get("email")!=None and data.get("pw")!=None and data.get("dob")!=None):
            newuser=customuser.objects.create(
                firstname=data.get("fn") ,
                lastname=data.get('ln') ,
                email= data.get("email"),
                DOB=data.get("dob") ,

            )
            newuser.set_password(data.get("pw"))
            newuser.save()
            return JsonResponse({"status":"created succesfully"})
        else:
            return JsonResponse({"status":"failed to create due to invalid Credentials"})
        
    else:
        return JsonResponse({"status":"failed only POST methods Allowed"})
    
@csrf_exempt
def deleteuser(request,uid):
    if (request.method=='DELETE'):
         requser= customuser.objects.get(id=uid)
         requser.delete()
         return JsonResponse({"message":"Account Succesfully Deleted"})
    else:
        return JsonResponse({"message":"only DELETE method Allowed"})
    

@csrf_exempt
def getuserbyid(request,uid):
    
    if request.method=='GET':
        try:
            requser=customuser.objects.get(id=uid)
        except:
            return JsonResponse("no such user Exists",safe=False)
        else:
            requser=customuser.objects.get(id=uid)
            requser_x=userbyidserializer(requser)
            return JsonResponse(requser_x.data,safe=False)
    else:
        return JsonResponse("only GET method allowed",safe=False)