// --- Selecting Elements from the DOM --- //

// Select the button element with ID "toggler"
let btn = document.querySelector("#toggler");

// Select the <body> element of the HTML page
let body = document.querySelector("body");

// Set a variable to keep track of the current mode (light or dark)
let currMode = "light";


// --- Toggle Dark/Light Mode on Button Click --- //

// Add a click event listener to the button
btn.addEventListener("click", () => {
    
    // Check the current mode
    if (currMode === "light") {
        // If current mode is light, change to dark
        currMode = "dark";

        // Change the background color to black
        body.style.backgroundColor = "black";

        // Change button text to "Light Mode" so user knows they can switch back
        btn.innerText = "Light Mode";
        
    } else {
        // If current mode is dark, change to light
        currMode = "light";

        // Change the background color to white
        body.style.backgroundColor = "white";

        // Change button text to "Dark Mode"
        btn.innerText = "Dark Mode";
    }
});
