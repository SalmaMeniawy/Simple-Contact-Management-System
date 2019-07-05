from odoo import models, fields, api

class res_partner(models.Model):
    _name='res.partner'
    _inherit = 'res.partner'

    birth_date = fields.Date(help="Date of birth ")
    @api.model
    def create(self, vals):
        # self.send_email()
        res = super(res_partner, self).create(vals)
        return res

    @api.model
    def send_email(self):
        import smtplib
        EMAIL = "xxxx@gmail.com"
        PASSWORD = "XXXXXXXXXX"
        MESSAGE = "we are greeting you for creating a new contact with us"
        user_email = self.email
        server = smtplib.SMTP('smtplib.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL ,user_email,MESSAGE)
        server.quit()



