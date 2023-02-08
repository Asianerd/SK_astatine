/*
id
name
description

price
stock
amount sold

thumbnail
images


*/

// class Item {
//     constructor(
//         id, name, description,
//         price, stock,
//         thumbnail, sold=0, images=[],
//         ) {

//         this.id = id;
//         this.name = name;
//         this.description = description;

//         this.price = price;
//         this.stock = stock;
//         this.sold = sold;

//         this.thumbnail = thumbnail;
//         this.images = images;
//     }

    
// }

const currencyFormatter = Intl.NumberFormat('en', {
    notation: 'standard',
    style: 'currency',
    currency: 'MYR'
});
const amountFormatter = Intl.NumberFormat('en', { notation: 'compact' } );

class Item {
    static collection = [];

    constructor (name, price, description, image_url, sold) {
        this.id = Item.collection.length;
        this.name = name;
        this.price = price;

        this.description = description;

        this.image_url = image_url
        this.sold = sold;
    }

    static initialize() {
        Item.collection.push(new Item("Gan11 M Duo", 214.49, "lorem ipsum dolor sit amet", "gan_duo.png", 117_314));
        Item.collection.push(new Item("Skullcandy", 580.64, "lorem ipsum dolor sit amet", "skullcandy.png", 54_091_102));
        Item.collection.push(new Item("Nothing Ear 1", 498, "lorem ipsum dolor sit amet", "nothing_ear.png", 351_933));
        Item.collection.push(new Item("GAN CUBE", 1000, "idk", "gan_duo.png", 1000));

        // fetch from sql here

        this.displayAll();
    }

    static displayAll() {
        Item.collection.forEach(element => {
            console.log(element.name);
        });
    }

    static push(id, object) {
        
    }

    static update(id, object) {

    }

    static fetch(id) {

    }

    fetchAsHTML() {
        return `<td><a href="#" class="entity"><img src="assets/sample-images/${this.image_url}"><div id="text-content"><h1>${this.name}</h1><hr><div id="price-info"><h2>${currencyFormatter.format(this.price)}</h2><h3>${amountFormatter.format(this.sold)} sold</h3></div><div id="star-container"><img src="assets/logos/star.png"><img src="assets/logos/star.png"><img src="assets/logos/star.png"><img src="assets/logos/star.png"><img src="assets/logos/unfilled_star.png"></div></div></a></td>`;
    }
}

class CPU_Item {
    static collection = [];

    constructor (name, price, cores, threads, base_freq, boosted_freq, interaction_count = 0) {
        this.id = CPU_Item.collection.length;
        this.name = name;

        this.cores = cores;
        this.threads = threads;
        this.base_frequency = base_freq;
        this.boosted_frequency = boosted_freq;

        this.price = price; // USD
        this.interaction_count = interaction_count;
    }

    static initialize() {
        CPU_Item.collection.push(new CPU_Item("Intel® Core™ i9-9900K Processor", 500, 8, 16, 3.6, 5));
        CPU_Item.collection.push(new CPU_Item("Intel® Core™ i3-10325 Processor", 169, 4, 8, 3.9, 4.7));
    }
}
