from django.db import models
import datetime
import uuid

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="img/")

    def __str__(self):
        return self.title



class Programacao(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="img/programacao/")
    info = models.TextField()

    def __str__(self):
        return self.title

class Filme(models.Model):

    GENERO_CHOICES = [
        ('acao', 'Ação'),
        ('animacao', 'Animação'),
        ('aventura','Aventura'), 
        ('comedia','Comédia'), 
        ('drama', 'Drama'), 
        ('suspense', 'Suspense'), 
        ('terror','Terror')
    ]
    CLASS_INDIC_CHOICES = [
        ('l','Livre'),
        ('10','+10'),
        ('12','+12'),
        ('14','+14'),
        ('16','+16'),
        ('18','+18'),
    ]
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        blank=True
    )

    titulo = models.CharField(
        max_length=200,
        unique=True
    )
        
    genero = models.CharField(
        max_length=30,
        choices=GENERO_CHOICES
    )

    diretor = models.CharField(
        max_length=100
    )
    
    class_indic = models.CharField(
        max_length=10,
        choices=CLASS_INDIC_CHOICES,
        default='l'
    )

    duracao = models.IntegerField(
        default=100
    )

    data_estreia = models.DateField(
        default = datetime.date.today
    )

    em_cartaz = models.BooleanField(
        default=True
    )

    poster = models.ImageField(
        blank=True
    )

    sinopse = models.TextField(
        default = 'Sinopse'
    )

    def __str__(self):
        return self.titulo

class Cinema(models.Model):
	
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		blank=True)

	nome = models.CharField(
		max_length=100,
		unique=True)

	cidade = models.CharField(
		max_length=100
	)

	estado = models.CharField(
		max_length=2
	)

	def __str__(self):
		return self.nome

class Salas(models.Model):

    TIPO_CHOICES = [
        ('2d','2D'),
        ('3d','3D'),
        ('premium2d','2D - Premium'),
        ('premium3d','3D - Premium'),
    ]

    TIPO_LEGENDA = [
        ('dublado', 'Dublado'),
        ('legendado', 'Legendado')
    ]
    
    cinema = models.ForeignKey(
        'Cinema',
        on_delete=models.CASCADE
    )

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        blank=True
    )

    nome = models.CharField(
        max_length=2,
    )

    capacidade = models.IntegerField(

    )

    tipo = models.CharField(
        max_length = 40,
        default = '2d',
        choices = TIPO_CHOICES
    )

    legenda = models.CharField(
        max_length = 10,
        default = 'dublado',
        choices = TIPO_LEGENDA,
    )

    sessoes = models.ManyToManyField(
        'Filme',
        through='Sessao',
        through_fields=('sala', 'filme'),
    )

    class Meta:
        constraints = [models.UniqueConstraint(fields = ['nome','cinema'], name='Unico')]
    
    def __str__(self):
        return "Sala " + self.nome + " - " + self.tipo + " - " + self.cinema.nome 

class Sessao(models.Model):

	id = models.UUIDField(
		primary_key=True,
		blank = True,
		default = uuid.uuid4
	)
	sala = models.ForeignKey(
		'Salas',
		on_delete=models.CASCADE,
	)

	filme = models.ForeignKey(
		'Filme',
		on_delete=models.CASCADE,
	)

	data = models.DateField(

		)

	horario = models.CharField(
    	max_length = 5,
	)
	
	class Meta:
		constraints = [models.UniqueConstraint(fields = ['sala', 'data', 'horario'], name='Unicos')]

	def __str__(self):
		return self.sala.cinema.nome +" - sala "+ self.sala.nome + " - " + self.filme.titulo +" - " + str(self.data)+ " " + self.horario



class Add_cat(models.Model):
    category = models.CharField("Name",max_length=25,unique=True)

    def __unicode__(self):
        return u'{0}'.format(self.category)

class Add_prod(models.Model):
    book = models.CharField("Book Name",max_length=40)
    author = models.CharField("Author",max_length=30)
    price = models.PositiveIntegerField("Price")
    image = models.ImageField(upload_to='images',null=True)
    cat = models.ForeignKey(Add_cat,on_delete=models.CASCADE)