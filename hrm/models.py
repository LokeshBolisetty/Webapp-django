from django.db import models

#This is the model which makes database of mentors. Any field that ha to be added to a mentor or deleted from a mentor has to be done from here. 
# After making changes in this class do not forget to make migrations and migrate them failing which no changes will be applied to the database and may lead to errors.

class mentor(models.Model):
    #username = models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    #Here courses have to be connected to each of the mentors. Adding a manytomany field gives error because course is defined after this class. 
    #Some method either in Mentor or in Course has to be created which connects mentors to courses also. 

    #courses = models.ManyToManyField(Courses,help_text="Enter all the courses you are dealing with")

    #This method overrides the __str__ method in models.Model to return the name of the mentor while viewing in the admin site.

    def __str__(self):
        return self.name
    #This field allows mentor to add his photo to his profile. It takes images only. Other files will not be accepted. 
    #Its not compulsory to add a photo to his profile. (blank=True)
    #Image will be stored in the photos folder in BASE_DIR(Path(__file__).resolve(strict=True).parent.parent)

    photo = models.ImageField(upload_to='./photos',blank=True)

# This class creates a link between courses and its database.
# Any change made to this will be reflected in the database only if migrations are made without which one may face errors.

class Course(models.Model):

    #Name of the Course is to be given here.
    title = models.CharField(max_length=100)

    #Description of the course can be provided.
    description = models.TextField()

    #This links the courses to its mentors.
    mentor = models.ManyToManyField(mentor,help_text="Enter the names of the mentors of this course.")

    #This method overrides the __str__ method in models.Model to return the name of the course while viewing in the admin site.
    def __str__(self):
        return self.title
    
    #This method prints the names of the mentors. When you try to print the names of the mentors with the 'mentor' field itself, it gives numbers corresponding to each mentor. 
    #In order to get their names and not ID numbers, this method is created. 
    def mentors(self):
        return ', '.join(mentor.name for mentor in self.mentor.all())
    #display_mentors.short_description = 'Mentor(s)'



