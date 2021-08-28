from django.db import models

def assignment_default():
    return {"default": "default"}

class AssignmentTemplate(models.Model):
    schema = models.JSONField(default=assignment_default, max_length=5000)
    title = models.CharField(default="title", max_length=200)

    def __str__(self):
        return str(self.schema)

class Assignment(models.Model):
    template = models.ForeignKey(AssignmentTemplate, default=1, on_delete=models.CASCADE)
    schema = models.JSONField(default=assignment_default, max_length=5000)
    
    def __str__(self):
        return str(self.schema)
