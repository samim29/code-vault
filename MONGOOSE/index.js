// --- Import Mongoose ---
// Import the mongoose library to interact with MongoDB using an object data modeling (ODM) approach.
const mongoose = require('mongoose');


// --- Database Connection Setup ---

// Define an async function to connect to the MongoDB database
async function main() {
  // Connect to MongoDB running locally on the default port (27017) and using a database named 'test'
  await mongoose.connect('mongodb://127.0.0.1:27017/test');
}

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


// --- Define Schema ---

// Create a schema that defines the structure of documents in the collection
// A schema acts like a blueprint that enforces rules on the shape of the data
const userSchema = new mongoose.Schema({
  name: String,   // The user's name (string)
  email: String,  // The user's email (string)
  age: Number     // The user's age (number)
});


// --- Create Models ---

// Create a model named 'User' based on the userSchema
// A model allows us to interact with the 'users' collection in the database
const User = mongoose.model("User", userSchema);

// Create another model named 'Employee' using the same schema (optional)
// Even though the schema is the same, this will point to a different collection: 'employees'
// const Employee = mongoose.model("Employee", userSchema);


// --- Create and Save Documents ---

// Create a new instance of the User model with name, email, and age
// This does NOT save the data to the database yet; it only creates the object
// const user1 = new User({
//     name: "Adam",            // User's name
//     email: "adam@yahoo.in",  // User's email
//     age: 48                  // User's age
// });

// Save the user1 document to the MongoDB collection
// This will insert a new document in the 'users' collection
// user1.save();  // No .then/.catch used here, so any error won't be caught/displayed


// Create another user instance (like above) with different data
// const user2 = new User({
//     name: "Eve",
//     email: "eve@yahoo.in",
//     age: 48
// });

// Save the user2 document to the database with promise handling
// user2
//   .save()  // This returns a Promise
//   .then((res) => {
//       // If save is successful, log the saved document
//       console.log(res);
//   })
//   .catch((err) => {
//       // If there's an error during save (like validation or connection issue), log it
//       console.log(err);
//   });


// --- Retrieve Documents from the Database ---

// Use the .find() method to get all documents from the 'users' collection
// The empty object {} means "no filter", so it fetches everything
User.find({})
  .then((res) => {
    // If retrieval is successful, log the array of users
    console.log(res);
  })
  .catch((err) => {
    // If there's an error during retrieval, log the error
    console.log(err);
  });
