// Importing required libraries
const { faker } = require('@faker-js/faker'); // For generating fake user data
const mysql = require('mysql2'); // MySQL driver for Node.js
const express = require("express"); // Web framework for building server
const app = express(); // Initializing express application
const path = require("path"); // Built-in Node.js module to work with file paths
const { v4: uuidv4 } = require('uuid'); // For generating unique user IDs
const methodOverride = require("method-override"); // Allows using PUT/PATCH/DELETE via POST method

// Middleware to parse incoming form data
app.use(express.urlencoded({ extended: true }));

// Enable method override for supporting PATCH/DELETE in HTML forms
app.use(methodOverride("_method"));

// Set view engine to EJS for rendering dynamic HTML pages
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "/views")); // Set views directory path

const port = 8080; // Define port for the server

// --- MySQL Database Connection Setup ---
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  database: 'delta_app',
  password: 'Samim@123'
});

// -------------------- ROUTES -------------------- //

// Home Route
app.get("/", (req, res) => {
  let q = `SELECT count(*) FROM user`; // Query to get total number of users

  try {
    connection.query(q, (err, result) => {
      if (err) throw err;
      let count = result[0]["count(*)"]; // Extracting the count from result
      res.render("home.ejs", { count }); // Render home page with user count
    });
  } catch (err) {
    console.log(err);
    res.send("Some error in DB");
  }
});

// Show All Users Route
app.get("/user", (req, res) => {
  let q = `SELECT * FROM user`; // Query to fetch all users

  try {
    connection.query(q, (err, users) => {
      if (err) throw err;
      res.render("showusers.ejs", { users }); // Render user list page
    });
  } catch (err) {
    console.log(err);
    res.send("Some error in DB");
  }
});

// Edit User Form Route
app.get("/user/:id/edit", (req, res) => {
  let { id } = req.params;
  let q = `SELECT * FROM user WHERE id='${id}'`; // Fetch user data for editing

  try {
    connection.query(q, (err, result) => {
      if (err) throw err;
      let user = result[0];
      res.render("edit.ejs", { user }); // Render edit form with user data
    });
  } catch (err) {
    console.log(err);
    res.send("Some error in DB");
  }
});

// Update Username Route
app.patch("/user/:id", (req, res) => {
  let { id } = req.params;
  let { password: formPass, username: newUsername } = req.body;

  let q = `SELECT * FROM user WHERE id='${id}'`; // Get user by ID

  try {
    connection.query(q, (err, result) => {
      if (err) throw err;
      let user = result[0];

      // Check if entered password matches the current user's password
      if (formPass != user.password) {
        res.send("wrong password");
      } else {
        let q2 = `UPDATE user SET username="${newUsername}" WHERE id="${id}"`; // Update username
        try {
          connection.query(q2, (err, result) => {
            if (err) throw err;
            res.send(result); // Respond with result (can be changed to redirect or message)
          });
        } catch (err) {
          console.log(err);
        }
      }
    });
  } catch (err) {
    console.log(err);
    res.send("Some error in DB");
  }
});

// Delete User Route
app.delete("/user/:id", (req, res) => {
  let { id } = req.params;
  const { password } = req.body;

  if (!password) {
    res.send("Password Required");
    return;
  }

  let q4 = `SELECT * FROM user WHERE id='${id}'`; // Get user by ID
  try {
    connection.query(q4, (err, result) => {
      if (err) throw err;
      let user = result[0];

      if (user.password !== password) {
        res.send("Incorrect password.");
      } else {
        let q5 = `DELETE FROM user WHERE id = "${id}"`; // Delete user query
        try {
          connection.query(q5, (err, result) => {
            if (err) throw err;
            res.redirect("/user"); // Redirect to user list after deletion
          });
        } catch (err) {
          console.log(err);
        }
      }
    });
  } catch (err) {
    console.log(err);
  }
});

// Add New User Form Route
app.get("/newuser", (req, res) => {
  res.render("newuser.ejs"); // Render form for new user
});

// Create New User Route
app.post("/newuser", (req, res) => {
  let { username: formuser, email: formemail, password: formpassword } = req.body;
  const id = uuidv4(); // Generate unique ID for new user

  const q3 = `INSERT INTO user (id, username, email, password) VALUES (?, ?, ?, ?)`;
  const values = [id, formuser, formemail, formpassword];

  try {
    connection.query(q3, values, (err, result) => {
      if (err) throw err;
      res.redirect("/user"); // Redirect to user list after successful insertion
    });
  } catch (err) {
    console.log(err);
    res.send("Some error in DB");
  }
});

// Start the server on specified port
app.listen(port, () => {
  console.log(`listening to port ${port}`);
});
