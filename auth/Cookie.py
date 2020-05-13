from http.cookiejar import Cookie
from auth.models import appusers
import pickle


def createcookie(username, password):
    c = Cookie.SimpleCookie()
    c['username'] = username
    c['password'] = password
    c['idiotita'] = getidiotita(username)
    savecookies(c)


def getidiotita(username):
    result = appusers.objects.filter(username=username)
    for index in result:
            idiotita = index.idiotita
    return idiotita


def destroycookie(c):
    c.cookie.clear()


def savecookies(requests_cookiejar):
    with open('stored_cookies.txt', 'wb') as f:
        pickle.dump(requests_cookiejar)


def loadcookies(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)