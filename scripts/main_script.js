// #region Prefabs
// JQuery 😎
$("#prefab_header").load('/prefabs/sidebar.php', function () {})
$("#prefab_login_popup").load('/prefabs/login_popup.html', function () {})
// #endregion

var opened = false;
var sidebarParent = undefined;

function onSidebarClick() {
    if (sidebarParent == undefined) {
        sidebarParent = document.getElementsByClassName("sidebar-parent")[0];
    }
    if (sidebarParent == undefined) {
        return;
    }

    opened = !opened;

    sidebarParent.id = opened ? "open" : "closed";

    if (sidebarParent.id == "closed") {
        return;
    }

    var slogans = [
        "Mencari CPU dari seluruh dunia",
        "Pilihan yang murah",
        "Ribuan CPU di hujung jari",
        "Mencari CPU yang teringin",
        "Buat perbandingan CPU lain"
    ];
    var current = document.getElementById("slogan").innerHTML;
    for (var i = 0; i <= 20; i++) {
        target = slogans[parseInt(Math.floor(Math.random() * slogans.length))];
        if (target == current) {
            continue;
        }
        document.getElementById("slogan").innerHTML = target;
        return;
    }
}

function logOut() {
    document.cookie = 'user_id=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/';
}

function toggleLoginPopup() {
    var popup = document.getElementById("login_popup");
    popup.ariaLabel = popup.ariaLabel == "active" ? "inactive" : "active";
}
