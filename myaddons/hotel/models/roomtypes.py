from odoo import models, fields

class HotelRoomTypes(models.Model):
    _name = 'hotel.roomtypes'
    _description = 'Hotel Room Types'

    name = fields.Char("Room Type", required=True)
    description = fields.Char("Room Type Description")