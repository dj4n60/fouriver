from auth.models import appusers
from .models import user, developerinfo, customerinfo

class Calls():

    """docstring for Calls."""

    def __init__(self):
        pass


    def profilecall(self,request):
        user1 = appusers()
        result = appusers.objects.filter(username=request.session.get("username"))

        if request.session.get('idiotita') == 'developer':
            result1 = developerinfo.objects.filter(username=request.session.get("username"))

            user1.info1 = result1.values_list('github',flat=True)[0]
            user1.info2 = result1.values_list('cv', flat=True)[0]
            user1.info3 = result1.values_list('language', flat=True)[0]
            user1.profile_pic = 'test'# result1.values_list('profile_pic', flat=True)
            user1.location2 = result1.values_list('location', flat=True)[0]
            user1.location = user1.location2
        else:
            result2 = customerinfo.objects.filter(username=request.session.get("username"))

            user1.info1 = result2.values_list('linkedin', flat=True)[0]
            user1.info2 = result2.get('disc', flat=True)[0]
            user1.info3 = " "
            user1.profile_pic = result2.get('profile_pic', flat=True)[0]
            user1.location2 = result2.get('location', flat=True)[0]

        user1.username = result.values_list('fullname', flat=True)[0]
        user1.location = result.values_list('location', flat=True)[0]
        user1.birthday = result.values_list('birthday', flat=True)[0]
        user1.gmail = result.values_list('email', flat=True)[0]
        user1.twlink = 'test'
        user1.fblink = 'test'
        user1.gitlink = 'test'

        if user1.location2 in globals():
            user1.location = user1.location2


        return user1
