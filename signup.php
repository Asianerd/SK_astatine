<?php

// declares signup states
enum signupStatus {
    case Unset;
    case Success;

    case UsernameOccupied;
}

// sets to unset first
$status = signupStatus::Unset;

if (isset($_POST["signup_name"]) &&
    isset($_POST["signup_username"]) &&
    isset($_POST["signup_password"]) &&
    isset($_POST["signup_confirm_password"])) {
    // if name, username, password and confirm password arent null
    $user_db = new mysqli($hostname='localhost', $username='astatine', $password='password', $database='astatine_data'); // login to database
    $result = $user_db->query("SELECT * FROM `pelanggan` WHERE username = '{$_POST["signup_username"]}'"); // querys data

    if ($result->num_rows >= 1) {
        // if more than one record exists
        // dont let them sign up, the username is already taken
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
        foreach ($user_db->query("SELECT user_id FROM `pelanggan`") as $rows) { // queries all users
            $current = (int)$rows["user_id"]; // $current = user's id
            $current_user_id++; // increments $current_user_id

            if ($current != $current_user_id) {
                // refer to the algorithm above
                $found = true;
                break;
            }
        };
        if (!$found) {
            $current_user_id++;
        }

        // adds new user into database
        $user_db->query("INSERT INTO `pelanggan` (user_id, nama, username, kata_laluan, admin)
            VALUES ({$current_user_id}, \"{$_POST["signup_name"]}\", \"{$_POST["signup_username"]}\", \"{$_POST["signup_password"]}\", 0)");
        $status = signupStatus::Success;
    }
}

if ($status == signupStatus::Success) {
    // sets cookies with 1 day expiry
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
        <title>Astatine.eshop : Daftar akaun</title>
        <script type="text/javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <link rel="icon" type="image/x-icon" href="/favicon.ico">
        <link rel="stylesheet" href="./styles/style.css">
        <link rel="stylesheet" href="./styles/login.css">
    </head>
    <body>
        <div style="height:100vh; width:100vw; padding:0; margin:0; display:flex; justify-content:center; align-items:center;">
            <div class="parent signup">
                <h1>
                    astatine.eshop
                </h1>
                <h2 id="status">
                    <?php
                    if ($status == signupStatus::UsernameOccupied) {
                        echo "Username \"{$_POST['signup_username']}\" sudah wujud.";
                    }
                    ?>
                </h2>
                <form class="form" action="signup.php" method="POST" autocomplete="on" onsubmit="return validateForm();">
                    <div id="fields">
                        <h2>Nama : </h2>
                        <input placeholder="Nama penuh anda" class="signup_inputField" id="signup_name" type="text" name="signup_name">
                        <h2>Username : </h2>
                        <input placeholder="Tanpa jarak aksara" class="signup_inputField" id="signup_username" type="text" name="signup_username">
                        <!-- Add show password button? -->
                        <h2>Kata laluan : </h2>
                        <div id="password_criteria">
                            <input placeholder="Antara 4-8 aksara" class="signup_inputField" id="signup_password" type="password" name="signup_password" autocomplete="on" onkeyup="onPasswordUpdate();">
                            <div>
                                <img src="./assets/logos/cross.png">
                                <h3>antara 4-8 aksara</h3>
                                <img src="./assets/logos/cross.png">
                                <h3>sekurang-kurangnya satu huruf besar</h3>
                                <img src="./assets/logos/check.png">
                                <h3>sekurang-kurangnya satu huruf kecil</h3>
                                <img src="./assets/logos/check.png">
                                <h3>sekurang-kurangnya satu nombor</h3>
                                <img src="./assets/logos/check.png">
                                <h3>sekurang-kurangnya satu tanda baca</h3>
                                <img src="./assets/logos/check.png">
                                <h3>tidak mempunyai jarak aksara</h3>
                            </div>
                        </div>
                        <h2>Kata laluan sekali lagi : </h2>
                        <input placeholder="Mesti sama dengan kata laluan" class="signup_inputField" id="signup_confirm_password" type="password" name="signup_confirm_password" autocomplete="on">
                    </div>
                    <a id="login" href="/login.php">
                        Kembali ke log masuk
                    </a>
                    <input id="submit" type="submit" value="Daftar pengguna">
                </form>
            </div>
        </div>

        <script src="./scripts/main_script.js"></script>
        <script src="./scripts/signup.js"></script>
    </body>
</html>