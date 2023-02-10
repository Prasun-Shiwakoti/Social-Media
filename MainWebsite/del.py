from .models import DetailedUser
from difflib import get_close_matches
from django.core import serializers


uname = ""
if uname:
    userData = {}

    for user in DetailedUser.objects.all():
        fullname = user.fname + " " + user.lname
        if (fullname) in userData:
            userData[fullname].append(user)
        else:
            userData[fullname] = [user]
    print(userData)

    matches = get_close_matches(uname, userData.keys(), len(userData))

    print(matches)

    ret = []
    for match in matches:
        ret += userData[match]
    print(ret)

    print(serializers.serialize(ret))