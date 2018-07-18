import django_filters

from skill_db.models import Student
from django.contrib.auth.models import User

class StudentFilter(django_filters.FilterSet):

    class Meta:
        model = Student
        fields = {'group'}

    def __iter__(self):
        for each in self.__dict__.keys():
            yield self.__getattribute__(each)



