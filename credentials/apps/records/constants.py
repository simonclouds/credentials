WAFFLE_FLAG_RECORDS = 'student_records'
RECORDS_RATE_LIMIT = '15/m'  # This rate was arbitrarily chosen due to a lack of data.  It may need to be changed later.


class UserCreditPathwayStatus(object):
    """ Allowed values for UserCreditPathway.status """
    SENT = 'sent'
