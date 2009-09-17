"""
Various helper functions

"""

js_base = """

function init() {
 json = {replace_me}

  //Create a new canvas instance.
  var canvas = new Canvas('mycanvas', {
    //Where to inject the canvas. Any div container will do.
    'injectInto':'infovis',
    //width and height for canvas. Default's to 200.
    'width': 900,
    'height':500
 });

  var rgraph= new RGraph(canvas,  {
    //interpolation type, can be linear or polar
    interpolation: 'linear',
    //parent-children distance
    levelDistance: 100,
    //Set node/edge styles
    //Node: {
    //  color: 'white'
    //},
    //Edge: {
    //  color: '#772277'
    //},
    //Add a controller to make the tree move on click.
     onCreateLabel: function(domElement, node) {  
       domElement.innerHTML = node.name;  
       domElement.onclick = function() {  
          rgraph.onClick(node.id);  
       };  
     }
   });

    //load tree from tree data.
    rgraph.loadJSON(json);
    //compute positions and plot
    rgraph.refresh();
}
"""

def get_js(json):
    """ This is an admittedly lame template function. """
    return js_base.replace('{replace_me}', json)


def format_letter_node(letter):
    """ I take a single character and format it in thejit node style """
    u = {}
    u['id'] = "node_l_%s" % letter
    u['name'] = letter.lower()
    u['data'] = {}
    u['children'] = []
    return u    

def format_user_node(user):
    """ I take a Django user name and format it in thejit node style """    
    
    name = user.get_full_name().strip()
    if not name:
        name = user.username
    
    u = {}
    u['id'] = "node_%s" % user.username
    u['name'] = name
    u['data'] = {}
    u['children'] = []
    return u