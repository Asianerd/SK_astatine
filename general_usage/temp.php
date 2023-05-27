<!-- < ?php
$user_db = new mysqli($hostname='localhost', $username='astatine', $password='temp', $database='astatine_data');

foreach ($user_db->query("SELECT user_id FROM `user`") as $rows) {
    var_dump((int)$rows["user_id"]);
};
?> -->

<?php
// var_dump(explode("i", "abcdef"));

$highest_user_id = 0;

$user_db = new mysqli($hostname='localhost', $username='astatine', $password='password', $database='astatine_data');

$result = $user_db->query("SELECT MAX(user_id)
FROM pelanggan;");

foreach ($result as $element) {
    $highest_user_id = $element["MAX(user_id)"];
}


?>
