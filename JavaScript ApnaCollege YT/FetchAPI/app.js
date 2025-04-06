// --- API URL from which we will fetch random cat facts --- //
const URL = "https://cat-fact.herokuapp.com/facts";


// --- Using async/await to fetch data --- //

const getFacts = async () => {
    // Print a message indicating that data fetching has started
    console.log("getting data..");

    // Wait for the fetch request to complete (fetch returns a Promise)
    let response = await fetch(URL);

    // Log the raw response object (includes headers, status code, etc.)
    console.log(response); // This will be a Response object in JSON format

    // Parse the JSON body from the response so it becomes a usable JavaScript object
    let data = await response.json();

    // Log the final parsed data (which is an array of cat facts)
    console.log(data);
};


// --- Alternate Version: Using Promises (.then) instead of async/await --- //

// function getFacts() {
//     // Make the fetch request (returns a Promise)
//     fetch(URL)
//         .then((response) => {
//             // Convert the response to JSON
//             return response.json();
//         })
//         .then((data) => {
//             // Log the parsed data (cat facts)
//             console.log(data);
//         });
// }
