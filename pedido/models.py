from django.db import models

class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
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
    IdProduto = models.PositiveIntegerField()
    variacao = models.CharField(max_length = 255)
    IdVariacao = models.PositiveIntegerField()
    preco = models.FloatField()
    precoPromocional = models.FloatField(default = 0)
    qntd = models.PositiveIntegerField()
    imagem = models.CharField(max_length = 2000)

    def __str__(self):
        return f'Item do {self.pedido}'
    
    class meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens do pedido'