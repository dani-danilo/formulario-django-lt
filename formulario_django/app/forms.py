from django import forms

class RegistroForm(forms.Form):
    usuario = forms.CharField(label="Usuario", max_length=100)
    contraseña = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput,
        max_length=100
    )

    def clean_contraseña(self):
        contraseña = self.cleaned_data.get('contraseña')
        especiales = "@#$%&*?!-_."

        if len(contraseña) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula, un número y un carácter especial (@#$%&*?!-_.).")

        tiene_mayuscula = any(c.isupper() for c in contraseña)
        tiene_minuscula = any(c.islower() for c in contraseña)
        tiene_numero = any(c.isdigit() for c in contraseña)
        tiene_especial = any(c in especiales for c in contraseña)

        if not (tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial):
            raise forms.ValidationError(
                "La contraseña debe tener mayúscula, minúscula, número y carácter especial (@#$%&*?!-_.)."
            )

        return contraseña