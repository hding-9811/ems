from django.db import models

# Create your models here.


from django.db import models


# Create your models here.

class User(models.Model):
    gender_choices = (
        (0, "male"),
        (1, "female"),
    )

    username = models.CharField(max_length=80)
    real_name = models.CharField(max_length=80)
    password = models.CharField(max_length=80)
    gender = models.SmallIntegerField(choices=gender_choices, default=0)
    status = models.SmallIntegerField(default=False)
    register_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "bz_user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Employee(models.Model):
    emp_name = models.CharField(max_length=80)
    img = models.ImageField(upload_to="pic", default="pic/1.jpg")
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    age = models.IntegerField()

    @property
    def img_name(self):
        img_name=str(self.img).split('/')
        return img_name[-1]

    class Meta:
        db_table = "bz_employee"
        verbose_name = "员工"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.emp_name
