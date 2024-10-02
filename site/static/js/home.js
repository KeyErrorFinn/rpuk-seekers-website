// Select the image element
const logo = document.getElementById('logo');
const lie = document.getElementById('lie');
const truth = document.getElementById('truth');

// Add event listeners for mouse hover
logo.addEventListener('mouseover', function() {
    document.body.style.backgroundColor = '#151515';  // Change body background color on hover
    lie.style.opacity = '0';
    truth.style.opacity = '1';
});

// Revert the background color on mouse out
logo.addEventListener('mouseout', function() {
    document.body.style.backgroundColor = '#868686';  // Revert to original background color
    lie.style.opacity = '1';
    truth.style.opacity = '0';
});