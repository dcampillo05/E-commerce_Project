from django.db import models
from PIL import Image
from django.conf import settings
import os


class Produto(models.Model):
    nome = models.CharField(max_length = 255, verbose_name = 'Nome do Produto')
    shortDesc = models.TextField(max_length = 255, verbose_name = 'Descrição Curta')
    longDesc = models.TextField(verbose_name = 'Descrição longa')
    imagem = models.ImageField(
        upload_to = 'produtos_imagem/%Y/%m/', blank = True, null = True
    )
    slug = models.SlugField(unique = True)
    preco = models.FloatField(verbose_name = 'Preço')
    precoPromocional = models.FloatField(default = 0, verbose_name = 'Preço Promocional')
    tipo = models.CharField(
        default = 'V',
        max_length = 1,
        choices = (
            ('V', 'Variação'),
            ('S', 'Simples')
        )
    )

    @staticmethod

    def resizeImage(img, new_width = 800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_heigth = img_pil.size
        
        if original_width <= new_width:
            print('Retornando! A largura original é menor do que a nova largura!')
            img_pil.close()
            return

        new_height = round((new_width * original_heigth) / original_width)
        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize = True,
            quality = 50
        )
        print('A imagem foi redimencionada')

        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        max_image_size = 800

        if self.imagem:
            self.resizeImage(self.imagem, max_image_size)

    def __str__(self):
        return self.nome

class Var(models.Model):
    produto = models.ForeignKey(Produto, on_delete = models.CASCADE)
    nome = models.CharField(max_length = 50, blank = True, null = True)
    preco = models.FloatField(verbose_name = 'Preço')
    precoPromocional = models.FloatField(default = 0, verbose_name = 'Preço Promocional')
    estoque = models.PositiveIntegerField(default = 1)

    def __str__(self): 
        return self.nome or self.produto.nome
    
    class Meta:
        verbose_name = 'Var'
        verbose_name_plural = 'Var'