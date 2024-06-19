"use strict";
const i = 999999; 
(function () //IIFE  this kind of function is called immediately invoked function expression
{
    for(let i = 0; i < 10; i++)
    {
        console.log(i)
    }
})()
if (true)
{
    let i = 88888
    console.log("after loop", i )
}
