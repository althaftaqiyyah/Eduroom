document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const currentPassword = document.querySelector('#current-password');
    const newPassword = document.querySelector('#new-password');
    const repeatNewPassword = document.querySelector('#repeat-new-password');
    const saveChangesBtn = document.querySelector('.btn-a');

    const passwordErrors = document.querySelector('.errors');
    const lengthError = document.querySelector('#length');

    // Validate new password length
    newPassword.addEventListener('input', function() {
        if (newPassword.value.length < 8) {
            lengthError.classList.add('invalid');
            lengthError.classList.remove('valid');
        } else {
            lengthError.classList.remove('invalid');
            lengthError.classList.add('valid');
        }
    });

    // Validate form on submit
    saveChangesBtn.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Clear previous error messages
        passwordErrors.innerHTML = '';

        if (newPassword.value.length < 8) {
            alert('New password must be at least 8 characters long');
            return; // Stop execution if new password does not meet the criteria
        }

        if (newPassword.value !== repeatNewPassword.value) {
            alert('New password and repeat new password do not match');
            return; // Stop execution if new password does not match confirm password
        }

        // Perform your password update logic here
        // Example: Send a request to the server to update the password

        // Clear input fields after successful update
        currentPassword.value = '';
        newPassword.value = '';
        repeatNewPassword.value = '';

        // Show success message or perform other actions
        alert('Password successfully updated');
    });
});
