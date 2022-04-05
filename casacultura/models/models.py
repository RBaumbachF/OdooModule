from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date, datetime, timedelta

class casacultura_usuarios(models.Model):
    _name = 'casacultura.usuarios'

    name = fields.Char(string="Nombre", required=True)
    dni = fields.Char(string="DNI", required=True)
    phone = fields.Char(string="Teléfono")
    birthDate = fields.Date(string="Fecha de nacimiento", required=True)
    age = fields.Integer(string="Edad", compute="_age", store=True)
    type = fields.Selection([("client", "Cliente"), ("instructor", "Monitor")], "Tipo de usuario", required=True)
    reservations = fields.One2many("casacultura.reservas", "user", string="Reservas realizadas")
    activities = fields.One2many("casacultura.actividades", "instructor", string="Actividad impartida")

    _sql_constraints = [('unique_dni','unique(dni)','El DNI ya está registrado')]

    @api.depends('birthDate')
    def _age(self):
        for record in self:
            if record.birthDate:
                record.age = (datetime.today().date() - datetime.strptime(str(record.birthDate), '%Y-%m-%d').date()) // timedelta(days=365)

    # @api.depends('dni')
    # def _dni(self, cr, uid, ids, context=None):
    #     record = self.browse(cr, uid, ids)
    #     pattern = "^\d{8}[A-Z]$"

class casacultura_actividades(models.Model):
    _name = 'casacultura.actividades'

    name = fields.Char(string="Nombre", required=True)
    description = fields.Char(string="Descripción")
    category = fields.Selection(string="Categoría", selection=[("workshop", "Taller"), ("trip", "Excursión"),("talk", "Charla")])
    date = fields.Datetime(string="Fecha")
    price = fields.Float("Precio", (8,2))
    instructor = fields.Many2one("casacultura.usuarios", string="Monitor")

    @api.constrains("date")
    def _date(self):
        if self.date < datetime.today():
            raise ValidationError("La fecha de la actividad no puede ser anterior a la actual")


class casacultura_reservas(models.Model):
    _name = 'casacultura.reservas'

    user = fields.Many2one("casacultura.usuarios", string="Usuario", required=True)
    age = fields.Integer(string="Edad", compute="_age", store=True)
    activity = fields.Many2one("casacultura.actividades", string="Actividad", required=True)
    date = fields.Datetime(string="Fecha", compute="_date", store=True)
    price = fields.Float(string="Precio", compute="_price", store=True)
    # totalprice = fields.Float(string="Importe total", compute="_totalprice", store=True)
    pagos = fields.One2many("casacultura.pagos", "reservation")

    @api.depends('activity.date')
    def _date(self):
        for r in self:
            r.date = r.activity.date

    @api.depends('activity.price')
    def _price(self):
        for r in self:
            r.price = r.activity.price

    @api.depends('user.age')
    def _age(self):
        for r in self:
            r.age = r.user.age


    # Además, el centro ofrece tarifas especiales a jóvenes (menores de 18 años) y
    # personas mayores de 65. En estos casos, el precio de la actividad se ve reducido en un 25%.
    
    # @api.onchange('age','price')
    # def _totalprice(self):
    #     if self.age > 18 or self.age < 65:
    #         self.totalprice = self.price
    #     else:
    #         self.totalprice = self.price * 0.8

class casacultura_pagos(models.Model):
    _name = 'casacultura.pagos'

    reservation = fields.Many2one("casacultura.reservas", string="Reserva", required=True)
    paymentMethod = fields.Selection(string="Método de pago", selection=[("cash", "Efectivo"), ("card", "Tarjeta"),("paypal", "PayPal")], default='cash')
    date = fields.Datetime(string="Fecha", compute="_date", store=True)
    totalprice = fields.Float(string="Importe", compute="_totalprice", store=True)

    @api.depends('reservation.date')
    def _date(self):
        for r in self:
            r.date = r.reservation.date

    @api.depends('reservation.price')
    def _totalprice(self):
        for r in self:
            r.totalprice = r.reservation.price
