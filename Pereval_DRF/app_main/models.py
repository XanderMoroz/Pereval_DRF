from django.contrib.auth.models import User
from django.db import models

class Users(models.Model):
    """
    Класс модели для пользователей (туристов на перевале со смартфоном)
    Поля модели:
    user - идентификатор пользователя (связан со встроенной моделью User);
    email - уникальный адрес электронной почты.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    firstname = models.CharField(max_length=255, verbose_name="Имя")
    lastname = models.CharField(max_length=255, verbose_name="Фамилия")

    class Meta:
        verbose_name_plural = ("Пользователи")

class Coords(models.Model):
    """
    Класс модели для координат перевала.
    Поля модели:
    latitude - географическая широта;
    longitude - географическая долгота;
    height - высота над уровнем моря
    """
    latitude = models.FloatField(max_length=254, verbose_name="Широта")
    longitude = models.FloatField(max_length=254, verbose_name="Долгота")
    height = models.IntegerField(verbose_name="Высота")

    def __str__(self):
        return f'{self.latitude} {self.longitude} {self.height}'

    class Meta:
        verbose_name_plural = ("Координаты")


class PerevalAdd(models.Model):
    """Класс модели для перевала."""
    NEW, PENDING, ACCEPTED, REJECTED = 'N', 'P', 'A', 'R'
    STATUS_CHOICES = [(NEW, 'new'),
                      (PENDING, 'pending',),
                      (ACCEPTED, 'accepted',),
                      (REJECTED, 'rejected')]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=NEW)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    coords_id = models.OneToOneField(Coords, on_delete=models.CASCADE)
    beautyTitle = models.CharField(max_length=254)
    title = models.CharField(max_length=254)
    other_titles = models.CharField(max_length=254)
    connect = models.TextField(blank=True)
    add_time = models.DateTimeField(auto_now_add=True)


class Level(models.Model):
    """
    Класс модели для категорий трудности. (В разное время года перевал может иметь разную категорию).
    Поля модели:
    pereval - перевал (связан с моделью PerevalAdd);
    level_spring - уровень сложности перевала весной;
    level_summer - уровень сложности перевала летом;
    level_autumn - уровень сложности перевала осенью;
    level_winter - уровень сложности перевала зимой;
    """
    pereval = models.ForeignKey(PerevalAdd, on_delete=models.CASCADE)
    level_spring = models.CharField(max_length=254, blank=True)
    level_summer = models.CharField(max_length=254, blank=True)
    level_autumn = models.CharField(max_length=254, blank=True)
    level_winter = models.CharField(max_length=254, blank=True)

    class Meta:
        verbose_name_plural = ("Категории сложности")

class Images(models.Model):
    """
    Класс модели для загружаемых картинок(фотографий перевалов):
    Поля модели:
    pereval - перевал, который сфотографировали (связан с моделью PerevalAdd);
    image - фото перевала (в виде необработанных двоичных данных);
    date_added - время добавления фото.
    """
    title = models.CharField(max_length=254)
    image = models.BinaryField()
    date_added = models.DateField(auto_now_add=True)
    pereval = models.ForeignKey(PerevalAdd, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pereval}: {self.title}'

    class Meta:
        verbose_name_plural = ("Фотографии")

