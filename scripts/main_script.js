// #region Prefabs
// JQuery 😎
$("#prefab_header").load('prefabs/header.php', function () {})
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
}

function logOut() {
    document.cookie = 'user_id=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/';
}
