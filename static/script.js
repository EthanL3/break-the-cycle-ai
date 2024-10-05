document.addEventListener("DOMContentLoaded", function() {
    const formElement = document.getElementById('relapse-form');

    // Automatically submit the form to go to the next question
    formElement.addEventListener('submit', function(event) {
        event.preventDefault();
        formElement.submit();
    });
});