from auth.models import appusers
from .models import user

class Calls():

    """docstring for Calls."""

    def __init__(self):
        pass


    def profilecall(self,request):
        user1 = appusers()
        result = appusers.objects.filter(username=request.session.get("username") )

        user1.username = result.values_list('fullname', flat=True)[0]
        user1.location = result.values_list('location', flat=True)[0]  #result.location
        user1.birthday = result.values_list('birthday', flat=True)[0] #result.birthday
        user1.gmail = result.values_list('email', flat=True)[0] #result.birthday
        user1.twlink = 'test' #result.twlink
        user1.fblink = 'test' #result.fblink
        user1.gitlink = 'test' #result.gitlink

        return user1
