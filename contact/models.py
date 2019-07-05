from django.db import models
import xmlrpc.client

# Create your models here.

class Contact (models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    mobile = models.CharField(max_length=14)
    phone = models.CharField(max_length=14)
    date_of_birth = models.DateField()
    email = models.EmailField()

    URL = "http://localhost:8069"
    DB = "Contact"
    USERNAME = "admin"
    PASSWORD = "admin"
    COMMON = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(URL))
    UID = COMMON.authenticate(DB, USERNAME, PASSWORD, {})
    def save(self):
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.URL))
        models.execute_kw(self.DB, self.UID, self.PASSWORD, 'res.partner', 'create', [{'name','heba'}])

    def __str__(self):
        return self.name