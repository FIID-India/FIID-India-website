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