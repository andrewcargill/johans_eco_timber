from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Not submitted"), (1, "Submitted"), (2, "Quoted"))

class Quote(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Userid")
    quote_name = models.CharField(max_length = 50)
    status = models.IntegerField(choices=STATUS, default=0)
    submitted_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['submitted_date']

    def __str__(self):
        return f"Quote Id: {self.id}"

SPECIES = (('Pine', 'Pine'), ('Birch', 'Birch'), ('Spruce', 'Spruce'))

LENGTH = ((0, "300"), (1, "400"), (2, "500"))

GRADE = ((0, "0"), (1, "1"), (2, "2"))


class Item(models.Model):
    quote_id = models.ForeignKey(Quote, on_delete=models.CASCADE, 
                                 related_name="Quoteid")
    species = models.CharField(choices=SPECIES, max_length=15)
    length = models.IntegerField(choices=LENGTH, default=2)
    width = models.IntegerField()
    thickness = models.IntegerField()
    quantity = models.IntegerField()
    deadline = models.DateField()
    quarter_sawn = models.BooleanField(default=False)
    grade = models.IntegerField(choices=GRADE, default=0)
    comments = models.TextField(max_length=200)


    class Meta:
        ordering = ['deadline']

    def __str__(self):
        return f"Item Id: {self.id} | Quote Id: {self.quote_id} | Deadline date: {self.deadline}"