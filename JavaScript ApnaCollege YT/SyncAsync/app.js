// ------------------------- setTimeout ------------------------- //

// A simple function that prints "hello"
function hello() {
    console.log("hello");
}

// setTimeout runs a function after a delay (in milliseconds)
// In this case, "hello" will be printed after 4 seconds
// setTimeout(hello, 4000);



// ------------------------- Promises ------------------------- //

// A promise represents the result of an asynchronous operation
// This Promise will log a message when it's created
// It can either be resolved (successful) or rejected (error)

// let promise = new Promise((resolve, reject) => {
//     console.log("I am a promise");

//     // Uncomment one of the below lines to simulate resolve/reject

//     // resolve(123); // When the operation succeeds
//     // reject("some error occurred"); // When it fails
// });



// ------------------------- async function ------------------------- //

// Declaring an async function. It always returns a Promise
async function hello() {
    console.log("hello");
    // You could return a value here, which becomes a resolved promise
    // return "Hello from async!";
}



// ------------------------- await keyword ------------------------- //

// A function that simulates an API call using a Promise and setTimeout
function api() {
    return new Promise((resolve, reject) => {
        // Simulate a 2-second delay like fetching data from a server
        setTimeout(() => {
            console.log("weather data"); // Log once data is 'fetched'
            resolve(200); // Send a fake success response (status code)
        }, 2000);
    });
}


// Using async/await to handle the above simulated API call

async function getWeatherdata() {
    // Wait until the first API call finishes
    await api(); // First API call - waits 2 seconds

    // Wait again for the second API call to finish
    await api(); // Second API call - waits another 2 seconds

    // Total time: 4 seconds for both to complete in sequence
}
