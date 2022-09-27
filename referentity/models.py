from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils.translation import gettext_lazy as _
from .services import gen_random_code

class CustomAccountManager(BaseUserManager):
    def create_user(self, phone_number , name, email ,password, **other_fields):
        if password is None:
            password=self.make_random_password()
        if not phone_number:
            raise ValueError(_('Provide an Phone Number for the user')) 
        if email=='' or None:
            user = Users(name=name,phone_number=phone_number, invite_code=gen_random_code(11) , **other_fields)
        else:
            user = Users(name=name,phone_number=phone_number,email = self.normalize_email(email), **other_fields)
        user.set_password(password)
        user.save(self._db)
        return user

    ##creating a super user or a admin for managing the whole things.
    def create_superuser(self,name,phone_number,password, **other_fields):
        other_fields.setdefault('is_admin', True)
        other_fields.setdefault('is_superuser', True)

        return self.create_user( phone_number,name,'',password, **other_fields)


class Users(AbstractBaseUser,PermissionsMixin): 
    email = models.EmailField(_('email address'),
                                blank=True,
                                null=True,
                                max_length=100,
                                )
    phone_number = models.CharField(_('Phone Number'),
                                blank=False,
                                null=False,
                                max_length=12,
                                unique=True
                                )
    country_code = models.CharField(_('Country Code'),blank=False,null=False,max_length=5)
    name = models.CharField(_('user name'),
                                blank=False,
                                null=False,
                                max_length=100)
    city = models.CharField(_('city'),
                                blank=True,
                                null=True,
                                max_length=100)
    
    invite_code = models.CharField(_('invite code'),
                                    blank=True,
                                    null=True,
                                    max_length=10
                                    )
    refer_count = models.IntegerField(blank=True,
                                    null=True,default=0)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_created=True,auto_now=True)
    updated_at = models.DateTimeField(auto_created=True,auto_now_add=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return str(self.name)

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return True
    
    def check_password(self, raw_password: str) -> bool:
        return super().check_password(raw_password)
 
    class Meta:
        db_table = "Users"
 