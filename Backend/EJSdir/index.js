// --- Import Required Modules --- //

// Import the express module (used to create web servers and handle routes)
const express = require("express");
const app = express(); // Initialize express app

// Import path module (used to handle and transform file paths)
const path = require("path");

// Define the port number your server will listen on
const port = 8080;


// --- Middleware Setup --- //

// Serve static files (like CSS, JS, images) from the 'public' folder
// This allows you to use files from "public/" directly in your EJS views (e.g., <link href="/style.css">)
app.use(express.static(path.join(__dirname, "public")));


// --- EJS Configuration --- //

// Set EJS as the view engine (to render dynamic HTML pages)
app.set("view engine", "ejs");

// Set the path to the 'views' folder where your EJS templates are located
app.set("views", path.join(__dirname, "/views"));


// --- Routes --- //

// Root route - when user visits http://localhost:8080/
// Render the "home.ejs" template from the "views" folder
app.get("/", (req, res) => {
    res.render("home.ejs");
});


// Dice rolling route - when user visits http://localhost:8080/rolldice
// Randomly generate a number between 1 and 6 and send it to the view
app.get("/rolldice", (req, res) => {
    let num = Math.floor(Math.random() * 6) + 1; // Random number between 1–6
    res.render("rolldice.ejs", { diceVal: num }); // Pass the number to the template
});


// Instagram-style profile route using dynamic routing
// When user visits something like /ig/adam or /ig/steve
app.get("/ig/:username", (req, res) => {
    let { username } = req.params; // Extract the dynamic segment from URL

    // Load data from a local JSON file (like a mock database)
    const instaData = require("./data.json");

    // Try to get the specific user's data using the username from the JSON object
    const data = instaData[username];

    // If user data exists, render the template and pass the data object
    if (data) {
        res.render("instragram.ejs", { data });
    } else {
        // If username doesn't exist in data.json, show an error page
        res.render("error.ejs");
    }
});


// --- Start the Server --- //

app.listen(port, () => {
    console.log(`listening on port ${port}`);
});
