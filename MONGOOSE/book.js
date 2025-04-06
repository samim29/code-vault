// --- Import Mongoose ---
// Import the mongoose library to interact with MongoDB using an object data modeling (ODM) approach.
const mongoose = require('mongoose');


// --- Database Connection Setup ---

// Define an async function to connect to the MongoDB database
async function main() {
  // Connect to a local MongoDB database named 'Amazon'
  // '127.0.0.1' refers to localhost and 27017 is the default MongoDB port
  await mongoose.connect('mongodb://127.0.0.1:27017/Amazon');
}

// Call the connection function and handle success/failure using Promises
main()
  .then(() => {
    // Runs when connection is successful
    console.log("connection successful");
  })
  .catch(err => 
    // Runs if there's an error while connecting
    console.log(err)
  );


// --- Define Schema ---

// A schema defines the structure of the documents in a MongoDB collection
// It acts like a template or blueprint for the data
const bookSchema = new mongoose.Schema({
  title: {
    type: String,     // The title should be a string
    required: true    // The title field is required; it must be provided
  },
  author: {
    type: String      // The author name is also a string
  },
  price: {
    type: Number      // Price should be a number
  }
});


// --- Create Model ---

// A model is created based on the schema and represents a collection in MongoDB
// In this case, 'Book' model will interact with the 'books' collection in the database
const Book = mongoose.model("Book", bookSchema);


// --- Create and Save a Document ---

// Create a new book object using the Book model
// This only creates the object in memory, it doesn't save it to the database yet
let book1 = new Book({
  title: "Mathematics XII",  // Book title (required)
  author: "RD Sharma",       // Author name (optional)
  price: 1200                // Price of the book
});

// Save the book1 document to the database
// This returns a Promise, so we use .then() to handle success and .catch() for errors
book1.save()
  .then(res => {
    // If save is successful, log the saved book document
    console.log(res);
  })
  .catch(err => {
    // If an error occurs during saving (e.g., validation fails), log the error
    console.log(err);
  });
