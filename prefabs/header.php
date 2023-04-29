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
        <img class="sidebar-indicator" src="../assets/logos/white_chevron_left.png">
        <div id="navigation">
            <div>
                <div id="nav_element">
                    <img src="../white_favicon.ico">
                    <h1>astatine.shop</h1>
                </div>
                <hr>
                <a href="index.php">
                    <div id="nav_element" aria-label="hoverable">
                        <img src="../assets/logos/search.png">
                        <h1>Cari</h1>
                    </div>
                </a>
                <hr>
                <div id="nav_element" aria-label="hoverable">
                    <img src="../assets/logos/heart_filled.png">
                    <h1>Pilihan diminati</h1>
                </div>
            </div>
            <div>
                <a href="login.php">
                    <div id="nav_element" aria-label="hoverable" onclick="logOut();">
                        <img src="../assets/logos/left_arrow.png">
                        <h1 style="color:#f9595f; font-weight:normal;">Log keluar</h1>
                    </div>
                </a>
                <?php
                    if ($user == 0) {
                        echo "<a href='login.php'><div id='nav_element' aria-label='hoverable' onclick='logOut();'><img src='../assets/logos/profile.png'><h1 id='signup'>Daftar akaun</h1></div></a>";
                    } else {
                        $source = $user["admin"] == 0 ? "profile" : "admin";
                        echo "<div id='nav_element'><img src='../assets/logos/{$source}.png'><h1>{$user['nama']}</h1></div>";
                    }
                ?>
            </div>
        </div>
    </div>
</div>