from django.contrib.auth import get_user_model
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import roomserializer,topicserializer,messageserializer,replyserializer,favsserializer
from .models import room,topic,message,reply,favs
from .forms import roomform
from django.db.models import Q
# from ..customusermodel.serializers import customuserserializer


# Create your views here.
@csrf_exempt
def getroomslist(request):

    if request.method=='GET':
        reqdata=room.objects.all()
        reqdata_x=roomserializer(reqdata,many=True)
        return JsonResponse({"data":reqdata_x.data})
    else:
        return JsonResponse({"detail":"Only Get Method Allowed"})
    

@csrf_exempt
def gettopicslist(request):
    if request.method=='GET':
        reqdata=topic.objects.all()
        reqdata_x=topicserializer(reqdata,many=True)
        return JsonResponse({'data':reqdata_x.data})
    else:
        return JsonResponse({'detail':'only get method allowed'}) 
    
@csrf_exempt
def createtopic(request,userstopic):
    if request.method=='POST':
        try:
            reqdata=topic.objects.get(topicname=userstopic)
            return JsonResponse({'detail':'topic already exists'})
        except:

        
            newtopic=topic.objects.create(
                topicname=userstopic
            )
            newtopic.save()
            return JsonResponse({'data':'topic added succesfully'})

        
        
    else:
        return JsonResponse({'detail':'only POST method allowed'})
    
@csrf_exempt
def deleteroom(request,rid,hid):
    if request.method=='DELETE':
        try:
            reqobj=room.objects.get(id=rid,host=hid)
            reqobj.delete()
            return JsonResponse({'data':'deleted Succesfully'}) 
        except:
            return JsonResponse({'detail':'you are not the host you are not supposed to be here'})
    
    else:
        return JsonResponse({'detail':'only DELETE method allowed Failed to delete'})


@csrf_exempt
def createroom(request,hid,tid):
    User=get_user_model()
    if request.method=='POST':
        inpdata=JSONParser().parse(request)
        try:
            reqhost=User.objects.get(id=hid)
        # reqtopic=topic.objects.get(topicname=inpdata.get('topic'))
            try:
                duproom=room.objects.get(name=inpdata.get('name'),roomtopic=tid)
                
            except:
                newroom=room.objects.create(
                name= inpdata.get('name'),
                roomtopic=topic.objects.get(id=tid),
                host=reqhost,
                desc= inpdata.get('desc')
                )
                newroom.save()
                return JsonResponse("created succesfully",safe=False)
            else:
                return JsonResponse('Room with same name and topic Already Exists', safe=False)
        
            

        except:
            return JsonResponse({'detail':'ivalid credentials something went wrong'})
    
        
        # reqdata=roomformserializer(roomform)

        
    
    else:
        return JsonResponse("Only POST method Allowed",safe=False)

@csrf_exempt
def getmessagelistbyroom(request,rid):
    if request.method=='GET':
        try:
            reqroom=room.objects.get(id=rid)
            reqmess=reqroom.message_set.all()
            reqmess_x=messageserializer(reqmess,many=True)
            return JsonResponse({'data':reqmess_x.data})
        except:
            return JsonResponse({'detail':'room has been deleted or wrong room id or room has no messages'})
        
    else:
        return JsonResponse("Only Get Method Allowed",safe=False)
    

@csrf_exempt
def getallmessages(request):
    if request.method=='GET':
        reqdata= message.objects.all()
        reqdata_x=messageserializer(reqdata,many=True)
        return JsonResponse({"data":reqdata_x.data})
    else:
        return JsonResponse("Only GET Method Allowed",safe=False)


@csrf_exempt
def createmessage(request,rid,uid):
    if request.method=='POST':
        try:
            User=get_user_model()
            reqroom=room.objects.get(id=rid)
            requser=User.objects.get(id=uid)
            inpdata=JSONParser().parse(request)
            newmessage=message.objects.create(
                body=inpdata.get('body'),
                author=requser,
                roomname=reqroom

            )
            newmessage.save()
            return JsonResponse({'data':'message created succesfully'})
        except:
            return JsonResponse({'detail':'something went wrong invalid details/room has been deleted'})
        
    else:
        return JsonResponse('only POST method Allowed',safe=False)


@csrf_exempt
def deletemessage(request,mid,uid):
    if request.method=='DELETE':
        User=get_user_model()
        try:
            reqmess=message.objects.get(id=mid,author=uid)
            requser=User.objects.get(id=uid)
            if  reqmess :
                reqmess.delete()
                return JsonResponse({'detail':'deleted succesfully'})
            
        except:
            return JsonResponse({'detail':'You are not the author you are Not Supposed To be Here'})
        
    else:
        return JsonResponse('Only DELETE method Allowed',safe=False)
            
@csrf_exempt
def getallreplies(request) :
    if request.method=='GET':
        reqdata=reply.objects.all()
        reqdata_x=replyserializer(reqdata,many=True)
        return JsonResponse({'data':reqdata_x.data})
    else:
        return JsonResponse({'detail':'only Get Method Allowed'})
    
@csrf_exempt
def getrepliesbyroom(request,rid):
    if request.method=='GET':
        try:
            reqroom=room.objects.get(id=rid)
            reqdata= reqroom.reply_set.all()
            reqdatax=replyserializer(reqdata,many=True)
            return JsonResponse({'data':reqdatax.data})
        except:
            return JsonResponse({'detail':'room has been deleted orhas no replies'})
        
    else:
        return JsonResponse('Only Get Method Allowed',safe=False)
    
