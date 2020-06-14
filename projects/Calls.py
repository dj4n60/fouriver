from auth.models import appusers
from .models import user, developerinfo, customerinfo

class Calls():

    """docstring for Calls."""

    def __init__(self):
        pass


    def profilecall(self,request):
        user1 = appusers()
        result = appusers.objects.filter(username=request.session.get("username"))


        if request.session.get('idiotita') == 'dev' :
            result1 = developerinfo.objects.filter(usenrame=request.session.get("username"))

            user1.info1 = result1.values_list('github', flat=True)[0]
            user1.info2 = result1.values_list('cv', flat=True)[0]
            user1.info3 = result1.values_list('language', flat=True)
            user1.profile_pic =' test'# result1.values_list('profile_pic', flat=True)[0]
            user1.location2 = result1.values_list('location', flat=True)
        else:
            result2 = customerinfo.objects.filter(username=request.session.get("username"))

            user1.info1 = result2.values_list('linkedin', flat=True)
            user1.info2 = result2.values_list('disc', flat=True)
            user1.info3 = " "
            user1.profile_pic = 'test'# result2.values_list('profile_pic', flat=True)
            user1.location2 = result2.values_list('location', flat=True)

        user1.username = result.values_list('fullname', flat=True)[0]
        user1.location = result.values_list('location', flat=True)[0]  #result.location
        user1.birthday = result.values_list('birthday', flat=True)[0] #result.birthday
        user1.gmail = result.values_list('email', flat=True)[0] #result.birthday
        user1.twlink = 'test' #result.twlink
        user1.fblink = 'test' #result.fblink
        user1.gitlink = 'test' #result.gitlink

        if user1.location2 in globals():
            user1.location = user1.location2


        return user1
