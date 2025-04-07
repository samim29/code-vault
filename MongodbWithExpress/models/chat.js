// Importing the 'mongoose' library to interact with MongoDB easily
const mongoose = require("mongoose");

// Defining a schema (structure) for the chat messages using Mongoose
// This helps us enforce rules on how a chat document should look in the database
const chatSchema = new mongoose.Schema({
    // 'form' (likely meant to be 'from') stores the sender's identifier (like user ID or username)
    // It is required, so MongoDB won't save a document without this field
    form: {
        type: String,
        required: true,
    },
    // 'to' stores the recipient's identifier
    // Also required
    to: {
        type: String,
        required: true,
    },
    // msg holds the actual message content
    // It can store up to 50 characters max
    msg: {
        type: String,
        maxLength: 50,
    },
    // 'created_at' stores the timestamp when the message was created
    // This is useful for ordering or filtering messages by time
    created_at: {
        type: Date,
        required: true,
    },
});

// Creating a model called 'Chat' based on the 'chatSchema'
// This model will be used to interact with the 'chats' collection in MongoDB
const Chat = mongoose.model("Chat", chatSchema);

// Exporting the Chat model so it can be used in other files (e.g., to create, read, or delete chat messages)
module.exports = Chat;


