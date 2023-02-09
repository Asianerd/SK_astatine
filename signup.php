<?php

enum signupStatus {
    case Unset;
    case Success;

    case UsernameOccupied;
}

$status = signupStatus::Unset;

if (isset($_POST["signup_name"]) &&
    isset($_POST["signup_username"]) &&
    isset($_POST["signup_password"]) &&
    isset($_POST["signup_confirm_password"])) {
    $user_db = new mysqli($hostname='localhost', $username='astatine', $password='temp', $database='astatine_data');
    $result = $user_db->query("SELECT * FROM `user` WHERE username = '{$_POST["signup_username"]}'");
    $current_user_id = ($user_db->query("SELECT * FROM `user`")->num_rows) + 1;

    if ($result->num_rows >= 1) {
        $status = signupStatus::UsernameOccupied;
    } else {
        // add user to database
        $status = signupStatus::Success;
    }
}

if ($status == signupStatus::Success) {
    setcookie("login_new", 0, time() + (86400 * 14), "/"); // index.php displays alert box if this is 0
    setcookie("login_username", $_POST["signup_username"], time() + (86400 * 14), "/");
    setcookie("user_id", $current_user_id, time() + (86400 * 14), "/");
    header("Location: ./index.php");
    exit();
}

?>
<!DOCTYPE html>
<html>
    <head>
        <title>Astatine.shop : Sign up</title>
        <script type="text/javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <link rel="icon" type="image/x-icon" href="/favicon.ico">
        <link rel="stylesheet" href="./styles/style.css">
        <link rel="stylesheet" href="./styles/login.css">
    </head>
    <body>
        <div style="height:100vh; width:100vw; padding:0; margin:0; display:flex; justify-content:center; align-items:center;">
            <div class="parent signup">
                <h1>
                    astatine.shop
                </h1>
                <h2 id="status">
                    <?php
                    if ($status == signupStatus::UsernameOccupied) {
                        echo "The username \"{$_POST['signup_username']}\" is already taken.";
                    }
                    ?>
                </h2>
                <form class="login" action="signup.php" method="POST" autocomplete="on" onsubmit="return validateForm();">
                    <div id="fields">
                        <h2>Name : </h2>
                        <input class="signup_inputField" id="signup_name" type="text" name="signup_name" required="">
                        <h2>Username : </h2>
                        <input class="signup_inputField" id="signup_username" type="text" name="signup_username" required="">
                        <!-- Add show password button? -->
                        <h2>Password : </h2>
                        <input class="signup_inputField" id="signup_password" type="password" name="signup_password" autocomplete="on" required="">
                        <h2>Confirm password : </h2>
                        <input class="signup_inputField" id="signup_confirm_password" type="password" name="signup_confirm_password" autocomplete="on" required="">
                    </div>
                    <a id="login" href="/login.php">
                        Back to login
                    </a>
                    <input id="submit" type="submit" value="Sign up">
                </form>
            </div>
        </div>

        <script src="./scripts/main_script.js"></script>
        <script src="./scripts/signup.js"></script>
    </body>
</html>