@csrf_exempt
def getrepliesbythread(request,mid):
    if request.method=='GET':
        try:
            reqmess=message.objects.get(id=mid)
            reqdata=reqmess.reply_set.all()
            reqdata_x=replyserializer(reqdata,many=True)
            return JsonResponse({'data':reqdata_x.data})
        except:
            return JsonResponse({"detail":"message has been deleted or room has been deleted"})
    
    else:
        return JsonResponse('only Get Method Allowed',safe=False)
    
@csrf_exempt
def createreply(request,mid,uid):
    if request.method=='POST':
        inpdata=JSONParser().parse(request)
        User=get_user_model()
        # try:
        reqmess=message.objects.get(id=mid)
        requser=User.objects.get(id=uid)
        if reqmess:
                # reqroom=room.objects.get(id=rid)
                reqroom=room.objects.get(id=reqmess.roomname.id)
                newreply=reply.objects.create(

                    author= requser ,
                    roomname= reqroom ,
                    threadname= reqmess ,
                    body = inpdata.get('body') ,

                )
                newreply.save()
                return JsonResponse({'detail': "created reply succesfully"})

        else:
                return JsonResponse({'detail':'message or room has been deleted'})
            
        # except:
        #     return JsonResponse({'detail':'Failed to all reply,invalid Data'})
        
    else:
        return JsonResponse({'detail':'Only POST method Allowed'})

##FIX CREATE REPLY BY NOT TAKING room ID
    

@csrf_exempt
def deletereply(request,rid,uid):
    if request.method=='DELETE':
        try:
            reqreply=reply.objects.get(id=rid,author=uid)
            if reqreply:
                reqreply.delete()
                return JsonResponse({'detail':'deleted reply Succesfully'})
            else:
                return JsonResponse({'detail':'Failed to delete'})
            
        except:
            return JsonResponse("failed to get object ",safe=False)
        
    else:
        return JsonResponse({'detail':'only DELETE method allowed'})

@csrf_exempt
def gertoombyid(request,rid):
    if request.method=='GET':
        try:
            reqroom=room.objects.get(id=rid)
            reqroom_x=roomserializer(reqroom)
            return JsonResponse(reqroom_x.data,safe=False)
        except:
            return JsonResponse("Rooms Has Been Deleted Or Dosent Exist",safe=False)
        
    else:
        return JsonResponse("only GET method Allowed",safe=False)

@csrf_exempt
def searchrooms(request,query):
    if request.method=="GET":
        try:
            
            reqdata=room.objects.filter(Q(name__icontains=query)|Q(roomtopic__topicname__icontains=query)
                                        |Q(host__firstname__icontains=query)|Q(host__lastname__icontains=query)
                                        |Q(desc__icontains=query))  
            reqdata_x=roomserializer(reqdata,many=True)    
            return JsonResponse(reqdata_x.data,safe=False)
        
        except:
            return JsonResponse('No Rooms With Matching Queries Found',safe=False)
        
    else:
        return JsonResponse('only POST method Allowed', safe=False)
    
@csrf_exempt
def searchmessages(request,query):
    if request.method=='GET':
        try:
            reqmess=message.objects.filter(Q(body__icontains=query)| Q(author__firstname__icontains=query) | Q(author__lastname__icontains=query))
        except:
            return JsonResponse('No Match',safe=False)
        else:
            reqmess=message.objects.filter(Q(body__icontains=query)| Q(author__firstname__icontains=query) | Q(author__lastname__icontains=query))
            reqmess_x=messageserializer(reqmess,many=True)
            return JsonResponse(reqmess_x.data,safe=False)
        
    else:
        return JsonResponse('Only GET method allowed',safe=False)


@csrf_exempt
def addtoORremovefromFAVS(request,oid,mid,mn):
    if request.method=='POST':
        User=get_user_model()
        requser=User.objects.get(id=oid)
        dupfav=favs.objects.filter(Q(movieid=mid ) & Q(owner=requser))
        if dupfav.count()>0:
             dupfav.delete()
             return JsonResponse('Succesfully Removed From Favourites',safe=False)
        else:
            newfav=favs.objects.create(
                owner=requser,
                movieid=mid,
                moviename=mn

            )
            newfav.save()
            return JsonResponse('Succesfully Added Favourites',safe=False)




        # try:
        #     dupfav=favs.objects.get(Q(movieid=mid ) & Q(owner__id=oid))
        # except:
        #     newfav=favs.objects.create(
        #         owner=requser,
        #         movieid=mid,
        #         moviename=mn

        #     )
        #     newfav.save()
        #     return JsonResponse('Succesfully Added Favourites',safe=False)
        # else:
        #     dupfav=favs.objects.get(Q(movieid=mid ) & Q(owner__id=oid))
        #     dupfav.delete()
        #     return JsonResponse('Succesfully Removed From Favourites',safe=False)
    else:
        return JsonResponse('Only POST method Allowed',safe=False)
    


@csrf_exempt
def getfavslist(request,uid):
    if request.method=='GET':
        User=get_user_model()
        requser=User.objects.get(id=uid)
        favslist=requser.favs_set.all()
        favslist_x=favsserializer(favslist,many=True)
        return JsonResponse(favslist_x.data,safe=False)
    else:
        return JsonResponse('Only GET method allowed',safe=False)


@csrf_exempt
def getroomsbyuser(request,uid):
    if request.method=='GET':
        User=get_user_model()
        requser=User.objects.get(id=uid)
        reqrooms=requser.room_set.all()
        reqdata=roomserializer(reqrooms,many=True)
        return JsonResponse(reqdata.data,safe=False)
    else:
        return JsonResponse('only GET method allowed',safe=False)