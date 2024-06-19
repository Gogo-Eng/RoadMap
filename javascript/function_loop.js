var time = 0;
var my_list = ['orange', 'apple', 'pawpaw']

while(time < 10)
{
    console.log('tried', time++)
}


console.log()
do {
    console.log('tried it', time++)
}while(time < 10)

console.log()

for (var time = 0; time < 10; time++)
{
    console.log('tried', time)   
}

console.log()

for (var time = 0; time < my_list.length; time ++)
{
    console.log('tried', my_list[time])
}