// --- Importing and Initializing Express --- //

// Require the express module (it's a function)
const express = require("express");

// Call the express function to create an Express application instance
const app = express();


// --- Server Setup --- //

let port = 3000; // Define which port your app will listen on

// Start the server and listen on the defined port
// This method handles incoming requests and activates the server
app.listen(port, () => {
    console.log(`app is listening on port ${port}`);
});


// --- Basic Route Handling --- //

// Handle GET request to the root URL (http://localhost:3000/)
app.get("/", (req, res) => {
    res.send("You contacted root path");
});


// --- Path Parameters --- //
// These are dynamic segments in the route URL, captured as variables

// Example: If user visits http://localhost:3000/john/123
// `username` will be "john", and `id` will be "123"
app.get("/:username/:id", (req, res) => {
    // Destructure path parameters from the request
    let { username, id } = req.params;

    // Log any query string params (like ?age=25) — not used here, but good for demo
    console.log(req.query);

    // Send a response using the dynamic username
    res.send(`You contacted parameter path @${username}`);
});


// -------------------- OPTIONAL / COMMENTED EXAMPLES -------------------- //

// Catch-all route: handles all unmatched GET requests
// Useful for custom 404 pages
// app.get("*", (req, res) => {
//     res.send("This path does not exist");
// });

// Handle POST requests to root (would only respond to POST, not GET)
// app.post("/", (req, res) => {
//     res.send("You made a POST request to the root");
// });


// --- Extra Example --- //
// Simple middleware-style response (responds to all requests regardless of method or route)
// app.use((req, res) => {
//     console.log("Request received");
//     res.send("Hello, I am a response from .use() middleware");
// });

