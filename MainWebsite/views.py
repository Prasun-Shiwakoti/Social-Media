import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Post, DetailedUser
from PIL import Image
from django.core import serializers
from django.http import JsonResponse
import os
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from difflib import get_close_matches


def PIL2Django(img, name):
    thumb_io = BytesIO()
    img.save(thumb_io, format='JPEG')
    return InMemoryUploadedFile(thumb_io, None, f'{name}.jpg', 'image/jpeg',
                                len(thumb_io.getvalue()), None)

def home(request):
    if request.user.is_authenticated:
        all_users = DetailedUser.objects.exclude(username=request.user)
        self = DetailedUser.objects.get(username=request.user)
        return render(request, 'index.html', context={"all_users": all_users, "friends": json.loads(self.friends), "posts":Post.objects.all().order_by("-id"), "self":self})

    return render(request, "landing.html")

def editProfile(request):
    if request.user.is_authenticated:
        all_users = DetailedUser.objects.exclude(username=request.user)
        self = DetailedUser.objects.get(username=request.user)
        friends = self.friends
        context={"all_users": all_users, "friends": json.loads(friends), "error":"", "self":self}

        if request.method == "POST":
            username = request.POST.get("username") or request.user.username
            f_name = request.POST.get("f_name") or request.user.first_name
            l_name = request.POST.get("l_name") or request.user.last_name
            email = request.POST.get("email") or request.user.email
            gender = request.POST.get("male") 
            gender = (gender and "male") or "female"

            if username and username != request.user.username:
                if  User.objects.filter(username = username).exists():
                    context["error"] = "The username is already taken. Please try a different one"
                    return render(request, "edit-profile.html", context=context)
            
            User.objects.filter(username=request.user).update(username=username,first_name=f_name,last_name=l_name,email=email)
            DetailedUser.objects.filter(username=request.user).update(username=username,fname=f_name,lname=l_name,gender=gender)
        
            return redirect("/edit-profile")
        return render(request, "edit-profile.html", context=context)
    else:
        return render("/")

def editPassword(request):
    if request.user.is_authenticated:
        all_users = DetailedUser.objects.exclude(username=request.user)
        self = DetailedUser.objects.get(username=request.user)
        friends = self.friends
        context={"all_users": all_users,"self":DetailedUser.objects.get(username=request.user) ,"friends": json.loads(friends), "error":"", "self":self}

        if request.method == "POST":
            try:
                c_pass = request.POST["curr_password"]
                n_pass = request.POST["password"]
            except:
                context["error"] = "Something went wrong while changing password. Please try again."
                return render(request, "edit-password.html", context=context)
            
            user = auth.authenticate(username=request.user, password=c_pass)
            if user:
                user = User.objects.get(username=request.user)
                user.set_password(n_pass)
                user.save()
                context["error"] = "Password changed successfull"
            else:
                context["error"] = "The password is incorrect"


        return render(request, "edit-password.html", context=context)
    else:
        return redirect("/")

def messages(request):
    if request.user.is_authenticated:
        self = DetailedUser.objects.get(username=request.user)
        self_friends = json.loads(self.friends)
        to_chat = request.GET.get("t") 
        toChat = None
        
        if not to_chat:
            return redirect("/messages?t=" + self_friends[-1]["username"])
        
        for friend in self_friends:
            if to_chat == friend["username"]:
                toChat = friend
                break
        else:
            return redirect("/messages?t=" + self_friends[-1]["username"])


        all_chats = json.loads(self.chats)
        chats = all_chats.get(to_chat)
        if not chats:
            all_chats[to_chat] = []

        toChat["chats"] = all_chats.get(to_chat)

        """
        Create a chat field (JSONField) in DetailedUser table.
        Json Format: 
        {
            "username":[["message", sender], ["message", sender]....]
        }
        Json Example:
        Account: admin
        {
            "prasun":[[Hello admin, 1], ["Hi prasun", 0]...],
            "jhon" : [[Hello admin, 1], ["Hi jhon", 0]...],
        }
        0 : Message sent by user
        1 : Message not sent by user


        Regarding the sending data async, you might be able to use the request object of recieving user
        """
        
        return render(request, 'messages.html', context={"friends": json.loads(self.friends), "self":self, "toChat":toChat})
    return redirect("/")

def logout(request):
    auth.logout(request)
    DetailedUser.objects.filter(username=request.user).update(status='off')
    return redirect("/")

def login(request):
    if request.method == "POST":
        try:
            username = request.POST["username"]
            password = request.POST["password"]
        except:
            return render(request, "landing.html", context={"error: l"})
        user = auth.authenticate(username=username, password=password)
        if (user):
            auth.login(request, user)
            return redirect("/")
        else:
            return render(request, "landing.html",context={"error": "ic"})
        



    return render(request, "landing.html")

