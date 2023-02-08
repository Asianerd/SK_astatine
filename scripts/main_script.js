// #region General usage
const currencyFormatter = Intl.NumberFormat('en', {
    notation: 'standard',
    style: 'currency',
    currency: 'MYR'
});
const amountFormatter = Intl.NumberFormat('en', { notation: 'compact' } );
// #endregion

// #region Prefabs
// JQuery 😎
// run when document finishes loading
// $(document).ready(function() {
//     User.initialize();
// })

$("#prefab_header").load('prefabs/header.php', function () {})

$('#prefab_item_filter').load('prefabs/item_filter.html', function () {
    itemFilterElement = document.getElementsByClassName("item-filter")[0];
    itemFilterButton = document.getElementById("toggle-button-image");

    itemFilterEnabled = false;
    updateItemFilter();
})
// #endregion

// #region Visuals
var itemFilterEnabled = false;
var itemFilterElement;
var itemFilterButton;

var navbar = 0;

var scrollAmount = 0;
var _previousScroll = 0;

onscroll = function () {
    if (navbar == 0) {
        navbar = document.getElementsByClassName("nav-bar")[0];
    }

    scrollAmount = this.scrollY - _previousScroll;
    _previousScroll = this.scrollY;

    navbar.style.height = scrollAmount > 0 ? "0vh" : "10vh";
}

function toggleItemFilter() {
    itemFilterEnabled = !itemFilterEnabled;
    updateItemFilter();
}

function updateItemFilter() {
    if (!itemFilterEnabled) {
        itemFilterElement.style.left = "-400px";
        itemFilterButton.src = "/assets/logos/search.png";
        itemFilterButton.style.transform = "rotate(0deg)";
    } else {
        itemFilterElement.style.left = "0px";
        itemFilterButton.src = "/assets/logos/left_chevron.png";
        itemFilterButton.style.transform = "rotate(360deg)";
    }
}
// #endregion
