"use strict";
var i = 999999; 
(function () //IIFE  this kind of function is called immediately invoked function expression
{
    for(var i = 0; i < 10; i++)
    {
        console.log(i)
    }
})()
console.log("after loop", i )