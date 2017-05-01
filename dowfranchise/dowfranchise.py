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
            'penalty' : fields.char('Penalty', size=100, required=True),
            'deadline' : fields.char('Deadline', size=100, required=True),
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

class dowfranchise_request(osv.Model):
    _name = 'dowfranchise.request'
    _description = 'Request'
    _columns = {
            'name' : fields.char('Name', size=100, required=True),
 			'request_uid' : fields.many2one('res.users', 'Requested by'),
 			'request_date' : fields.date('Request Date'),
            'approval_ids': fields.one2many('dowfranchise.request.approval', 'request_id', 'Approvals'),            
            'stage_id': fields.selection([('draft', 'Draft'),('ongoing', 'On Going'),('declined', 'Declined'),('approved', 'Approved'),], 'Stage', default="draft", required=True),
        }

    def confirm_request(self, cr, uid, ids, model_id, context=None):
        return none

    def send_email(self, cr, uid, ids, model_id, context=None):
        return none

    def approve_request(self, cr, uid, ids, model_id, context=None):
        return none

    def decline_request(self, cr, uid, ids, model_id, context=None):
        return none

class dowfranchise_request_approval(osv.Model):
    _name = 'dowfranchise.request.approval'
    _description = 'Request Approval'    
    _columns = {
            'request_id' : fields.many2one('dowfranchise.request', 'Request', required=True),
 			'group_id' : fields.many2one('res.groups', 'Group'),
 			'approval_uid' : fields.many2one('res.users', 'Approval'),
 			'approval_date' : fields.date('Approval Date'),
            'status_id': fields.selection([('approved', 'Approved'),('declined', 'Declined'),], 'Status'),
            'comment' : fields.text('Comment', ),
        }

class dowfranchise_requesttermination(osv.Model):
    _name = 'dowfranchise.requesttermination'
    _inherits = {'dowfranchise.request': 'request_id'}
    _description = 'Request Termination'
    _columns = {
            'request_id' : fields.many2one('dowfranchise.request', 'Request', required=True),
            'legal_name' : fields.char('Legal Name', size=100, required=True),
            'partner_name' : fields.char('Partner Name', size=100, required=True),
            'locationarea_id' : fields.many2one('dowfranchise.locationarea', 'Location area', ),
            'businessline_ids' : fields.many2many('dowfranchise.businessline', 'dowfranchise_requesttermination_businessline_rel', 'requesttermination_id', 'businessline_id', string='Business Line'),
            'franchisemanager_uid' : fields.many2one('res.users', 'Franchise Manager'),
            'expected_termination_date' : fields.date('Expected Termination date', ),
            'reason_id' : fields.many2one('dowfranchise.terminationreason', 'Reason', ),
            'reason_comment' : fields.text('Reason Comment', ),
            'proof_ids': fields.one2many('dowfranchise.request.proof', 'requesttermination_id', 'Proofs'),
            'meeting_date' : fields.date('Meeting date', ),
            'attended_uids' : fields.many2many('res.users', 'dowfranchise_requesttermination_users_rel', 'requesttermination_id', 'user_id', string='Meeting Attended'),
            'meeting_summary' : fields.text('Meeting Summary', ),
            'legal_comment' : fields.text('Legal Comment', ),

        }

class dowfranchise_request_proof(osv.Model):
    _name = 'dowfranchise.request.proof'
    _description = 'Request Termination Proof'    
    _columns = {
            'requesttermination_id' : fields.many2one('dowfranchise.requesttermination', 'Request Termination', required=True),
            'name' : fields.char('Name', size=100),
        }
