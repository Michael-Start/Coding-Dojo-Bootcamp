// var pie1 = {
//         crust: "deep dish",
//         cheese: "mozzarella",
//         toppings: ["sausage", "peporoni"],
//         sauce: "traditional",
//         pizzaOven: function () {
//             console.log( "The crust is "    + this.crust);
//             console.log( "The sauce is "    +this.sauce)
//             console.log( "The cheese is "   + this.cheese);
//             console.log( "The toppings are "+ this.toppings);
//         }
//     }
// pie1.pizzaOven();

// var pie2 = {
//     crust: "hand tossed",
//     sauce: "marinara",
//     cheese: ['mozzarella', ' feta'],
//     toppings: ["mushrooms", " olives", " onions"],
//     pizzaOven: function () {
//         console.log( "The crust is "    + this.crust);
//         console.log( "The sauce is "    +this.sauce)
//         console.log( "The cheese is "   + this.cheese);
//         console.log( "The toppings are "+ this.toppings);
//     }

// }

// pie2.pizzaOven()

// var pie3 = {
//     crust: "thin crust",
//     sauce: "alfredo",
//     cheese: "mozzarella",
//     toppings: ["chicken", " green peppers", " bacon"],
//     pizzaOven: function () {
//         console.log( "The crust is "    + this.crust);
//         console.log( "The sauce is "    +this.sauce)
//         console.log( "The cheese is "   + this.cheese);
//         console.log( "The toppings are "+ this.toppings);
//     }
// }

// pie3.pizzaOven()

// var pie4 = {
//     crust:"crispy",
//     sauce:"bbq",
//     cheese:["chedder", " blue cheese"],
//     toppings:["buffolo chicken", " red peppers"],
//     pizzaOven: function () {
//         console.log( "The crust is "    + this.crust);
//         console.log( "The sauce is "    +this.sauce)
//         console.log( "The cheese is "   + this.cheese);
//         console.log( "The toppings are "+ this.toppings);
//     }
// }

// pie4.pizzaOven();

var randoPie = {
    crust: Math.floor((Math.random()* crust.length-1) +0)[" crispy", " thin crust", " traditional", " deep dish"],
    sauce: [" bbq", " traditional", " alfredo", " marinara"],
    cheese: [" chedder", " blue cheese", " mozarella", " feta"],
    toppings: [" buffolo chicken", " red peppers", " chicken", " green peppers", " mushrooms", " olives", " onions", " peporoni", " sausage"],
    randomPizza: function(){ 
        console.log( "The crust is "    + this.crust);
        console.log( "The sauce is "    + this.sauce)
        console.log( "The cheese is "   + this.cheese);
        console.log( "The toppings are "+ this.toppings);
        console.log(Math.random())
    }
}

randoPie.randomPizza()