def register(request):
    if request.method == "POST":
        try:
            full_name = request.POST["fullname"].split(" ", maxsplit=1)
            if len(full_name) == 1:
                full_name += [" "]
            
            f_name, l_name = full_name
            username = request.POST["username"]
            password = request.POST["password"]
            email = request.POST["email"]
            gender = request.POST.get("male")
            gender = (gender and "male") or "female"
        except:
            return render(request, "landing.html", context={"error": "r"})

        if User.objects.filter(username=username).exists():
            return render(request, "landing.html", context={"error": "u_taken"})

        URL = os.getcwd()+f"/media/UserProfilePics/"
        # Image.open(URL+"default.jpg").convert('RGB').save(URL + username + ".jpg")
        # userProfilePic = Image.open(URL + username + ".jpg")
        userProfilePic = Image.open(URL+"default.jpg").convert("RGB")


        DetailedUser.objects.create(
            username = username,
            gender = gender,
            fname = f_name,
            lname = l_name,
            image = PIL2Django(userProfilePic, username)
        )

        user = User.objects.create_user(username=username, password=password, email=email, first_name=f_name, last_name=l_name)
        user.save()
        return render(request, "landing.html", context={"error": "success"})

        
    return render(request, 'landing.html')

def addFriend(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get("username")
            if username and username != request.user.username:
                user = DetailedUser.objects.get(username=request.user)
                friend = DetailedUser.objects.get(username=username)
                curr_friends = json.loads(user.friends)

                for curr_friend in curr_friends:
                    if curr_friend["username"] == username:
                        return redirect("/")

                data = {"username": friend.username, "f_name": friend.fname, "l_name": friend.lname, "status":friend.status, "image":friend.image.url}    
                curr_friends.append(data)
                DetailedUser.objects.filter(username=request.user).update(friends=json.dumps(curr_friends))
                data.update({"status":200})
                return JsonResponse(data)
            return JsonResponse({"status":202})
    return redirect("/")
            
def addPost(request):
    print(request.META)
    print(request.META["HTTP_REFERER"])
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                content = request.POST["content"]
                img = request.FILES.get("img")
                publisherimg = DetailedUser.objects.get(username=request.user).image
                if img:
                    Image.open(img)
                Post.objects.create(PublisherUsername=request.user.username, Publisher=(request.user.first_name+" "+request.user.last_name), Content=content, Image=request.FILES.get("img"), PublisherImage=publisherimg)
            except Exception as e:
                print(e)
            
            if request.META['HTTP_REFERER'].split("/")[3].startswith("timeline?u="):
                return redirect("timeline")
    return redirect("/")

def changePP(request):
    if request.user.is_authenticated:
        try:
            new_pp = request.FILES["pp"]
            Image.open(new_pp).convert("RGB").save(os.getcwd()+f"/media/UserProfilePics/{request.user}.jpg")
            return redirect("editProfile")
        except Exception as e:
            print(e)

    return redirect("/")

def addComment(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                id = request.POST["id"]
                post = Post.objects.get(id=id)
                commenter = DetailedUser.objects.get(username=request.user)
                comment = {"commenter":commenter, "comment":request.POST["comment"]}
                old_comments = json.loads(post.Comments)
                old_comments.append(comment)
                new_comments = json.dumps(old_comments, default=lambda x: serializers.serialize('json', [ x, ]))
                post.Comments=new_comments
                post.save()
            except Exception as e:
                print(e)
                return redirect("logout")
    return redirect("/")

def changeStatus(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            status = request.POST.get("status")
            if status:
                DetailedUser.objects.filter(username=request.user).update(status=status)
                return HttpResponse("Status 200 OK")
    return redirect("/")

def likePost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            id = request.POST.get("id")
            if id:
                post = Post.objects.get(id=id)
                likers = json.loads(post.Likers)
                if likers.get(request.user.username):
                    del likers[request.user.username]
                else:
                    likers[request.user.username] = 1
                
                post.Likers = json.dumps(likers)
                post.save()
    
    return HttpResponse("Status 200 OK")

def timeline(request):
    if request.user.is_authenticated:
        all_users = DetailedUser.objects.exclude(username=request.user)
        self = DetailedUser.objects.get(username=request.user)
        
        friend_id = request.GET.get("u")
        if not friend_id:
            return redirect("/timeline?u="+request.user.username)
        
        friendObj = DetailedUser.objects.get(username=friend_id)

        
        return render(request, 'timeline.html', context={"all_users": all_users, "friends": json.loads(self.friends), "posts":Post.objects.filter(PublisherUsername=friend_id).order_by("-id"), "self":self, "friend":friendObj})

def searchUser(request):
    if request.method == "POST":
        uname = request.POST.get("searched")
        if uname:
            userData = {}

            for user in DetailedUser.objects.all():
                fullname = user.fname 
                if " " in uname:
                    fullname += user.lname

                if fullname in userData:
                    userData[fullname].add(user)
                else:
                    userData[fullname] = {user}
            
            matches = get_close_matches(uname, userData.keys(), 5)

            ret = []
            for match in matches:
                ret += userData[match]
            
            if ret.__len__() < 5:
                for user in DetailedUser.objects.filter(fname__startswith = uname):
                    if user not in ret:
                        ret.append(user)


            udata = []
            for user in ret:
                udata.append({"username": user.username, "fullname": user.fname + user.lname, "imageURL": user.image.url})
            data = {
                "status": 200,
                "ret": udata
            }
            return JsonResponse(json.dumps(data), safe=False)

    return HttpResponse("")







