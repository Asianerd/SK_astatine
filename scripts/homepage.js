const currencyFormatter = Intl.NumberFormat('en', {
    notation: 'standard',
    style: 'currency',
    currency: 'MYR'
});

const amountFormatter = Intl.NumberFormat('en', { notation: 'compact' } );

const queryContainer = document.getElementsByClassName("query-result")[0];

var sortDirection = true;
const sortDirectionImg = document.querySelector("#sort-direction img");
const sortDirectionText = document.querySelector("#sort-direction h3");

const sortItems = document.querySelectorAll("#sort-types input");
var sortItemValue = 0;

const searchBar = document.querySelector("#content-parent #search-bar input");
const sliderData = {};
const sliderTexts = Array.from(document.getElementsByClassName("slider-text"));
var fullyInitialized = false;

function updateValues() {
    // if either left or right slider is updated, this function is called
    var ranges = this.parentNode.getElementsByTagName("input"); // get both sliders
    var start = parseFloat(ranges[0].value); // get slider values
    var end = parseFloat(ranges[1].value);
    if (start > end) {
        // 1, 0 -> 0, 1
        // 0, 1 -> 0, 1
        // from, to
        [start, end] = [end, start]; // swap values
    }
    sliderData[this.parentNode.id] = [start, end]; // update data

    if (fullyInitialized) {
        updateSliderText();
        updateEntityList();
    }
}

function updateSliderText() {
    sliderTexts[0].innerHTML = `${sliderData["core"][0]} - ${sliderData["core"][1]}`;
    sliderTexts[1].innerHTML = `${sliderData["frequency"][0].toFixed(1)}GHz - ${sliderData["frequency"][1].toFixed(1)}GHz`;
    sliderTexts[2].innerHTML = `${currencyFormatter.format(sliderData["price"][0])} - ${currencyFormatter.format(sliderData["price"][1])}`;
}

function updateEntityList() {
    var http = new XMLHttpRequest(); // create new http request
    http.onreadystatechange = function() {
        if ((this.readyState == 4) && (this.status == 200)) {
            // if there isnt any error from http, set the container innerhtml
            queryContainer.innerHTML = this.response;
        }
    }

    var args = "";

    for (const [key, value] of Object.entries(sliderData)) {
        // go through all the data entries and add to the arguments
        args += `&${key}-high=${value[1]}`;
        args += `&${key}-low=${value[0]}`;
    }

    args += `&sort=${sortItemValue}`;
    args += `&direction=${sortDirection ? 1 : -1}`;
    args += `&search_input=${searchBar.value}`;

    http.open("GET", `../server/fetch_cpu.php?request-mode=filtered&${args}`, true);
    http.send();
    // send it to the fetch_cpu.php file
}

window.onload = function(){
    // Initialize Sliders
    var rangeSections = Array.from(document.getElementsByClassName("slider-range")); // get all slider-range divs
    // also converts HTMLCollection/NodeList to array so that its iterable
    rangeSections.forEach(section => {
        sliders = Array.from(section.getElementsByTagName("input")); // fetch all range inputs in div
        sliders.forEach(element => {
            element.oninput = updateValues; // subscribe to function
            element.oninput(); // call for first update
        })
    });

    fullyInitialized = true;
    updateSliderText();
    updateEntityList();
    // update entity list
}

function sortDirectionClick() {
    sortDirection = !sortDirection;

    sortDirectionImg.id = sortDirection ? "ascending" : "descending";
    sortDirectionText.innerHTML = sortDirection ? "Menaik" : "Menurun";

    updateEntityList();
}

sortItems.forEach(element => {
    element.addEventListener('click', function() {
        sortItems.forEach(element => {
            element.checked = false;
            // set all the elements to unchecked
        })

        if (sortItemValue != element.value) {
            // if the current item value isnt the same, set to true
            element.checked = true;
            sortItemValue = element.value;
        } else {
            // else unselect all
            sortItemValue = 0;
        }

        updateEntityList();
    })
})

searchBar.addEventListener('input', updateEntityList)

// #region typing effect
// shamelessly stolen from https://codepen.io/gschier/pen/DLmXKJ
var TxtRotate = function(el, toRotate, period) {
    this.toRotate = toRotate;
    this.el = el;
    this.loopNum = 0;
    this.period = parseInt(period, 10) || 2000;
    this.txt = '';
    this.tick();
    this.isDeleting = false;
};

TxtRotate.prototype.tick = function() {
    var i = this.loopNum % this.toRotate.length;
    var fullTxt = this.toRotate[i];

    if (this.isDeleting) {
        this.txt = fullTxt.substring(0, this.txt.length - 1);
    } else {
        this.txt = fullTxt.substring(0, this.txt.length + 1);
    }

    this.el.placeholder = this.txt;

    var that = this;
    var delta = 150 - (Math.random() * 100);

    if (this.isDeleting) {
        delta *= 0.5;
    }

    if (!this.isDeleting && this.txt === fullTxt) {
        delta = this.period;
        this.isDeleting = true;
    } else if (this.isDeleting && this.txt === '') {
        this.isDeleting = false;
        this.loopNum++;
        delta = 500;
    }

    setTimeout(function() {
        that.tick();
    }, delta);
};

var elements = document.getElementsByClassName('typing-effect');
for (var i=0; i<elements.length; i++) {
    var toRotate = elements[i].getAttribute('data-rotate');
    var period = elements[i].getAttribute('data-period');
    if (toRotate) {
        new TxtRotate(elements[i], JSON.parse(toRotate), period);
    }
}
// #endregion
