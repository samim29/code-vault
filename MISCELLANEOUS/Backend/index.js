//requiring express
const express = require("express");
const app = express();
const port = 8080;

app.use(express.urlencoded({extended: true})); //parsing for post request

app.get("/register", (req,res) => {
    res.send("Standard GET response");
});

app.post("/register", (req,res) => {
    let {user, password} = req.body;
    res.send(`standard POST response. welcome ${user}`);
});

app.listen(port,() => {
    console.log(`Listening to port ${port}`);
});
