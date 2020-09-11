from django.db import models
from mainapp.models import Delivery_agent

class Agent_docs(models.Model):
    driving_license = models.ImageField(upload_to="documents")
    aadhar_card = models.ImageField(upload_to="documents")
    passbook = models.ImageField(upload_to="documents")
    agent_id = models.ForeignKey(Delivery_agent, on_delete=models.CASCADE)

    class Meta:
        db_table = "agentdocs"

