from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
from tutoring.models import Course
from django.utils import timezone

# Create your models here.
    
class Student(models.Model):

    COLLEGE_LIST = (
        ('Revelle', 'Revelle'),
        ('Muir', 'Muir'),
        ('Marshall', 'Marshall'),
        ('Warren', 'Warren'),
        ('ERC', 'ERC'),
        ('Sixth', 'Sixth'),
        ('Seventh', 'Seventh'),
    )  

    MAJOR_LIST = (('Math', 'Mathematics'), ('CS', 'Computer Science'), 
        ('Bio', 'Biology'), ('Japn', 'Japanese Studies'), 
        ('Chem', 'Chemistry'), ('SE', 'Structural Engineering'), 
        ('Phys', 'Physics'), ('EE', 'Electrical Engineering'), 
        ('Poli', 'Political Science')
    )

    INTEREST_LIST = [('Anime', 'Anime'), ('WoW', 'World of Warcraft'), ('Racoon', 'Racoon Watching'),
        ('Speeding', 'Driving over speed limit'), ('HW', 'Doing Problem Set'), ('Travel', 'Traveling'),
        ('CS', 'Counter Strike'), ('LoL', 'League of Legends'), ('Football', 'Football')
    ]

    student_user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)  

    # Basic user information
    fname = models.CharField(max_length=200, null=True)
    lname = models.CharField(max_length=200, null=True)
    user_college = models.CharField(max_length=200, null=True, choices=COLLEGE_LIST)
    user_major = models.CharField(max_length=200, choices=MAJOR_LIST)
    profile_pic = models.ImageField(default="../icons/pfp.png",null=True, blank=True)

    # User contact info
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    ig = models.CharField(max_length=200, null=True)
    discord = models.CharField(max_length=200, null=True)

    # User interests
    user_interest1 = models.CharField(max_length=40, choices=INTEREST_LIST)
    user_interest2 = models.CharField(max_length=40, choices=INTEREST_LIST)
    user_interest3 = models.CharField(max_length=40, choices=INTEREST_LIST)
    
    # 3 categories of user's classes
    current_courses = models.ManyToManyField(Course, related_name='current_courses_set', blank=True)
    past_courses = models.ManyToManyField(Course, related_name='past_courses_set', blank=True)
    tutoring_courses = models.ManyToManyField(Course, related_name='tutoring_courses_set', blank=True)

    def __str__(self):
        return f'{self.fname} {self.lname}'

    # 地図: Set karma for each user, default is 0
    user_karma = models.IntegerField(default=0)

    #地図: Def set_karma, I don't think this is the right place to put it but it'll work for now
    def set_karma(self, add_karma):
        #print("！！\nset_karma has been called\n")

        #print("self.user_karma before:")
        #print(self.user_karma)

        self.user_karma += add_karma
        #print("self.user_karma after:")
        #print(self.user_karma)

        #print("！！\n")

    def set_phone(self, phone):
        self.phone = phone

    def set_ig(self, ig):
        self.ig = ig

    def set_discord(self, discord):
        self.discord = discord