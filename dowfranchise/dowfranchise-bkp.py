from openerp.osv import fields, osv

class dowfranchise_culture(osv.Model):

    _name = 'dowfranchise.culture'
    _description = 'Cultures'
    _columns = {
            'name' : fields.char('Name', size=100, required=True),
            'business_ids' : fields.many2many('dowfranchise.business', 'dowfranchise_culture_business_rel', 'culture_id', 'business_id', string='Business'),
        }

class dowfranchise_businessline(osv.Model):

    _name = 'dowfranchise.businessline'
    _description = 'Business Lines'
    _columns = {
            'name' : fields.char('Name', size=100, required=True),
            'business_ids' : fields.many2many('dowfranchise.business', 'dowfranchise_businessline_business_rel', 'businessline_id', 'business_id', string='Business'),
        }

class dowfranchise_business(osv.Model):

    _name = 'dowfranchise.business'
    _description = 'Business'
    _columns = {
            'name' : fields.char('Name', size=100, required=True),
        }

class dowfranchise_locationarea(osv.Model):

    _name = 'dowfranchise.locationarea'
    _description = 'Location Areas'
    _columns = {
            'name' : fields.char('Name', size=100, required=True),
        }

class dowfranchise_terminationreason(osv.Model):

    _name = 'dowfranchise.terminationreason'
    _description = 'Termination Reason'
    _columns = {
            'name' : fields.char('Name', size=100, required=True),
        }

class dowfranchise_attribute(osv.Model):

    _name = 'dowfranchise.attribute'
    _description = 'Attributes'
    _columns = {
            'name' : fields.char('Name', size=100, required=True),
        }

class dowfranchise_criteria(osv.Model):

    _name = 'dowfranchise.criteria'
    _description = 'Criterias'
    _columns = {
            'name' : fields.char('Name', size=100, required=True),
            'weight': fields.selection([('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),], 'Weight', ),
            'weight_readonly' : fields.boolean('Weight Readonly', default=False),
            'attribute_id' : fields.many2one('dowfranchise.attribute', 'Attribute', required=True),
            'business_ids' : fields.many2many('dowfranchise.business', 'dowfranchise_criteria_business_rel', 'criteria_id', 'business_id', string='Business'),
        }

class dowfranchise_requestbase(osv.Model):
    _name = 'dowfranchise.requestbase'
    _description = 'Request Base'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _columns = {
            'name' : fields.char('Name', size=100, required=True),
 			'request_uid' : fields.many2one('res.users', 'Requested by'),
 			'request_date' : fields.datetime('Request Date'),
            'locationarea_id' : fields.many2one('dowfranchise.locationarea', 'Location area', ),
            'approval_ids': fields.one2many('dowfranchise.requestbase.approval', 'requestbase_id', 'Approvals'),            
            'stage_id': fields.selection([('draft', 'Draft'),('on going', 'On Going'),('declined', 'Declined'),('approved', 'Approved'),], 'Stage', default="draft", required=True),
        }

    def confirm_request(self, cr, uid, ids, model_id, context=None):
        return none

    def send_email(self, cr, uid, ids, model_id, context=None):
        return none

    def approve_request(self, cr, uid, ids, model_id, context=None):
        return none

    def decline_request(self, cr, uid, ids, model_id, context=None):
        return none

class dowfranchise_requestbase_approval(osv.Model):
    _name = 'dowfranchise.requestbase.approval'
    _description = 'Request Approval'    
    _columns = {
            'requestbase_id' : fields.many2one('dowfranchise.requestbase', 'Request Base', required=True),
 			'group_id' : fields.many2one('res.groups', 'Group'),
 			'approval_uid' : fields.many2one('res.users', 'Approval'),
 			'approval_date' : fields.datetime('Approval Date'),
            'status_id': fields.selection([('approved', 'Approved'),('declined', 'Declined'),], 'Status'),
            'comment' : fields.char('Comment', size=2000),
        }

class dowfranchise_requesttermination(osv.Model):
    _name = 'dowfranchise.requesttermination'
    _inherit = 'dowfranchise.requestbase'
    _description = 'Request Termination'
    _columns = {
            'legal_name' : fields.char('Legal Name', size=100, required=True),
            'partner_name' : fields.char('Partner Name', size=100, required=True),
            'businessline_ids' : fields.many2many('dowfranchise.businessline', 'dowfranchise_requesttermination_businessline_rel', 'requesttermination_id', 'businessline_id', string='Business Line'),
            'expected_termination_date' : fields.datetime('Expected Termination date', ),
            'reason_id' : fields.many2one('dowfranchise.terminationreason', 'Reason', ),
            'comment' : fields.char('Comment', size=2000),
            'proof_ids': fields.one2many('dowfranchise.requesttermination.proof', 'requesttermination_id', 'Proofs'),
        }

class dowfranchise_requesttermination_proof(osv.Model):
    _name = 'dowfranchise.requesttermination.proof'
    _description = 'Request Termination Proof'    
    _columns = {
            'requesttermination_id' : fields.many2one('dowfranchise.requesttermination', 'Request Termination', required=True),
        }

class dowfranchise_requestexpanding(dowfranchise_requestbase):

    _name = 'dowfranchise.requestexpanding'
    _description = 'Request Expanding'
    _columns = {
            'request_type': fields.selection([('new', 'New Franchise'),('replace', 'Replacement'),], 'Request Type', required=True, ),
            'expected_entry_date' : fields.datetime('Expected entry date', ),
            'proposal_area': fields.selection([('new', 'New'),('active', 'Active'),], 'Proposal Area', ),
        }

class dowfranchise_requestexpandinghf(dowfranchise_requestexpanding):

    _name = 'dowfranchise.requestexpandinghf'
    _description = 'Request Expanding HF'
    _columns = {
            'culture_ids' : fields.many2many('dowfranchise.culture', 'dowfranchise_requestexpandinghf_culture_rel', 'requestexpandinghf_id', 'culture_id', string='Business Line'),
        }

class dowfranchise_requestexpandingseed(dowfranchise_requestexpanding):

    _name = 'dowfranchise.requestexpandingseed'
    _description = 'Request Expanding Seed'
    _columns = {
            'businessline_ids' : fields.many2many('dowfranchise.businessline', 'dowfranchise_requestexpandingseed_businessline_rel', 'requestexpandingseed_id', 'businessline_id', string='Business Line'),
        }

class dowfranchise_requestexpandingpasture(dowfranchise_requestexpanding):

    _name = 'dowfranchise.requestexpandingpasture'
    _description = 'Request Expanding Pasture'

