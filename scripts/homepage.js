const currencyFormatter = Intl.NumberFormat('en', {
    notation: 'standard',
    style: 'currency',
    currency: 'MYR'
});

const amountFormatter = Intl.NumberFormat('en', { notation: 'compact' } );

const itemContainer = document.getElementsByClassName("item-container")[0];

var sortDirection = true;
const sortDirectionImg = document.querySelector("#sort-direction img");
const sortDirectionText = document.querySelector("#sort-direction h3");

const sortItems = document.querySelectorAll("#sort-types input");
var sortItemValue = 0;

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
    var http = new XMLHttpRequest();
    http.onreadystatechange = function() {
        if ((this.readyState == 4) && (this.status == 200)) {
            itemContainer.innerHTML = this.response;
        }
    }

    var args = "";

    for (const [key, value] of Object.entries(sliderData)) {
        args += `&${key}-high=${value[1]}`;
        args += `&${key}-low=${value[0]}`;
    }

    args += `&sort=${sortItemValue}`;
    args += `&direction=${sortDirection ? 1 : -1}`;

    http.open("GET", `../server/fetch_cpu.php?${args}`, true);
    http.send();
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
}

function sortDirectionClick() {
    sortDirection = !sortDirection;

    sortDirectionImg.id = sortDirection ? "ascending" : "descending";
    sortDirectionText.innerHTML = sortDirection ? "Ascending" : "Descending";

    updateEntityList();
}

sortItems.forEach(element => {
    element.addEventListener('click', function() {
        sortItems.forEach(element => {
            element.checked = false;
        })

        if (sortItemValue != element.value) {
            element.checked = true;
            sortItemValue = element.value;
        } else {
            sortItemValue = 0;
        }

        updateEntityList();
    })
})