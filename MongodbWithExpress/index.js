const express = require("express");
const app = express();
let port = 8080;
const path = require("path");

const Chat = require("./models/chat.js");
app.set("views", path.join(__dirname,"views"));
app.set("view engine","ejs");
app.use(express.static(path.join(__dirname,"public")));
app.use(express.urlencoded({extended:true}))
const methodOverride = require('method-override');
app.use(methodOverride('_method'));

const mongoose = require('mongoose');


 // Call the main function and handle connection success or failure
main()
.then(() => {
  // This will run if the connection is successful
  console.log("connection successful");
})
.catch(err => 
  // This will run if there's an error while connecting
  console.log(err)
);

async function main() {
  await mongoose.connect('mongodb://127.0.0.1:27017/whatsapp');

  // use `await mongoose.connect('mongodb://user:password@127.0.0.1:27017/test');` if your database has auth enabled
}


//Index Route
app.get("/chats",async (req,res) => {
  let chats = await Chat.find();
  // console.log(chats);
  res.render("index.ejs",{ chats });
})

//New Route
app.get("/chats/new",(req,res) => {
  res.render("new.ejs");
});

//create route

app.post("/chats",(req,res) => {
  let {form,msg,to} = req.body;
  let newChat = new Chat({
    form: form,
    to: to,
    msg: msg,
    created_at: new Date()
  });
  newChat.save()
  .then((res) => {
    console.log("chat was saved");
  })
  .catch((err) => {
    console.log(err);
  });
  res.redirect("/chats");
})

//Edit Route
app.get("/chats/:id/edit",async(req,res) => {
  let {id} = req.params;
  let chat = await Chat.findById(id);
  res.render("edit.ejs",{chat});
});

//Update route
app.put("/chats/:id",async(req,res) => {
  let {id} = req.params;
  let {msg:newMsg} = req.body;
  let updatedchat = await Chat.findByIdAndUpdate(id,{msg:newMsg},{runValidators:true,new:true});
  console.log(updatedchat);
  res.redirect("/chats");
})

//DELETE route
app.delete("/chats/:id",async (req,res) => {
  let {id} = req.params;
  let deletedChat = await Chat.findByIdAndDelete(id);
  console.log(deletedChat);
  res.redirect("/chats");
})

//Home Page
app.get("/", (req,res) => {
    res.send("root is working");
});


app.listen(port,() => {
    console.log("server is listening onport 8080");
});

