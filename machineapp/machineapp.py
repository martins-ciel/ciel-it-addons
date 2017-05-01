from openerp.osv import fields, osv

class machineapp_plant(osv.Model):

    _name = 'machineapp.plant'
    _description = 'Plant'
    _columns = {
            'name' : fields.char('Name', size=100, required=True),
            'parent_id' : fields.many2one('machineapp.plant', 'Parent'),
        }

class machineapp_workcenter(osv.Model):

    _name = 'machineapp.workcenter'
    _description = 'Work Center'
    _columns = {
            'code' : fields.char('Code', size=100, required=True),
            'name' : fields.char('Description', size=100, required=True),
            'parent_id' : fields.many2one('machineapp.workcenter', 'Parent'),
            'plant_id' : fields.many2one('machineapp.plant', 'Plant', required=True),
        }

class machineapp_machine(osv.Model):

    _name = 'machineapp.machine'
    _description = 'Machine'
    _columns = {
            'name' : fields.char('Name', size=100, required=True),
            'workcenter_id' : fields.many2one('machineapp.workcenter', 'Work Center', required=True),
            'barcode' : fields.char('Barcode', size=100),
            'max_perc_downtime' : fields.float('Maximum percentage of Downtime'),
            'max_perc_setup' : fields.float('Maximum percentage of Setup'),
            'min_perc_prod_time' : fields.float('Minimum percentage Productive Time'),
            'active' : fields.boolean('Active', default=False),
        }

class machineapp_operator(osv.Model):

    _name = 'machineapp.operator'
    _description = 'Operator'
    _columns = {
            'name' : fields.char('Name', size=100, required=True),
            'plant_id' : fields.many2one('machineapp.plant', 'Plant', required=True),
            'barcode' : fields.char('Barcode', size=100),
        }

class machineapp_action(osv.Model):

    _name = 'machineapp.action'
    _description = 'Action'
    _columns = {
            'name' : fields.char('Name', size=100, required=True),
            'barcode' : fields.char('Barcode', size=100),
            'type': fields.selection([('setup', 'Setup'),('productive', 'Productive'),('downtime', 'Downtime'),('idle', 'Idle'),('consumption','Consumption'),], 'Type', required=True),
            'production_order' : fields.boolean('Ask Production Order and Finish Good?', default=False),
            'qtd_produced' : fields.boolean('Ask Quantity Produced?', default=False),
            'close_production' : fields.boolean('Ask to close Production Order?', default=False),
            'qtd_used' : fields.boolean('Ask Raw Material Quantity Used?', default=False),
        }

class machineapp_finishgood(osv.Model):

    _name = 'machineapp.finishgood'
    _description = 'Finish Good'
    _columns = {
            'code' : fields.char('Code', size=100, required=True),
            'name' : fields.char('Name', size=100, required=True),
            'barcode' : fields.char('Barcode', size=100),
        }

class machineapp_rawmaterial(osv.Model):

    _name = 'machineapp.rawmaterial'
    _description = 'Raw Material'
    _columns = {
            'code' : fields.char('Code', size=100, required=True),
            'name' : fields.char('Name', size=100, required=True),
            'barcode' : fields.char('Barcode', size=100),
        }

class machineapp_billofmaterial(osv.Model):

    _name = 'machineapp.billofmaterial'
    _description = 'Bill of Material'
    _columns = {
            'finishgood_id' : fields.many2one('machineapp.finishgood', 'Finish Good', required=True),
            'basequantity' : fields.float('Base Quantity', required=True),
            'component_ids': fields.one2many('machineapp.billofmaterialcomponent', 'billofmaterial_id', 'Components'),            
        }

class machineapp_billofmaterialcomponent(osv.Model):

    _name = 'machineapp.billofmaterialcomponent'
    _description = 'Bill of Material Component'
    _columns = {
            'billofmaterial_id' : fields.many2one('machineapp.billofmaterial', 'Bill of Material', required=True),
            'rawmaterial_id' : fields.many2one('machineapp.rawmaterial', 'Raw Material', required=True),
            'quantity' : fields.float('Quantity', required=True),
        }

class machineapp_routing(osv.Model):

    _name = 'machineapp.routing'
    _description = 'Routing'
    _columns = {
            'finishgood_id' : fields.many2one('machineapp.finishgood', 'Finish Good', required=True),
            'basequantity' : fields.float('Base Quantity', required=True),
            'operation_ids': fields.one2many('machineapp.routingoperation', 'routing_id', 'Operations'),
        }

class machineapp_routingoperation(osv.Model):

    _name = 'machineapp.routingoperation'
    _description = 'Routing Operation'
    _columns = {
            'routing_id' : fields.many2one('machineapp.routing', 'Routing', required=True),
            'machine_id' : fields.many2one('machineapp.machine', 'Machine', required=True),
            'minutes' : fields.float('Minutes', required=True),
        }

class machineapp_productionboard(osv.Model):

    _name = 'machineapp.productionboard'
    _description = 'Production Board'
    _columns = {
            'code' : fields.char('Code', size=100, required=True),
            'name' : fields.char('Name', size=100, required=True),
            'barcode' : fields.char('Barcode', size=100),
        }
        
