<?php
// redirects the user back to the homepage if they arent an admin

if (!isset($_COOKIE['user_id'])) {
    // redirect if user_id cookie is not set
    redirect();
}

$user = 0;
$db = new mysqli($hostname='localhost', $username='astatine', $password='password', $database='astatine_data');
$query = $db->query("SELECT * FROM `pelanggan` WHERE user_id = {$_COOKIE['user_id']}"); // select record with the same user_id
foreach ($query as $x) {
    $user = $x;
    break;
}

if ($user == 0) {
    // redirect if no matches
    redirect();
}

if ($user['admin'] != 1) {
    // redirect if user is non-admin
    redirect();
}

function redirect() {
    header("Location: ./nonadmin_redirect.php");
}
?>