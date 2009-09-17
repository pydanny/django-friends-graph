
function init() {
 json = {{ json|safe }}

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