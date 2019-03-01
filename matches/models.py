from django.db import models

# Create your models here.


class Match(models.Model):
    date = models.DateField(auto_now=False)
    team1 = models.CharField(max_length=25)
    team2 = models.CharField(max_length=25)
    r_h = models.FloatField()
    r_a = models.FloatField()
    tp_h = models.PositiveIntegerField()
    tp_a = models.PositiveIntegerField()
    ap_h = models.PositiveIntegerField()
    ap_a = models.PositiveIntegerField()
    kp_h = models.PositiveIntegerField()
    kp_a = models.PositiveIntegerField()
    sy_h = models.PositiveIntegerField()
    sy_a = models.PositiveIntegerField()
    ph_h = models.PositiveIntegerField()
    pa_h = models.PositiveIntegerField()
    ob_h = models.PositiveIntegerField()
    ob_a = models.PositiveIntegerField()
    sht_h = models.PositiveIntegerField()
    sht_a = models.PositiveIntegerField()
    sht_all = models.PositiveIntegerField()
    g_h = models.PositiveIntegerField()
    g_a = models.PositiveIntegerField()
    g_all = models.PositiveIntegerField()
    cl_h = models.PositiveIntegerField()
    cl_a = models.PositiveIntegerField()
    result = models.CharField(max_length=1)
    ft = models.CharField(max_length=5)
    champ = models.CharField(max_length=15)

    objects = models.Manager()

    def __str__(self):
        return self.team1 + ' - ' + self.team2
