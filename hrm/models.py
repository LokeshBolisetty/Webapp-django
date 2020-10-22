from django.db import models

class mentor(models.Model):
    #username = models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    #courses = models.ManyToManyField(Courses,help_text="Enter all the courses you are dealing with")
    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    mentor = models.ManyToManyField(mentor,help_text="Enter the names of the mentors of this course.")
    def __str__(self):
        return self.title
    def mentors(self):
        return ', '.join(mentor.name for mentor in self.mentor.all())
    #display_mentors.short_description = 'Mentor(s)'



