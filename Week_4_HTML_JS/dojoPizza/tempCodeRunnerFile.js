var crust = [
    "deep dish",
    "hand tossed",
    "thin crust",
    "gluten free"
]

var sauce = [
    "traditional",
    "marinara",
    "alfredo",
    "bbq"
]

var cheese = [
    "mozzarella",
    "chedder",
    "provalone",
    "vegan"
]

var toppings = [
    "pepperoni",
    "sausage",
    "bell peppers",
    "chicken",
    "bacon"
]

function chooser(arr) {
    var i = Math.floor(arr.length * Math.random());
    return arr[i];
}

function randomPizza(){
    var pizza = {};
        pizza.crust = chooser(crust);
        pizza.sauce = chooser(sauce);
        pizza.cheese = chooser(cheese);
        pizza.toppings = chooser(toppings);
        return pizza;
        console.log(pizza)
    
}

console.log(randomPizza());