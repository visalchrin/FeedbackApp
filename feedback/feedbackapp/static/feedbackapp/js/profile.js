const personalForm = document.getElementById("personalForm"),
    profileForm = document.getElementById("profileForm"),
    changeProfileBtn = document.getElementById("changeProfile");


// change profile btn
changeProfileBtn.addEventListener("click", ()=>{
  console.log("change profile btn is clicked");
  overlay.style.display = "block";
  profileForm.style.display = 'grid';
  
});

// close-icon
closeBtn.forEach((button) => {
  button.addEventListener("click", ()=>{
    // overlay.style.display = "none";
    // loginForm.style.display = "none";
    // registerForm.style.display = "none";
    // personal form close
    personalForm.style.display = 'none';
    // profile form close 
    profileForm.style.display = 'none';
  });
});