const hamburger = document.getElementById("hamburger"),
    loginBtn = document.querySelectorAll(".loginBtn"),
    loginForm = document.getElementById("loginForm"),
    mobile = document.getElementById("mobile"),
    registerForm = document.getElementById("registerForm"),
    registerBtn = document.getElementById("register"),
    overlay = document.getElementById("overlay"), 
    closeBtn = document.querySelectorAll(".close-icon"),
    notification = document.getElementById("notification"),
    alertBtn = document.querySelector(".alert");
  
// hamburger button handle
hamburger.addEventListener('click', ()=>{
  console.log("hamburger clicked");
  if (mobile.style.display === "inline-block") {
    mobile.style.display = "none";
    overlay.style.display = "none";
  } else {
    mobile.style.display = "inline-block";
    overlay.style.display = "block";
  }
});


alertBtn.addEventListener("click", ()=>{
  console.log("Alert button is clicked");
  notification.style.display = "grid";
  overlay.style.display = "block";
});

// show edit personal form
function showEditPersonal() {
  console.log("edit personal is clicked");
  overlay.style.display = "block";
  personalForm.style.display = 'grid';
  return false;
}

// show login form
function showLoginForm() {
  // scroll back to top
  window.scrollTo(0, 0);

  mobile.style.display = "none";
  registerForm.style.display = "none";
  overlay.style.display = "block";
  console.log("Login button clicked");
    loginForm.style.display = "grid";
    return false;
}

// close notification
function closeNotification() {
  notification.style.display = "none";
  overlay.style.display = "none";

  return false;
}

// show Register Form 
function showRegisterForm() {
  // scroll back to top
  window.scrollTo(0, 0);
  
  loginForm.style.display = "none";
  overlay.style.display = "block";
  console.log("register Btn is clicked");
  registerForm.style.display = "grid";
  return false;
}

// close-icon
closeBtn.forEach((button) => {
  button.addEventListener("click", ()=>{
    overlay.style.display = "none";
    loginForm.style.display = "none";
    registerForm.style.display = "none";
  });
});

