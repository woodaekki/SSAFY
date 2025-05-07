from django.db import models

# Create your models here.
class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField()
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()

    def __str__(self):
        return f"{self.kor_co_nm} - {self.fin_prdt_nm}"

class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()

    def __str__(self):
        return f"{self.fin_prdt_cd} - {self.save_trm}개월"