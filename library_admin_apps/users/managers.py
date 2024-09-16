from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, **kwargs):
        if "email" not in kwargs:
            raise ValueError(
                "email must be provided for a user"
            )
        user = self.model(email=kwargs.pop("email"), **kwargs)
        user.set_password(kwargs.pop("password", ""))
        user.is_active = True
        user.save()
        return user
    
    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
