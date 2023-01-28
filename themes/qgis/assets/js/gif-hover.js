/* 
  Hover handler for static image to gif
  Code courtesy of 
   https://codereview.stackexchange.com/a/277669
*/
document.querySelectorAll('.is-gif-hover').forEach(element => {
    element.addEventListener('mouseenter', event => {
      var uri = element.style.backgroundImage.slice(4, -1).replace(/["']/g, "");
      uri = uri.replace(/\.png$/, '.gif');
      element.style.backgroundImage = "url(" + uri + ")"
    })
  
    element.addEventListener('mouseleave', event => {
      var uri = element.style.backgroundImage.slice(4, -1).replace(/["']/g, "");
      uri = uri.replace(/\.gif$/, '.png');
      element.style.backgroundImage = "url(" + uri + ")"
    })
  });

