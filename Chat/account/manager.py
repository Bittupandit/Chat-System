from django.contrib.auth.base_user import BaseUserManager
from django.http import request


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self,email,password):
        if not email:
            raise ValueError('Email is required!')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        print(user.email,user.password)
        # user.paid = True
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
