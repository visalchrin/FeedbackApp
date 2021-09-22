const feedbackBtn = document.querySelectorAll(".FeedbackBtn"),
      feedbackForm = document.querySelectorAll(".feedback__form");

// feedback click
feedbackBtn.forEach((button)=>{
  button.addEventListener("click", (event) => {
    const courseId = event.target.getAttribute('data-courseId');
    console.log(courseId);
    console.log("Feedback is clicked");
    const feedback = document.getElementById(`${courseId}`);
      console.log(feedback);
    feedback.style.display = "grid";
    overlay.style.display = "block";
  });
});


// close Btn click
closeBtn.forEach((button) => {
  button.addEventListener("click", ()=>{
    overlay.style.display = "none";

    // close all feedback forms
    feedbackForm.forEach((form) => {
      form.style.display = "none";
    });
  });
});