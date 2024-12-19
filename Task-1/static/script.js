document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("pdfForm");
    const loadingMessage = document.getElementById("loading-message");
    const submitButton = document.getElementById("submitBtn");
    const errorMessage = document.getElementById("error-message");
    const fileInput = document.getElementById("file");
    const queryInput = document.getElementById("query");

    // Form submission
    form.addEventListener("submit", function (event) {
        errorMessage.style.display = "none";

        // Check if the file and query are provided
        if (!fileInput.files.length || !queryInput.value.trim()) {
            event.preventDefault(); // Prevent submission
            errorMessage.style.display = "block"; // Show error message
            return;
        }

        // Show loading message
        loadingMessage.style.display = "block";
        submitButton.disabled = true; // Disable the button during submission
    });

    // Hide the loading message on page load
    window.addEventListener("pageshow", function () {
        loadingMessage.style.display = "none";
        submitButton.disabled = false;
    });
});
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("pdfForm");
    const submitButton = document.getElementById("submitBtn");
    const buttonText = document.getElementById("buttonText");
    const spinner = document.getElementById("spinner");

    form.addEventListener("submit", function () {
        // Show spinner and change button text
        spinner.style.display = "block";
        buttonText.textContent = "Submitting...";
        submitButton.disabled = true; // Disable button during submission
    });

    // Hide the spinner on page load (after submission response)
    window.addEventListener("pageshow", function () {
        spinner.style.display = "none";
        buttonText.textContent = "Submit";
        submitButton.disabled = false;
    });
});
