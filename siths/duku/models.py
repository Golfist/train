from django.db import models

class Cruiser(models.Model):
    #question_text
    cruiser_class = models.CharField(max_length=200)
    #pub_date
    build_date = models.DateTimeField('date building')

    def __str__(self):
        return self.cruiser_class

class Weapon(models.Model):
    #question
    cruiser = models.ForeignKey(Cruiser, on_delete=models.CASCADE)
    #choice_text
    weapon_parametrs = models.CharField(max_length=200)
    #votes
    shot = models.IntegerField(default=0)

    def __str__(self):
        return self.weapon_parametrs