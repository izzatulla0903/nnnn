from django.contrib import admin
from groups.models import Group, GroupStudents
from groups.models import Teacher, Students

#register youtr models here 
admin.site.register(Teacher)
admin.site.register(Students)
# admin.site.register(Group)
admin.site.register(GroupStudents)


@admin.register(Group)
class Croups(admin.ModelAdmin): 
    list_display = ('id','title', 'teacher_id', 'count_of_students', 'list_of_students')

    def list_of_students(self, obj):
        # print(obj),'--------'
        qs = GroupStudents.objects.filter(group_id=obj.id)
        res = []
        for x in qs:
            x = str(x).split(' ->')
            res.append(x[0])
        if not res:
            return 'No students'
        return res

    def count_of_students(self, obj):
        qs = GroupStudents.objects.filter(group_id=obj.id)
        return qs.count

