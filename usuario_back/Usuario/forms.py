from django import forms

INVERSIONISTA = "IN"
ESTUDIANTE = "ES"

class UsuarioFormRegistro(forms.Form):

    Role = (
        (INVERSIONISTA, 'Inversionista'),
        (ESTUDIANTE, 'Estudiante'),
    )

    nombreUsuario = forms.CharField(label="Usuario", max_length=30, min_length=3, required=True)
    correo = forms.CharField(label="Correo", max_length=60, min_length=3, required=True)
    password = forms.CharField(label="contrasena", max_length=40, min_length=3, required=True)
    role = forms.ChoiceField(choices=Role)

class UsuarioFormIngreso(forms.Form):

    Role = (
        (INVERSIONISTA, 'Inversionista'),
        (ESTUDIANTE, 'Estudiante'),
    )
    
    correo = forms.CharField(label="Correo", max_length=60, min_length=3, required=True)
    password = forms.CharField(label="contrasena", max_length=40, min_length=3, required=True)
    role = forms.ChoiceField(choices=Role)