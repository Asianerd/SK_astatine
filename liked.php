<!DOCTYPE html>
<html>
    <head>
        <title>Pilihan diminati</title>
        <link rel="icon" type="image/x-icon" href="/favicon.ico">
        <link rel="stylesheet" href="./styles/style.css">
        <link rel="stylesheet" href="./styles/homepage.css">
        <link rel="stylesheet" href="./styles/liked.css">
        <?php

        if (isset($_COOKIE["login_new"]) && ($_COOKIE["login_new"] <= 0)) {
            if ($_COOKIE['login_new'] == 0) {
                echo "<script>alert(\"Berjaya log masuk dengan akaun '{$_COOKIE["login_username"]}'.\")</script>";
            } else {
                echo "<script>alert(\"Berjaya daftar masuk akaun baharu '{$_COOKIE["login_username"]}'.\")</script>";
            }
            setcookie("login_new", 1, time() + (86400 * 14), "/"); // after alert, increment so it doesnt alert again
        }

        // require __DIR__ . '/client/CPU.php'; // import cpu class

        // Item::initialize();
        // initialized twice, once here and another in fetch_cpu but thats fine

        ?>
    </head>
    <body>
        <?php include './prefabs/sidebar.php'; ?>
        <?php include './prefabs/login_popup.html'; ?>
        <div id="title">
            <h1>Pilihan diminati</h1>
            <hr>
            <hr>
        </div>
        <div class="query-result">
            
        </div>
        <script src="./scripts/main_script.js"></script>
        <script src="./scripts/liked.js"></script>
        <script src="./scripts/entity_events.js"></script>
    </body>
</html>