<?php
$user = 0;
if (isset($_COOKIE["user_id"])) {
    $db = new mysqli($hostname='localhost', $username='astatine', $password='password', $database='astatine_data');

    foreach($db->query("SELECT * FROM `pelanggan` WHERE user_id = {$_COOKIE['user_id']}") as $row) {
        $user = $row;
    }
}
?>
<div class="sidebar-parent" id="closed">
    <div class="sidebar-toggle" onclick="onSidebarClick();"></div>
    <div id="background" onclick="onSidebarClick();"></div>
    <div class="sidebar">
        <img class="sidebar-indicator" src="/assets/logos/white_chevron_left.png">
        <div id="navigation">
            <div>
                <div id="nav_element">
                    <img src="/white_favicon.ico">
                    <h1>astatine.eshop</h1>
                </div>
                <h3 id="slogan">
                    Mencari CPU dari seluruh dunia
                </h3>
                <hr>
                <a href="/index.php">
                    <div id="nav_element" aria-label="hoverable">
                        <img src="/assets/logos/search.png">
                        <h1>Cari</h1>
                    </div>
                </a>
                <hr>
                <a href="/liked.php">
                    <div id="nav_element" aria-label="hoverable">
                        <img src="/assets/logos/heart_filled.png">
                        <h1>Pilihan diminati</h1>
                    </div>
                </a>
                <?php
                if (($user != 0) && ($user["admin"] == 1)) {
                    echo "
                    <a href='/admin/daftar.php'>
                        <hr>
                        <div id='nav_element' aria-label='hoverable'>
                            <img src='/assets/logos/tools.png'>
                            <h1>Daftar CPU</h1>
                        </div>
                    </a>";
                }
                ?>
            </div>
            <div>
                <div id="nav_element" aria-label="hoverable" onclick="colorTheme();onSidebarClick();" style="padding:calc(var(--sidebar-closed-width) * 0.25) !important;">
                    <img src="/assets/logos/color_wheel.png">
                    <h1>Tema warna</h1>
                </div>
                <a href="/login.php">
                    <div id="nav_element" aria-label="hoverable" onclick="logOut();">
                        <img src="/assets/logos/left_arrow.png">
                        <h1 style="color:#f9595f; font-weight:normal;">Log keluar</h1>
                    </div>
                </a>
                <?php
                    if ($user == 0) {
                        echo "<a href='/login.php'><div id='nav_element' aria-label='hoverable' onclick='logOut();'><img src='/assets/logos/profile.png'><h1 id='signup'>Daftar akaun</h1></div></a>";
                    } else {
                        $source = $user["admin"] == 1 ? "admin" : "profile";
                        echo "<div id='nav_element'><img src='/assets/logos/{$source}.png'><h1>{$user['nama']}</h1></div>";
                    }
                ?>
            </div>
        </div>
    </div>
    <div id="customize-menu_parent" style="display:none;justify-content:center;align-items:center;height:100vh;background:#0005;">
        <div class="customize-menu">
            <h1>Tema warna</h1>
            <div id="theme-container">
            </div>
            <div id="close-container">
                <h6 onclick="colorTheme()">Close</h6>
            </div>
        </div>
    </div>
</div>