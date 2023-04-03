// #region Prefabs
// JQuery 😎
$("#prefab_header").load('prefabs/header.php', function () {})
// #endregion

// #region Visuals
var navbar = 0;

var scrollAmount = 0;
var _previousScroll = 0;

onscroll = function () {
    if (navbar == 0) {
        navbar = document.getElementsByClassName("nav-bar")[0];
    }

    scrollAmount = this.scrollY - _previousScroll;
    _previousScroll = this.scrollY;

    // navbar.style.height = scrollAmount > 0 ? "0vh" : "10vh";
}
// #endregion
