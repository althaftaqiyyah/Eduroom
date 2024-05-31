const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');
constmain = document.getElementById('main');

signUpButton.addEventListener('click', () => {
    main.classList.add("right-panel-active");
});
signInButton.addEventListener('click', () => {
    main.classList.remove("right-panel-active");
});

function validate() {
    const passwordInput = document.querySelector('input[name="pswd"]');
    const lengthError = document.getElementById('length');

    if (passwordInput.value.length >= 8) {
        lengthError.classList.remove('invalid');
        lengthError.classList.add('valid');
    } else {
        lengthError.classList.remove('valid');
        lengthError.classList.add('invalid');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const passwordInput = document.querySelector('input[name="pswd"]');
    passwordInput.addEventListener('input', validate);
});

function validatePassword() {
    const passwordInput = document.querySelector('input[name="pswd"]');
    const confirmPasswordInput = document.getElementById('confirmPassword');
    const lengthError = document.getElementById('length');
    const matchError = document.getElementById('match');

    // Check password length
    if (passwordInput.value.length >= 8) {
        lengthError.classList.remove('invalid');
        lengthError.classList.add('valid');
    } else {
        lengthError.classList.remove('valid');
        lengthError.classList.add('invalid');
    }

    // Check password match
    if (passwordInput.value === confirmPasswordInput.value) {
        matchError.classList.remove('invalid');
        matchError.classList.add('valid');
    } else {
        matchError.classList.remove('valid');
        matchError.classList.add('invalid');
    }
}

// Prevent form submission if passwords do not match
document.querySelector('form[action="#"]').addEventListener('submit', function(event) {
    const passwordInput = document.querySelector('input[name="pswd"]');
    const confirmPasswordInput = document.getElementById('confirmPassword');
    if (passwordInput.value !== confirmPasswordInput.value) {
        event.preventDefault(); // Prevent form submission
        alert('Passwords do not match');
    }
});


