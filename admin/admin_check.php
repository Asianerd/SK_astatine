<?php

if (!isset($_COOKIE['user_id'])) {
    redirect();
}

$user = 0;
$db = new mysqli($hostname='localhost', $username='astatine', $password='password', $database='astatine_data');
$query = $db->query("SELECT * FROM `pelanggan` WHERE user_id = {$_COOKIE['user_id']}");
foreach ($query as $x) {
    $user = $x;
    break;
}

if ($user == 0) {
    redirect();
}

if ($user['admin'] != 1) {
    redirect();
}

function redirect() {
    header("Location: ./nonadmin_redirect.php");
}
?>