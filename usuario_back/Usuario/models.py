from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, correo, nombreUsuario, password = None):
        if not correo: 
            raise ValueError('El usuario debe tener un correo eléctronico')

        usuario = self.model(
            nombreUsuario = nombreUsuario,
            correo = self.normalize_email(correo),
        )

        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, nombreUsuario, correo, password):
        usuario = self.create_user(
            correo,
            nombreUsuario=nombreUsuario,
            password=password
        )
        usuario.is_admin = True; 
        usuario.save(using=self._db)
        return usuario

class Usuario(AbstractBaseUser):
    nombreUsuario = models.CharField(max_length=30, unique=True, null=False)
    correo = models.EmailField(primary_key=True, verbose_name="email", max_length=60)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects  = UserManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS  = ['nombreUsuario']

    def __str__(self):
        return '{}'.format(self.nombreUsuario)

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True 

    @property
    def is_staff(self):
        return self.is_admin  