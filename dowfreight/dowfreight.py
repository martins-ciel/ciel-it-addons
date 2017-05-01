
from openerp.osv import fields, osv
#from osv import fields, osv

class dowfreight_company(osv.Model):

    _name = 'dowfreight.company'
    _description = 'Companies'
    _columns = { 
            'external_id' : fields.char('External Id', size=30, required=True, help='Used to relate this record to ECC system.'),
            'name' : fields.char('Name', size=100, required=True),          
         }

class dowfreight_location(osv.Model):

    _name = 'dowfreight.location'
    _description = 'Locations'
    _columns = {
            'external_id' : fields.char('External Id', size=30, required=True, help='Used to relate this record to ECC system.'),
            'name' : fields.char('Name', size=100, required=True),
         }

class dowfreight_carrier(osv.Model):

    _name = 'dowfreight.carrier'
    _description = 'Carriers'
    _columns = {
            'external_id' : fields.char('External Id', size=30, required=True, help='Used to relate this record to ECC system.'),
            'name' : fields.char('Name', size=100, required=True),
         }

class dowfreight_carrier_bizshared(osv.Model):

    _name = 'dowfreight.carrier.bizshared'
    _description = 'Carrier Business Shared'
    _columns = {
            'company_id' : fields.many2one('dowfreight.company', 'Company', required=True),
            'carrier_id' : fields.many2one('dowfreight.carrier', 'Carrier', required=True),
            'bizshared' : fields.float('Business Shared %', required=True),
         }
    
class dowfreight_carrier_cost(osv.Model):

    _name = 'dowfreight.carrier.cost'
    _description = 'Carrier Cost'
    _columns = { 
            'company_id' : fields.many2one('dowfreight.company', 'Company', required=True),
            'carrier_id' : fields.many2one('dowfreight.carrier', 'Carrier', required=True),
            'location_id' : fields.many2one('dowfreight.location', 'Location', required=True),
            'freight_cost' : fields.float('Freight Cost', required=True),
         }
         
class dowfreight_deliverysheet(osv.Model):

    _name = 'dowfreight.deliverysheet'
    _description = 'Delivery Sheet'
    _columns = {
            'company_id' : fields.many2one('dowfreight.company', 'Company', required=True),
            'stage_id': fields.selection([('draft', 'Draft'),('delivery_imported', 'Delivery Imported'),('calculated', 'Calculated'),('approved', 'Approved'),('exported_to_ecc', 'Exported to ECC'),('carrier_notified', 'Carrier Notified'),], 'Stage', default='draft', required=True),
            'name' : fields.char('Name', size=100, required=True),          
            'date' : fields.datetime('Date', required=True),
            'delivery_imported_ids': fields.one2many('dowfreight.delivery.imported', 'deliverysheet_id', 'Deliveries Imported'),            
            'delivery_suggested_ids': fields.one2many('dowfreight.delivery.suggested', 'deliverysheet_id', 'Deliveries Suggested'),            
            'delivery_approved_ids': fields.one2many('dowfreight.delivery.approved', 'deliverysheet_id', 'Deliveries Approved'),            
         }

    def create_deliveries(self, cr, uid, ids, model_id, context=None):
        # Somente permitido caso o stage = "Draft"
        # Importar arquivo do ECC e cria deliveries "Imported"
        # Alterar o stage de "Draft" para "Imported"
        return none

    def calculate_carriers(self, cr, uid, ids, model_id, context=None):
        # Somente permitido caso o stage = "Imported"
        # Ira fazer o calculo com base nos parametros sugerindo menor custo para entrega
        # criar deliveries "Suggested" e "Approved" com base na "Imported"
        # Alterar o stage de "Imported" para "Calculated"
        return none

    def approve_deliveries(self, cr, uid, ids, model_id, context=None):
        # Somente permitido caso o stage = "Calculated"
        # Alterar o stage de "Calculated" para "Approved"
        return none

    def export_deliveries(self, cr, uid, ids, model_id, context=None):
        # Somente permitido caso o stage = "Approved"
        # Criar arquivo TXT para importacao no ECC
        # Alterar o stage de "Approved" para "ECC Exported"
        return none

    def back_to_draft(self, cr, uid, ids, model_id, context=None):
        # Somente permitido caso o stage <> "ECC Exported"
        return none

class dowfreight_delivery_base(osv.Model):

    _name = 'dowfreight.delivery.base'
    _description = 'Deliveries Base'
    _columns = {
            'deliverysheet_id' : fields.many2one('dowfreight.deliverysheet', 'Delivery Sheet', required=True),
            'carrier_id' : fields.many2one('dowfreight.carrier', 'Carrier', required=True),
            'location_id' : fields.many2one('dowfreight.location', 'Location', required=True),
            'name' : fields.char('Name', size=100, required=True),
            'freight_cost' : fields.float('Freight Cost', required=True),
         }
         
class dowfreight_delivery_imported(dowfreight_delivery_base):

    _name = 'dowfreight.delivery.imported'
    _description = 'Deliveries Imported'

class dowfreight_delivery_suggested(dowfreight_delivery_base):

    _name = 'dowfreight.delivery.suggested'
    _description = 'Deliveries Suggested'

class dowfreight_delivery_approved(dowfreight_delivery_base):

    _name = 'dowfreight.delivery.approved'
    _description = 'Deliveries Approved'
