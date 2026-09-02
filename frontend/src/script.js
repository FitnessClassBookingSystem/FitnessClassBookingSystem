const signupForm = document.getElementById("#signup-form");

signupForm.addEventListener("submit", async(event) => {
    event.preventDefault();
    const userData = {
        username: document.getElementById("username").value,
        email: document.getElementById("email").value,
        password: document.getElementById("password").value,
    };

    try{
        const response = await fetch("/api/users", {})
    }
})