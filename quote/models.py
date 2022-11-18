from django.db import models
from django.contrib.auth.models import User

SPECIES = (('Pine', 'Pine'), ('Birch', 'Birch'), ('Spruce', 'Spruce'))

GRADE = ((0, "0"), (1, "1"), (2, "2"))

QUOTE_STATUS = (("not_submitted", "Not submitted"), ("submitted", "Submitted"), ("quoted", "Quote Emailed"))

STATUS = ((0, "Not submitted"), (1, "Submitted"), (2, "Quote Emailed"))

LENGTH_NEW = (("300", "300"), ("400", "400"), ("500", "500"))


class QuoteData(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name="User_id")
    title = models.CharField(max_length=20)
    species = models.CharField(choices=SPECIES, max_length=15)
    length = models.CharField(choices=LENGTH_NEW, default="400", max_length=10)
    width = models.IntegerField()
    thickness = models.IntegerField()
    quantity = models.IntegerField()
    deadline = models.DateField()
    quarter_sawn = models.BooleanField(default=False)
    grade = models.IntegerField(choices=GRADE, default=0)
    comments = models.TextField(max_length=200)
    submitted_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['deadline']

    def __str__(self):
        return f"""
        Item Id: {self.id} | Quote Id: {self.user_id}
         | Deadline date: {self.deadline}
         """
