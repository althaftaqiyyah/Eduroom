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
    document.getElementById('popup').classList.add('open-popup');
    document.getElementById('overlay').classList.add('open-popup');
}

function closePopup() {
    document.getElementById('popup').classList.remove('open-popup');
    document.getElementById('overlay').classList.remove('open-popup');
}

document.querySelector('.button-book').addEventListener('click', closePopup);
document.querySelector('.button-cancel').addEventListener('click', closePopup);


document.getElementById('start_time').addEventListener('input', calculateDuration);
document.getElementById('end_time').addEventListener('input', calculateDuration);


function AddRow() {
    // Function to add row to the table or handle form submission
    console.log("Add button clicked");
}


function submitForm() {
    const reservationId = document.getElementById("reservation_id").value;
    const borrowerName = document.getElementById("borrower_name").value;
    const email = document.getElementById("email").value;
    const purpose = document.getElementById("purpose").value;
    const startDate = document.getElementById("start_date").value;
    const startTime = document.getElementById("start_time").value;
    const endDate = document.getElementById("end_date").value;
    const endTime = document.getElementById("end_time").value;

    if (!reservationId || !borrowerName || !email || !purpose || !startDate || !startTime || !endDate || !endTime) {
        alert("Please fill in all fields.");
        return;
    }

    const bookingTime = new Date().toLocaleString();
    const startDateTime = new Date(startDate + 'T' + startTime);
    const endDateTime = new Date(endDate + 'T' + endTime);
    const totalDuration = ((endDateTime - startDateTime) / (1000 * 60 * 60)).toFixed(2) + ' hours';

    const table = document.getElementById("reservationTable").getElementsByTagName("tbody")[0];
    const newRow = table.insertRow();

    newRow.insertCell(0).textContent = bookingTime;
    newRow.insertCell(1).textContent = reservationId;
    newRow.insertCell(2).textContent = startDate + ' ' + startTime;
    newRow.insertCell(3).textContent = endDate + ' ' + endTime;
    newRow.insertCell(4).textContent = "in line";

    closePopup();
}


document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById("reservation_id").value = generateReservationId();
});

function generateReservationId() {
    return 'RES' + Math.floor(Math.random() * 10000);
}


