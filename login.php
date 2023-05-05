<?php

// declaring login statuses
enum loginStatus {
    case Unset;
    case Success;
    case UsernameNotFound;
    case IncorrectPassword;
    case FieldNotSet;
}

// set to unset first
$status = loginStatus::Unset;

if (isset($_POST["login_username"]) && isset($_POST["login_password"])) {
    // if username and password arent null
    $user_db = new mysqli($hostname='localhost', $username='astatine', $password='password', $database='astatine_data'); // login to database
    $result = $user_db->query("SELECT * FROM `pelanggan` WHERE username = '{$_POST["login_username"]}'"); // query data
    if ($result->num_rows >= 1) {
        // if more than one record exists
        foreach ($result as $x) {
            $user = $x;
            break;
            // yea, dumb, but faster way to fetch first element
        }
        $status = $user['kata_laluan'] == $_POST["login_password"] ? loginStatus::Success : loginStatus::IncorrectPassword;
    } else {
        // no record exists
        $status = loginStatus::UsernameNotFound;
    }
}

if ($status == loginStatus::Success) {
    // sets cookies with 1 day expiry
    setcookie("login_new", 0, time() + (86400 * 14), "/"); // index.php displays alert box if this is 0
    setcookie("login_username", $user['username'], time() + (86400 * 14), "/");
    setcookie("user_id", $user['user_id'], time() + (86400 * 14), "/");
    header("Location: ./index.php"); // redirects to index.php
    exit();
}

?>
<!DOCTYPE html>
<html>
    <head>
        <title>Astatine.eshop : Log masuk</title>
        <script type="text/javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <link rel="icon" type="image/x-icon" href="/favicon.ico">
        <link rel="stylesheet" href="./styles/style.css">
        <link rel="stylesheet" href="./styles/login.css">
    </head>
    <body>
        <div style="position:absolute; top:0; left:0; height:100vh; width:100vw; padding:0; margin:0; display:flex; justify-content:center; align-items:center;">
            <div class="parent">
                <h1>
                    astatine.eshop
                </h1>
                <h2 id="status">
                    <?php
                    if ($status == loginStatus::UsernameNotFound) {
                        echo "Username \"{$_POST['login_username']}\" tidak wujud.";
                    } else if ($status == loginStatus::IncorrectPassword) {
                        echo "Kata laluan anda tidak tepat.";
                    }
                    ?>
                </h2>
                <form class="form" action="login.php" method="post" autocomplete="on">
                    <div id="fields">
                        <h2>Username : </h2>
                        <input placeholder="Username" type="text" name="login_username" required="" oninvalid="this.setCustomValidity('Username wajib diisi.')" oninput="setCustomValidity('')">
                        <h2>Kata laluan : </h2>
                        <input placeholder="Kata laluan" type="password" name="login_password" required="" oninvalid="this.setCustomValidity('Kata laluan wajib diisi.')" oninput="setCustomValidity('')" autocomplete="on">
                    </div>
                    <a id="signup" href="/signup.php">
                        Tiada akaun? Daftar akaun baharu di sini.
                    </a>
                    <input id="submit" type="submit" value="Log masuk">
                </form>
            </div>
        </div>
        <script src="./scripts/main_script.js"></script>
    </body>
</html>