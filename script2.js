window.addEventListener("scroll", function(){
  var header = document.querySelector("header");
  header.classList.toggle("sticky", window.scrollY > 0);
});

function toggleMenu(){
  let menuToggle = document.querySelector(".toggle");
  let menu = document.querySelector(".menu");
  menuToggle.classList.toggle("active");
  menu.classList.toggle("active");

};

window.addEventListener("onclick", function() {
  let imagesDisplay = document.getElementById("img-display");
  imagesDisplay.setAttribute("href", "img1");
  return false;
});