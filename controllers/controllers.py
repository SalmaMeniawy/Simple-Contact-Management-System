# -*- coding: utf-8 -*-
from odoo import http

# class ContactManagementSystem(http.Controller):
#     @http.route('/contact_management_system/contact_management_system/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contact_management_system/contact_management_system/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('contact_management_system.listing', {
#             'root': '/contact_management_system/contact_management_system',
#             'objects': http.request.env['contact_management_system.contact_management_system'].search([]),
#         })

#     @http.route('/contact_management_system/contact_management_system/objects/<model("contact_management_system.contact_management_system"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contact_management_system.object', {
#             'object': obj
#         })