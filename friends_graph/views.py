import string

from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson

from friends.models import Friendship

from friends_graph.helpers import get_js

def friends_graph(request, username, template_name='friends_graph/friends_graph.html'):
    """ Render a thejit rgraph based on the user's friends  """
    
    user = get_object_or_404(User, username=username)    
        
    # Format the core user node
    data = format_user_node(user)
    
    # Save all the letters of the alphabet to a dict as formal thejit notes
    letters = {}
    for letter in string.ascii_lowercase:
        letters[letter] = format_letter_node(letter)
    
    # loop through all the friends of the user
    for element in Friendship.objects.friends_for_user(user):
        friend = element['friend']

        # Save the friend to the associated letter in the letters dictionary
        # TODO make this not an ugly long string
        letters[friend.username[0].lower()]['children'].append(format_user_node(friend))

    # loop through the letters.
    # only add those letters with nodes as children so we don't pollute the screen.
    for letter, ldata in letters.items():
        if not ldata['children']:
            continue
        
        data['children'].append(ldata)
        
    # jsonify the data
    data = simplejson.dumps(data)
        
    # stick it into our hardcoded JS
    # TODO make the JS just plain better. 
    data = get_js(data)
    
    return render_to_response(template_name, {
        "base_user": user,
        "data":data
    }, context_instance=RequestContext(request))    
    
    
