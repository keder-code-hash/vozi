from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Users
from .services import gen_random_code


@receiver(pre_save,sender=Users)
def add_invite_code(sender,instance,**kwargs):
    if instance.id is None:
        pass
    print("working")
    if instance.invite_code is not None:
        user=Users.objects.get(invite_code=instance.code)
        refer=user.refer_count
        user.refer_count=refer+1 
    id = instance.id
    random_code= gen_random_code(id)   
    instance.invite_code=random_code 
    instance.save()