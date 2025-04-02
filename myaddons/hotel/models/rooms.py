from odoo import models, fields

class HotelRooms(models.Model):
    _name = 'hotel.rooms'
    _description = "Hotel Rooms"

    name = fields.Char("Room No.")
    description = fields.Char("Room Description")
