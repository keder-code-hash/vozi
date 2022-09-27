from django.shortcuts import render
from .forms import ReferralForm
from .models import Users
from .services import gen_random_code
import random


def index(request):
    if request.method=="GET":
        return render(request,"index.html",context={})
    if request.method=="POST":
        form=ReferralForm(request.POST)
        error=""
        name=form.data.get("name")
        phonenumber=form.data.get("phonenumber")
        city=form.data.get("city")
        invitecode=form.data.get("code")
        try:
            if invitecode is not None and invitecode not in [""," "]:
                _user=Users.objects.get(invite_code__exact=invitecode)
                refer=int(_user.refer_count)
                _user.refer_count=refer+1
                _user.save()
            refer_code=gen_random_code(random.randint(0,599))
            Users( name=name,
                        phone_number=phonenumber,
                        city=city,
                        invite_code=refer_code
                    ).save() 
            return render(request,"thankyou.html",context={'error':error,'invite_code':refer_code})
        except:
            error="This phone number may already exist or referral code is not valid"
            refer_code=""
        return render(request,"thankyou.html",context={'error':error,'invite_code':refer_code})

