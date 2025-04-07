// Import the 'mongoose' library to connect and interact with MongoDB
const mongoose = require('mongoose');

// Import the Chat model defined earlier (from './models/chat.js')
const Chat = require("./models/chat.js");

// Call the main() function to start the MongoDB connection
main()
  .then(() => {
    // This block runs if the connection to MongoDB is successful
    console.log("connection successful");
  })
  .catch(err => 
    // This block runs if there's an error during connection
    console.log(err)
  );

// Define an asynchronous function to connect to MongoDB
async function main() {
  // Connect to a local MongoDB database named 'whatsapp'
  await mongoose.connect('mongodb://127.0.0.1:27017/whatsapp');

  // If authentication is required in the database, you'd use the below format instead:
  // await mongoose.connect('mongodb://user:password@127.0.0.1:27017/whatsapp');
}

// Define an array of chat messages to insert into the database
let allChats = [
  {
    form: "neha",  // sender's name (should ideally be 'from')
    to: "priya",   // recipient's name
    msg: "send me your exam sheets",  // message content
    created_at: new Date()  // current timestamp
  },
  {
    form: "rohit",
    to: "sumit",
    msg: "all the best!",
    created_at: new Date()
  },
  {
    form: "amit",
    to: "sumit",
    msg: "steach me JS callbacks",  // minor typo: should be 'teach'
    created_at: new Date()
  },
  {
    form: "adam",
    to: "heve",  // minor typo: should be 'eve'?
    msg: "assalamuallaikum",
    created_at: new Date()
  },
  {
    form: "thor",
    to: "hulk",
    msg: "ready for a new fight",
    created_at: new Date()
  },
];

// Insert all the chat messages defined above into the 'chats' collection
// The Chat model handles creating the documents based on the schema
Chat.insertMany(allChats);
