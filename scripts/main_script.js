// $("#prefab_header").load('/prefabs/sidebar.php', function () {})
// $("#prefab_login_popup").load('/prefabs/login_popup.html', function () {})

var root = document.querySelector(':root');
var colorThemes = [
    {
        "name": "Material",
        "palette": {
            "primary": "13191f",
            "secondary": "262d37",
            "tertiary": "3970ff"
        },
        "font-color":"ffffff"
    },
    {
        "name": "Dracula",
        "palette": {
            "primary": "191a21",
            "secondary": "282a36",
            "tertiary": "ff79c6"
        },
        "font-color":"ffffff"
    },
    {
        "name": "Catppuccin",
        "palette": {
            "primary": "181825",
            "secondary": "302d41",
            "tertiary": "c9cbff"
        },
        "font-color":"ffffff"
    },
    {
        "name": "Cyberpunk",
        "palette": {
            "primary": "111111",
            "secondary": "222222",
            "tertiary": "fcee0c"
        },
        "font-color":"ffffff"
    },
]

var opened = false;
var sidebarParent = undefined;
var customizeMenuParent = undefined;

function fetchCookie(name) {
    var result = undefined;
    document.cookie.split(';').forEach(element => {
        let x = element.trim().split("=");
        if (x[0] == name) {
            console.log(x[x.length - 1]);
            result = x[x.length - 1];
        }
    });
    return result;
}

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

function colorTheme() {
    if (customizeMenuParent == undefined) {
        customizeMenuParent = document.getElementById("customize-menu_parent");
    }

    customizeMenuParent.style.display = customizeMenuParent.style.display == "flex" ? "none" : "flex";
}

function colorThemeUpdate() {
    if (fetchCookie('color_theme_index') === undefined) {
        return;
    }
    for (const [key, value] of Object.entries(colorThemes[parseInt(fetchCookie('color_theme_index'))]["palette"])) {
        root.style.setProperty(`--background-${key}`, `#${value}`);
    };
}

function colorThemeChange(index) {
    document.cookie = `color_theme_index=${index}; expires=Mon, 01 Jan 2030 00:00:00 UTC; path=/`;
    colorThemeUpdate();
}

function initializeColorThemes() {
    var themeContainer = document.querySelector(".customize-menu #theme-container");
    if (themeContainer == null) {
        return;
    }
    themeContainer.innerHTML = "";
    var i = 0;
    colorThemes.forEach(element => {
        themeContainer.innerHTML += `<h2 onclick="colorThemeChange(${i})" style="background-color:#${element['palette']['tertiary']} !important;">${element['name']}</h2>`;
        i++;
    });
}

initializeColorThemes();
colorThemeUpdate();
