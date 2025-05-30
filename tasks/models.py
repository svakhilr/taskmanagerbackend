from django.db import models
from users.models import CustomUser


class Tasks(models.Model):
    
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    
    PRIORITY = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )
    
    TASK_STATUS = (
        (PENDING,"Pending"),
        (IN_PROGRESS,"In Progress"),
        (COMPLETED,"Completed")
    )



    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='tasks')
    priority = models.CharField(max_length=20,choices=PRIORITY)
    status = models.CharField(max_length=20,choices=TASK_STATUS)
    title = models.CharField(max_length=100)
    due_date = models.DateField()
    discription = models.TextField()

    def __str__(self):
        return self.title