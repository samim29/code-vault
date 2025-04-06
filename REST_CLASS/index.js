const express = require("express"); // Importing the Express module to create and configure a web server
const app = express(); // Initializing the Express application
const port = 8080; // Defining the port number on which the server will listen for requests
const path = require("path"); // Importing the Path module to work with file and directory paths
const { v4: uuidv4 } = require('uuid'); // Importing UUID module for generating unique IDs
const methodOverride = require("method-override");
app.use(express.urlencoded({ extended: true })); // Middleware to parse incoming request bodies (form data from HTML forms)
app.use(methodOverride("_method"));
app.set("view engine", "ejs"); // Setting EJS as the template/view engine for rendering dynamic HTML files
app.set("views", path.join(__dirname, "/views")); // Defining the directory where EJS template files are stored

app.use(express.static(path.join(__dirname, "public"))); // Serving static files (CSS, JavaScript, images) from the 'public' directory

let posts = [ // Temporary array to store post data (acting as a simple in-memory database)
    { id: uuidv4(), username: "apnacollege", content: "I love coding!" },
    { id: uuidv4(), username: "shradhakhapra", content: "Hard work is important to achieve success." },
    { id: uuidv4(), username: "rahulkumar", content: "I got selected for my first internship!" }
];

// Route to display all posts (renders 'index.ejs' and passes the posts array)
app.get("/posts", (req, res) => {
     res.render("index.ejs", { posts });
}); 

// Route to display the form for creating a new post (renders 'new.ejs')
app.get("/posts/new", (req, res) => { 
    res.render("new.ejs"); 
}); 

app.post("/post", (req, res) => { // Route to handle form submission for creating a new post
   let { username, content } = req.body; // Extracts 'username' and 'content' from the request body
   let id = uuidv4();
   posts.push({ id, username, content }); // Adds new post to 'posts' array
   res.redirect("/posts"); // Redirects to the posts page
});

app.get("/posts/:id", (req, res) => { // Route to access a specific post by ID
    let { id } = req.params;
    let post = posts.find((p) => id === p.id);
    res.render("show.ejs", { post });
});


app.get("/posts/:id/edit",(req,res) => {
    let { id } = req.params;
    let post = posts.find((p) => id === p.id);
    res.render("edit.ejs",{post});   
});


app.patch("/posts/:id",(req,res) =>{// Route to update a specific post by ID
    let {id} =req.params;
    let newContent = req.body.content;
    let post = posts.find((p) => id === p.id);
    post.content=newContent;
    res.redirect("/posts");
});

app.delete("/posts/:id",(req,res) => {
    let {id} =req.params;
    posts = posts.filter((p) => id!==p.id);
    res.redirect("/posts");
})

// Starting the server and listening on the specified port
app.listen(port, () => { 
    console.log(`Server is running and listening on port: ${port}`); 
}); 
