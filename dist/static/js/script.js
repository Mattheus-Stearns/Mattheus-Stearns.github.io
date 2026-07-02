//This code is so that the navigation bar "sticks" to the top of the website when you scroll down

var sticky;

window.addEventListener('DOMContentLoaded', (event) => {
  var navbar = document.getElementById("navbar");
  if (navbar) {
    sticky = navbar.offsetTop;
    window.onscroll = function() {myFunction()};
  }
});

function myFunction() {
  var navbar = document.getElementById("navbar"); // Fetch navbar element inside the function
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}


document.addEventListener('DOMContentLoaded', function() {
    var coll = document.getElementsByClassName('collapsible');
    var i;
  
    for (i = 0; i < coll.length; i++) {
      coll[i].addEventListener('click', function() {
        var content = this.nextElementSibling;
        if (content.style.display === 'block') {
          content.style.display = 'none';
        } else {
          content.style.display = 'block';
        }
      });
    }
});
  

