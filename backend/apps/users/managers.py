from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_kwargs):
        if not email:
            raise ValueError("The email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_kwargs):
        extra_kwargs.setdefault('is_staff', True)
        extra_kwargs.setdefault('is_superuser', True)
        extra_kwargs.setdefault('is_active', True)

        if extra_kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        user = self.create_user(email, password, **extra_kwargs)
        return user

    @staticmethod
    def to_admin(user):
        user.is_staff = True
        user.save()

    @staticmethod
    def to_user(user):
        user.is_staff = False
        user.save()
