const express = require("express");
const app = express();

// app.use( (req,res,next) => {
//     console.log("Hi, I am middleware");
//     next();
// });

//Utility middleware logger

// app.use((req,res,next) => {
//     req.time =new Date(Date.now()).toString();
//     console.log(req.method,req.hostname,req.path, req.time);
//     next();
// })



//middleware with path
// app.use("/random", (req,res,next) => {
//     console.log("I am only for random");
//     next();
// });

//api token as query string

app.use("/api",(req,res,next) => {
    let {token} = req.query;
    if(token === "giveaccess"){
        next();
    }
    res.send("Access Denied!");
})

app.get("/api", (req,res) => {
    res.send("data");
})

app.get("/", (req, res) => {
    res.send("hi i am root");
});

app.get("/random", (req,res) => {
    res.send("this is a random page");
});

app.listen(8080,() => {
    console.log("server listening to port 8080");
});