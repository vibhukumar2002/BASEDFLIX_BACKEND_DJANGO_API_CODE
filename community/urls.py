from django.urls import path
from. import views

urlpatterns = [
    path('getroomslist/',views.getroomslist),
    path('gettopicslist/',views.gettopicslist),
    path('createnewtopic/<str:userstopic>/',views.createtopic),
    path('deleteroom/<int:rid>/<int:hid>/',views.deleteroom),
    path('createroom/<int:hid>/<int:tid>/',views.createroom),
    path('messagesbyroom/<int:rid>/',views.getmessagelistbyroom),
    path('allmessages/',views.getallmessages),
    path('newmessage/<int:rid>/<int:uid>/',views.createmessage),
    path('deletemessage/<int:mid>/<int:uid>/',views.deletemessage),
    path('allreplies/',views.getallreplies),
    path('getrepliesbyroom/<int:rid>/',views.getrepliesbyroom),
    path('getrepliesbythread/<int:mid>/',views.getrepliesbythread),
    path('createreply/<int:mid>/<int:uid>/',views.createreply),
    path('deletereply/<int:rid>/<int:uid>/',views.deletereply),
    path('getroombyid/<int:rid>/',views.gertoombyid),
    path('searchrooms/<str:query>/',views.searchrooms),
    path('searchmessages/<str:query>/',views.searchmessages),
    path('favs/<int:oid>/<int:mid>/<str:mn>/',views.addtoORremovefromFAVS),
    path('favslist/<int:uid>/',views.getfavslist),
    path('usersrooms/<int:uid>/',views.getroomsbyuser),
]


