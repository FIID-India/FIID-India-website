/* GO TO TOP
-------------------------------------------------- */
var mybutton = document.getElementById("myBtn");

window.onscroll = function() {scrollFunction()};
function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

/* SCROLL OR REDIRECT ON CLICK
-------------------------------------------------- */
let ScrollToSection = (id, url) =>{
  if(!url){
    document.getElementById(id).scrollIntoView();
  }else{
    window.location.href=url+'#'+id;
  }
}
let RedirectTo = (url) => window.location.href=url;


/* REMOVING HASH SYMBOL FROM THE ADDRESS BAR
-------------------------------------------------- */
setTimeout(()=>{
  history.replaceState('', document.title, window.location.origin + window.location.pathname + window.location.search);
}, 10);