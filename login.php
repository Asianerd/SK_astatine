<?php

enum loginStatus {
    case Unset;
    case Success;
    case UsernameNotFound;
    case IncorrectPassword;
    case FieldNotSet;
}

$status = loginStatus::Unset;

if (isset($_POST["login_username"]) && isset($_POST["login_password"])) {
    $user_db = new mysqli($hostname='localhost', $username='astatine', $password='temp', $database='astatine_data');
    $result = $user_db->query("SELECT * FROM `user` WHERE username = '{$_POST["login_username"]}'");
    if ($result->num_rows >= 1) {
        foreach ($result as $x) {
            $user = $x;
            break;
            // yea, dumb, but faster way to fetch first element
        }
        $status = $user['password'] == $_POST["login_password"] ? loginStatus::Success : loginStatus::IncorrectPassword;
    } else {
        $status = loginStatus::UsernameNotFound;
    }
}

if ($status == loginStatus::Success) {
    setcookie("login_new", 0, time() + (86400 * 14), "/"); // index.php displays alert box if this is 0
    setcookie("login_username", $user['username'], time() + (86400 * 14), "/");
    setcookie("user_id", $user['user_id'], time() + (86400 * 14), "/");
    header("Location: ./index.php");
    exit();
}

?>
<!DOCTYPE html>
<html>
    <head>
        <title>Astatine.shop : Login</title>
        <script type="text/javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <link rel="icon" type="image/x-icon" href="/favicon.ico">
        <link rel="stylesheet" href="./styles/style.css">
        <link rel="stylesheet" href="./styles/login.css">
    </head>
    <body>
        <div style="position:absolute; top:0; left:0; height:100vh; width:100vw; padding:0; margin:0; display:flex; justify-content:center; align-items:center;">
            <div class="parent">
                <h1>
                    astatine.shop
                </h1>
                <h2 id="status">
                    <?php
                    if ($status == loginStatus::UsernameNotFound) {
                        echo "The username \"{$_POST['login_username']}\" does not exist.";
                    } else if ($status == loginStatus::IncorrectPassword) {
                        echo "Your password was incorrect.";
                    }
                    ?>
                </h2>
                <form class="login" action="login.php" method="post" autocomplete="on">
                    <div id="fields">
                        <h2>Username : </h2>
                        <input type="text" name="login_username" required="" oninvalid="this.setCustomValidity('Your username is required.')" oninput="setCustomValidity('')">
                        <h2>Password : </h2>
                        <input type="password" name="login_password" required="" oninvalid="this.setCustomValidity('Your password is required.')" oninput="setCustomValidity('')" autocomplete="on">
                    </div>
                    <a id="signup" href="/signup.php">
                        Don't have an account? Create one here.
                    </a>
                    <input id="submit" type="submit" value="Log in">
                </form>
            </div>
        </div>
        <script src="./scripts/main_script.js"></script>
    </body>
</html>