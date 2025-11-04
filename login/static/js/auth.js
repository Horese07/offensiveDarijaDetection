document.getElementById("show-signup").addEventListener("click", function(event) {
    event.preventDefault();
    document.querySelector(".form-container").classList.add("hidden");
    document.querySelectorAll(".form-container")[1].classList.remove("hidden");
});

document.getElementById("show-login").addEventListener("click", function(event) {
    event.preventDefault();
    document.querySelector(".form-container").classList.remove("hidden");
    document.querySelectorAll(".form-container")[1].classList.add("hidden");
});
