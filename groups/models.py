from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.CharField(max_length=30)
    language = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name}  {self.last_name}'

class Students(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}  {self.last_name}'

class Group(models.Model):
    title = models.CharField(max_length=30)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.title}'

class GroupStudents(models.Model):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.student_id} -> {self.group_id}'

    class Meta:
        verbose_name = 'Group student'
        verbose_name = 'Group students'
        

    


        
