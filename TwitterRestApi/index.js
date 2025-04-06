//requiring express and setting port
const express = require("express");
const app = express();
const PORT = 8080;

// Importing UUID module for generating unique IDs
const { v4: uuidv4 } = require('uuid');
const methodOverride = require("method-override");
app.use(methodOverride("_method"));

//requiring path and setting view engine and path to render files
const path = require("path");
app.set("view engine","ejs");
app.set("views",path.join(__dirname,"/views"));

app.use(express.static(path.join(__dirname, "public"))); // Serving static files (CSS, JavaScript, images) from the 'public' directory
app.use(express.urlencoded({ extended: true})); // Middleware to parse incoming request bodies (form data from HTML forms)
//temporary databse .as we don,t have database we use array as jugadd.
let tweets = [
    {
        id: uuidv4(),
        username:"samim",
        content:"Hi,I am learning REST APIs"
    },
    {
        id: uuidv4(),
        username:"sadik",
        content:"Hi,I am learning CCT"
    },
    {
        id: uuidv4(),
        username:"sahil",
        content:"Hi,I am working as production manager"   
    }

];
// C = Create
//route to display the form for a new tweet
app.get("/tweets/new", (req,res) => {
    res.render("new.ejs");
});
 // Route to handle form submission for creating a new post
app.post("/tweet",(req,res) => {
    let {username,content} = req.body;
    let id =uuidv4();
    tweets.push({id,username,content});
    res.redirect("/tweets");

});

//U = Update
app.get("/tweets/:id/edit",(req,res) => {
    let {id} = req.params;
    let tweet = tweets.find((t) => id === t.id);
    // console.log("Requested ID:", id); //debugging
    // console.log("All Tweet IDs:", tweets.map(t => t.id));//debugging


    // console.log(tweet);
    res.render("edit.ejs",{tweet});
});

app.patch("/tweets/:id", (req,res) => {
    //we need the to find the post
    let {id} = req.params;
    let content = req.body.content;
    let tweet = tweets.find((t) => id ===t.id);
    tweet.content = content;
    res.redirect("/tweets");

});

//Delete the tweets

app.delete("/tweets/:id",(req,res) => {
    let {id} = req.params;
    tweets = tweets.filter((t) => id !== t.id);
    res.redirect("/tweets");
});

//view tweets(home page)(R =Read)
app.get("/tweets",(req,res) => {
    res.render("index.ejs",{tweets});
});







app.listen(PORT, () => {
    console.log(`Server is listening to port ${PORT}`);
});
