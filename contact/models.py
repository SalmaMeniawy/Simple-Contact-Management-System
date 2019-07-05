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
    external_odoo_record_num = models.IntegerField(default=0)

    def save(self,*args,**kwargs):
        URL = "http://localhost:8069"
        DB = "Contact_odoo"
        USERNAME = "admin"
        PASSWORD = "admin"
        COMMON = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(URL))
        UID = COMMON.authenticate(DB, USERNAME, PASSWORD, {})
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(URL))
        if self.external_odoo_record_num == 0:
            self.external_odoo_record_num = models.execute_kw(DB, UID, PASSWORD, 'res.partner', 'create'
                                                          , [{'name':self.name ,'street':self.address
                                                                 ,'mobile':self.mobile, 'phone':self.phone ,
                                                              'birth_date': self.date_of_birth.strftime("%Y%m%d") ,
                                                              'email':self.email}])
        else:
            models.execute_kw(DB, UID, PASSWORD, 'res.partner', 'write', [[self.external_odoo_record_num], {
                'name': self.name, 'street': self.address, 'mobile': self.mobile, 'phone': self.phone
                , 'birth_date': self.date_of_birth.strftime("%Y%m%d"), 'email': self.email
            }])
        return super(Contact, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        URL = "http://localhost:8069"
        DB = "Contact_odoo"
        USERNAME = "admin"
        PASSWORD = "admin"
        COMMON = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(URL))
        UID = COMMON.authenticate(DB, USERNAME, PASSWORD, {})
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(URL))
        models.execute_kw(DB, UID, PASSWORD,'res.partner', 'unlink', [[self.external_odoo_record_num]])
        return super(Contact, self).delete(*args, **kwargs)





    def __str__(self):
        return self.name