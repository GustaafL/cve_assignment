from django.db import models


class CVE(models.Model):
    cve_id = models.CharField(max_length=50)
    description = models.TextField()
