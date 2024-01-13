function validateRecruiterLogin() {
    // Replace these with your actual stored email and password for recruiters
    const recruiterStoredEmail = "recruiter@example.com";
    const recruiterStoredPassword = "recruiter123";

    // Get recruiter's entered email and password
    const email = document.getElementById('recruiter-email').value;
    const password = document.getElementById('recruiter-password').value;

    // Check if input matches stored credentials
    if (email === recruiterStoredEmail && password === recruiterStoredPassword) {
        alert("Recruiter Login successful!");
        // Redirect to the recruiter.html page or any other page you desire
        window.location.href = 'recruiter.html';
    } else {
        alert("Invalid credentials. Please try again.");
    }
}
