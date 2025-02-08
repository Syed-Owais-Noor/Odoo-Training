from odoo import models, fields, api, exceptions


state_selection = [
    ('draft', 'Draft'),
    ('publish', 'Publish'),
]


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = "Library Book"
    _inherit = ["mail.thread", "mail.activity.mixin"]


    # Enabling tracking so we can keep a record of values that a user changes of these fields

    name = fields.Char('Title', tracking=True)
    isbn = fields.Char('ISBN', tracking=True)

    # Setting a default value such that when a user will be creating a record then the current date will be set as the default value onward
    # the user may change it if needed

    date_published = fields.Date('Published Date', default=fields.Date.today(), tracking=True)

    image = fields.Binary('Cover Image')

    publisher_id = fields.Many2one('res.partner', string="Publisher ID", tracking=True)
    
    auther_ids = fields.Many2many('res.partner', string="Author IDs", tracking=True)

    active = fields.Boolean("Active", default=True)

    state = fields.Selection(selection=state_selection, string="Status", tracking=True, default='draft')

    is_published = fields.Boolean('Is Published', tracking=True)


    def action_publish(self):
        self.state = 'publish'

        self.is_published = True