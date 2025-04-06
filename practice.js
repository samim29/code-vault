var createCounter = function(n) {
    
    return function() {
        var temp = n;
        n = n + 1;
        console.log(temp);
        return;
    };
};


 const counter = createCounter(10)
  counter() // 10
  counter() // 11
  counter() // 12
 