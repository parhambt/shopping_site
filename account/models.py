from django.db import models
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser , AbstractUser 
# Create your models here.
class CustomeUserManager(BaseUserManager)  :
    use_in_migrations = True
    def create_user(self,username,email,password=None)  :
        if not username  :
            raise ValueError('user must have email')
        if not email : 
            raise ValueError('user must have email')
        
        user=self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,username,email,password=None)  :
        
        superuser=self.create_user(username=username,email=self.normalize_email(email),password=password)
        superuser.is_admin=True
        superuser.is_staff=True
        superuser.is_superuser=True
        superuser.is_active=True
        superuser.save(using=self._db)
        return superuser

    







class CustomeUser(AbstractBaseUser):
    use_in_migrations = True
    email = models.EmailField(verbose_name='email',unique=True,max_length=255) #required
    phone_number=models.CharField(max_length=12,verbose_name='phone number',blank=True)
    username=models.CharField(max_length=255,unique=True,verbose_name="user name") #required
    address=models.CharField(max_length=255,blank=True)
    first_name=models.CharField(max_length=64,blank=True,verbose_name='first name')
    last_name=models.CharField(max_length=64,blank=True,verbose_name="last name")



    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)


    is_active=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)

    objects=CustomeUserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username'] # email , username , password

    def __str__(self) : 
        return self.email
    
    def has_perm(self,perm,obj=None) : 
        return self.is_admin

    def has_module_perms(self,add_label):
        return True
    class Meta : 
        verbose_name="User"



    
        






    



    
