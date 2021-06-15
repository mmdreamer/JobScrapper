
window.onload = function() {
  var btnTop = document.getElementById("btnTop");

  window.onscroll = function() {scrollFunction()};

  function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
      btnTop.style.display = "block";
    } else {
      btnTop.style.display = "none";
    }
  }

 
};
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}