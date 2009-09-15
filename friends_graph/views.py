from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def friends_graph(request, username, template_name='friends_graph/friends_graph.html'):
    
    user = get_object_or_404(User, username=username)
    
    return render_to_response(template_name, {
        "user": user,
    }, context_instance=RequestContext(request))
upload = login_required(upload)    
    
    