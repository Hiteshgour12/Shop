from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from rest_framework_simplejwt.tokens import RefreshToken
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email,password=None , password2=None):
        """
        Creates and saves a User with the given email,name,tc,and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, name,tc and password.
        """
        user = self.create_user(
            email,
            password=password,
            
        )
        user.is_admin = True
        user.is_active =True
        user.name = 'admin'
        user.role = 'admin'
        user.save(using=self._db)
        return user
    

    # Custom User Manager
class User(AbstractBaseUser):
    DESIG = [
        ('admin', 'admin'),
        ('manager', 'manager'),
        ('user', 'user'),
        ]
    
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=20,blank=False,null=False)
    mobile_number = models.CharField(max_length=17,blank=False)
    role = models.CharField(choices=DESIG, max_length=200, default='user')
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



class UserProfiles(models.Model):
    user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    avatar = models.ImageField(upload_to='images/avatar/', default='images/avatar/avtar.jpg')
    bio = models.CharField(max_length=220, null=True, default='Intraduce your self......')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.bio
    
class UserAddress(models.Model):
    user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    aparment = models.CharField(max_length=220, null=True, default='H.No.')
    street  = models.CharField(max_length=150, null=True,default='Street/Landmark')
    postal_code = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=20, null=True)
    default = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.aparment