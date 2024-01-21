from django.db import models

from habits.validators import filled_only_one, empty_both, \
    connected_is_pleasant, is_under7, is_under120


class Habit(models.Model):

    user = models.ForeignKey("users.User", on_delete=models.CASCADE,
                             verbose_name="пользователь")
    place = models.CharField(max_length=100, verbose_name="место")
    time = models.TimeField(verbose_name="время")
    action = models.CharField(max_length=500, verbose_name="действие")
    is_pleasant = models.BooleanField(verbose_name="приятная", default=False)
    connected_habit = models.ForeignKey("Habit", on_delete=models.CASCADE,
                                        verbose_name="связана с",
                                        blank=True, null=True,
                                        validators=[connected_is_pleasant])
    periodity = models.IntegerField(verbose_name="повторяем через",
                                    default=1, validators=[is_under7])
    reward = models.CharField(max_length=500, verbose_name="награждение",
                              blank=True, null=True,)
    duration = models.IntegerField(verbose_name="продолжительность в секундах",
                                   default=60, validators=[is_under120])
    is_public = models.BooleanField(verbose_name="можно опубликовать")

    def save(self, **kwargs):
        self.clean()
        return super(Habit, self).save(**kwargs)

    def clean(self):
        print("clean active")
        filled_only_one(self.reward, self.connected_habit)

        if self.is_pleasant:
            empty_both(self.reward, self.connected_habit)


class SendingLog(models.Model):

    last_send = models.DateTimeField(verbose_name="дата последней отправки")
    habit_sent = models.ForeignKey("Habit",
                                   verbose_name="привычка",
                                   on_delete=models.CASCADE)
