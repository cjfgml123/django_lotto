from django.db import models
from django.utils import timezone
import random

class GuessNumbers(models.Model):
    name = models.CharField(max_length=24)
    text = models.CharField(max_length=255)
    lottos = models.CharField(max_length=255,
        default='[1, 2, 3, 4, 5, 6]')
    num_lotto = models.IntegerField(default=3)
    update_date = models.DateTimeField()

    def generate(self):
        self.lottos = ""
        origin = list(range(1,46))

        for _ in range(0, self.num_lotto):
            random.shuffle(origin)
            guess = origin[:6] # 1~5
            guess.sort()
            self.lottos += str(guess) + '\n' #로또 번호 str에 6개 번호 셋 추가

        self.update_date =timezone.now()
        self.save()

    def __str__(self): #admin page에서 display 되는 텍스트에 대한 변경
        return "pk {} : {} - {}".format(self.pk, self.name, self.text)
