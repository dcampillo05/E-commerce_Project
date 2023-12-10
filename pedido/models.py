from django.db import models
from django.contrib.auth.models import User

class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Usuario')
    total = models.FloatField()
    status = models.CharField(
        default = 'C',
        max_length = 1,
        choices = (
            ('A', 'Aprovado'),
            ('C', 'Criado'),
            ('R', 'Reprovado'),
            ('P', 'Pendente'),
            ('E', 'Enviando'),  
            ('F', 'Finalizado')
        )
    )

    def __str__(self):
        return f'Pedido N. {self.pk}'
    

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete = models.CASCADE)
    produto = models.CharField(max_length = 255)
    IdProduto = models.PositiveIntegerField(verbose_name = 'Id do Produto') 
    variacao = models.CharField(max_length = 255, verbose_name = 'Variação')
    IdVariacao = models.PositiveIntegerField(verbose_name = 'Id da Variação')
    preco = models.FloatField(verbose_name = 'Preço')
    precoPromocional = models.FloatField(default = 0, verbose_name = 'Preço Promocional')
    qntd = models.PositiveIntegerField(verbose_name = 'Quantidade de estoque')
    imagem = models.CharField(max_length = 2000)

    def __str__(self):
        return f'Item do {self.pedido}'
    
    class meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens do pedido'
