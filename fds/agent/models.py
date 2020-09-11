from django.db import models
from mainapp.models import Delivery_agent

class Agent_docs(models.Model):
    driving_license = models.ImageField(upload_to="documents",default="None")
    aadhar_card = models.ImageField(upload_to="documents",default="None")
    passbook = models.ImageField(upload_to="documents",default="None")
    agent_id = models.ForeignKey(Delivery_agent, on_delete=models.CASCADE)

    class Meta:
        db_table = "agentdocs"

