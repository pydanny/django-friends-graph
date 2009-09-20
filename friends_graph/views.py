import string


from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.utils import simplejson

from friends.models import Friendship

from friends_graph.helpers import format_letter_node, format_user_node

def make_graph(user):
        
    # Format the core user node
    data = format_user_node(user)
    
    # Save all the letters of the alphabet to a dict as formal thejit notes
    letters = {}
    for letter in string.ascii_uppercase:
        letters[letter] = format_letter_node(letter)
    
    # loop through all the friends of the user
    for element in Friendship.objects.friends_for_user(user):
        friend = element['friend']

        # Save the friend to the associated letter in the letters dictionary
        # TODO make this not an ugly long string
        letters[friend.username[0].upper()]['children'].append(format_user_node(friend))

    # loop through the letters.
    # only add those letters with nodes as children so we don't pollute the screen.
    for letter, ldata in letters.items():
        if not ldata['children']:
            continue
        
        data['children'].append(ldata)
        
    return data

def get_js(json, template_name='friends_graph/friends_graph.js'):
    """ Render the in page javascript """
    
    template = get_template(template_name)
    c = Context({'json': json})
    return template.render(c)

def friends_graph(request, username, template_name='friends_graph/friends_graph.html'):
    """ Render a thejit rgraph based on the user's friends  """
    
    user = get_object_or_404(User, username=username)    
    
    data = make_graph(user)
        
    # jsonify the data
    data = simplejson.dumps(data)
        
    # stick it into our custom written JS templates
    friends_graph_js = get_js(data)
    
    return render_to_response(template_name, {
        "base_user": user,
        "friends_graph_js":friends_graph_js
    }, context_instance=RequestContext(request))    
    
    
def friends_graph_508(request, username, template_name='friends_graph/friends_graph_508.html'):
    
    user = get_object_or_404(User, username=username)    
    
    data = make_graph(user)    
    
    return render_to_response(template_name, {
        "base_user": user,
        "friends_graph_data": data
    }, context_instance=RequestContext(request))    
    