from django.db import models


class Me(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    family_name = models.CharField(max_length=30)
    birth = models.IntegerField(default=2000)
    birth_day = models.DateField()
    college = models.CharField(max_length=60)
    univerity = models.CharField(max_length=60)
    # i'm 
    im1 = models.CharField(max_length=100)
    im2 = models.CharField(max_length=100)
    im3 = models.CharField(max_length=100)
    im4 = models.CharField(max_length=100, null=True, default="freelance")

    # skills in web
    html = models.IntegerField(default=100)
    django = models.IntegerField(default=70)
    php = models.IntegerField(default=50)
    css = models.IntegerField(default=70)
    bootstrap = models.IntegerField(default=20)
    js = models.IntegerField(default=50, null=True)

    # language
    python = models.IntegerField(default=80)
    cshap = models.IntegerField(default=40)
    kotlin = models.IntegerField(default=60)
    c_and_cpp = models.IntegerField(default=60)

    # media sociaux links
    facebook = models.CharField(max_length=300, null=True)
    whatsapp = models.CharField(max_length=300, null=True)
    telegram = models.CharField(max_length=300, null=True)
    linkedin = models.CharField(max_length=300, null=True)
    github = models.CharField(max_length=300, null=True)

    # bout me
    about = models.CharField(max_length=300, null=True)

    # contact number
    number1 = models.CharField(max_length=10, null=True)
    number2 = models.CharField(max_length=10, null=True)
    email = models.EmailField(max_length=30, null=True)

    # city
    city = models.CharField(max_length=100, null=True)



    def __str__(self):
        return f" my name {self.first_name}"
