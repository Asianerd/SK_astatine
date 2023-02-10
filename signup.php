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

    if ($result->num_rows >= 1) {
        $status = signupStatus::UsernameOccupied;
    } else {
        /* finds new user id
         * if 0, 1, 2, 4, 5, then new user id is 3 (because database skipped a number, 3)
         * if 0, 1, 2, 3, then new user id is 4
         * 
         * situation 1:
         *  current_user_id, user_id
         *  1, 1
         *  2, 2
         *  3, 3
         *  4, 5 -> if both values arent the same, that means one user_id is missing
         *  
         *  found = true
         * if !found, so nothing happens
         * new user id is 4
         * 
         * situation 2:
         *  1, 1
         *  2, 2
         *  3, 3
         *  4, 4
         *  5, 5
         *  6, 6
         *  (list ends)
         * 
         * (found = false)
         * if !found, then current_user_id -> 6 + 1 = 7
         * new user id is 7
         */
        $current_user_id = 0;
        $found = false;
        foreach ($user_db->query("SELECT user_id FROM `user`") as $rows) {
            $current = (int)$rows["user_id"];
            $current_user_id++;

            if ($current != $current_user_id) {
                $found = true;
                break;
            }
        };
        if (!$found) {
            $current_user_id++;
        }

        $user_db->query("INSERT INTO `user` (user_id, name, username, password)
            VALUES ({$current_user_id}, \"{$_POST["signup_name"]}\", \"{$_POST["signup_username"]}\", \"{$_POST["signup_password"]}\")");
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
                        <input class="signup_inputField" id="signup_name" type="text" name="signup_name">
                        <h2>Username : </h2>
                        <input class="signup_inputField" id="signup_username" type="text" name="signup_username">
                        <!-- Add show password button? -->
                        <h2>Password : </h2>
                        <div id="password_criteria">
                            <input class="signup_inputField" id="signup_password" type="password" name="signup_password" autocomplete="on" onkeyup="onPasswordUpdate();">
                            <div>
                                <img src="./assets/logos/cross.png">
                                <h3>between 4-8 characters</h3>
                                <img src="./assets/logos/cross.png">
                                <h3>must have at least one uppercase letter</h3>
                                <img src="./assets/logos/check.png">
                                <h3>must have at least one lowercase letter</h3>
                                <img src="./assets/logos/check.png">
                                <h3>must have at least one number</h3>
                                <img src="./assets/logos/check.png">
                                <h3>must have at least one special character</h3>
                                <img src="./assets/logos/check.png">
                                <h3>must not include spaces</h3>
                            </div>
                        </div>
                        <h2>Confirm password : </h2>
                        <input class="signup_inputField" id="signup_confirm_password" type="password" name="signup_confirm_password" autocomplete="on">
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