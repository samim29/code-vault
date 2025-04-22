const express = require("express");
const app = express();
const ExpressError = require("./ExpressError");
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
    throw new ExpressError(401,"Access Denied!");
})



app.get("/err", (req,res,) => {
    abcd = abcd;
})

app.use((err, req, res, next) => {
    console.log(err);
    next(err);
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