from django.db import models
from django.urls import reverse


class Poll(models.Model):
    title = models.TextField(max_length=200, verbose_name="Вопрос")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def get_absolute_url(self):
        return reverse('poll_view', kwargs={'pk': self.pk})

    def upper(self):
        return self.title.upper()

    def __str__(self):
        return f"{self.pk}. {self.title}"

    class Meta:
        db_table = 'polls'
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Choice(models.Model):
    question_id = models.ForeignKey("webapp.Poll", on_delete=models.DO_NOTHING,
                                    related_name="choices",
                                    verbose_name="Вопрос",)
    answer = models.TextField(max_length=200, verbose_name="Опрос")

    def __str__(self):
        return f"{self.pk}. {self.answer}"

    class Meta:
        db_table = 'choices'
        verbose_name = 'Варианта ответa'
        verbose_name_plural = 'Варианты ответов'


class Answer(models.Model):
    question = models.ForeignKey("webapp.Poll", on_delete=models.DO_NOTHING,
                                    related_name="answers",
                                    verbose_name="Опрос", )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    choices = models.ForeignKey("webapp.Choice", on_delete=models.DO_NOTHING,
                                    related_name="answers",
                                    verbose_name="Вариант ответа", )

    def __str__(self):
        return f"{self.pk}.  {self.question} - {self.choices}"

    class Meta:
        db_table = 'answers'
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'