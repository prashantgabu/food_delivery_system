from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    feedback_date_time = models.DateTimeField()
    feedback_message = models.TextField()

    class Meta:
        db_table = "feedback"
