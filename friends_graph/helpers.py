"""
Various helper functions

"""



def format_letter_node(letter):
    """ I take a single character and format it in thejit node style """
    u = {}
    u['id'] = "node_l_%s" % letter
    u['name'] = letter.upper()
    u['data'] = {}
    u['children'] = []
    return u    

def format_user_node(user):
    """ I take a Django user and format it in thejit node style """    
    
    name = user.get_full_name().strip()
    if not name:
        name = user.username
    
    u = {}
    u['id'] = "node_%s" % user.username
    u['name'] = name
    u['data'] = {}
    u['children'] = []
    return u