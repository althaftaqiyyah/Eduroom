let profileDropdownList = document.querySelector(".profile-dropdown-list");
let btn = document.querySelector(".profile-dropdown-btn");

let classList = profileDropdownList.classList;

const toggle = () => classList.toggle("active");

window.addEventListener("click", function (e) {
  if (!btn.contains(e.target)) classList.remove("active");
});

let slideIndex = 0;
const slider = document.querySelector('.slider');
const slides = document.querySelectorAll('.slider img');

function slide(direction) {
    slideIndex += direction;
    if (slideIndex >= slides.length) { slideIndex = 0; }
    if (slideIndex < 0) { slideIndex = slides.length - 1; }
    const newPosition = -slideIndex * 100; 
    slider.style.transform = `translateX(${newPosition}%)`; 
    updateButtonState();
}

function updateButtonState() {
    const prevButton = document.querySelector('.prev');
    const nextButton = document.querySelector('.next');
    prevButton.classList.remove('disabled');
    nextButton.classList.remove('disabled');
    if (slideIndex === 0) { prevButton.classList.add('disabled'); } 
    if (slideIndex === slides.length - 1) { nextButton.classList.add('disabled'); } 
}


function openPopup() {
    console.log("openPopup called");
    document.getElementById('popup').classList.add('open-popup');
    document.getElementById('overlay').classList.add('open-popup');
    clearForm(); // Clear the form fields when opening the popup
}

function closePopup() {
    console.log("closePopup called");
    document.getElementById('popup').classList.remove('open-popup');
    document.getElementById('overlay').classList.remove('open-popup');
}

/*document.addEventListener('DOMContentLoaded', (event) => {
    console.log("DOMContentLoaded event");
    // Event listener hanya didaftarkan sekali setelah DOM dimuat
    document.querySelector('.button-book').addEventListener('click', bookReservation);
    document.querySelector('.button-cancel').addEventListener('click', () => {
        closePopup();
        clearForm(); // Clear the form fields when cancelling the popup
    });
});*/

function clearForm() {
    console.log("clearForm called");
    document.getElementById("borrower_name").value = "";
    document.getElementById("email").value = "";
    document.getElementById("purpose").value = "";
    document.getElementById("start_date").value = "";
    document.getElementById("start_time").value = "";
    document.getElementById("end_date").value = "";
    document.getElementById("end_time").value = "";
}

function submitForm() {
    console.log("submitForm called");
    const table = document.getElementById("reservationTable").getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();

    const currentDate = new Date().toLocaleString();
    const reservationId = generateReservationId();
    const startTime = `${document.getElementById("start_date").value} ${document.getElementById("start_time").value}`;
    const endTime = `${document.getElementById("end_date").value} ${document.getElementById("end_time").value}`;
    const status = "Not yet confirmed";

    newRow.insertCell(0).textContent = currentDate;
    newRow.insertCell(1).textContent = reservationId;
    newRow.insertCell(2).textContent = startTime;
    newRow.insertCell(3).textContent = endTime;
    newRow.insertCell(4).textContent = status;
}

function bookReservation() {
    console.log("bookReservation called");
    const borrowerName = document.getElementById("borrower_name").value;
    const email = document.getElementById("email").value;
    const purpose = document.getElementById("purpose").value;
    const startDate = document.getElementById("start_date").value;
    const startTime = document.getElementById("start_time").value;
    const endDate = document.getElementById("end_date").value;
    const endTime = document.getElementById("end_time").value;

    if (borrowerName === "" || email === "" || purpose === "" || startDate === "" || startTime === "" || endDate === "" || endTime === "") {
        alert("Please fill in all fields before booking.");
    } else {
        submitForm();
        closePopup();
    }
}

function generateReservationId() {
    return 'RES' + Math.floor(Math.random() * 10000);
}

document.addEventListener('DOMContentLoaded', (event) => {
    // Any additional initialization if required
    console.log("Page loaded and DOMContentLoaded event fired");
});
