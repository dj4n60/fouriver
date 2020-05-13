from http.cookiejar import Cookie
from auth.models import appusers


def createcookie(username, password):
    c = Cookie.SimpleCookie()
    c['username'] = username
    c['password'] = password
    c['idiotita'] = getidiotita(username)


def getidiotita(username):
    result = appusers.objects.filter(username=username)
    for index in result:
            idiotita = index.idiotita
    return idiotita


def destroycookie(c):
    c.cookie.clear()
