from django.db import models
from django.contrib.auth.models import User

class perfil(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, verbose_name = 'Usuario')
    idade = models.PositiveIntegerField()
    data_nascimento = models.DateField(verbose_name = 'Data de Nascimento')
    cpf = models.CharField(max_length = 11, verbose_name = 'CPF')
    endereco = models.CharField(max_length = 50, verbose_name = 'Endereço')
    numero  = models.CharField(max_length = 5)
    complemento = models.CharField(max_length = 10)
    bairro = models.CharField(max_length = 50)
    cep = models.CharField(max_length = 8)
    cidade = models.CharField(max_length = 30)
    estado = models.CharField(
        max_length = 2,
        default = 'SP',
        choices = (
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    def clean(self):
        pass

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = "Perfis"
    