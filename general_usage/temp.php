<!-- < ?php
$user_db = new mysqli($hostname='localhost', $username='astatine', $password='temp', $database='astatine_data');

foreach ($user_db->query("SELECT user_id FROM `user`") as $rows) {
    var_dump((int)$rows["user_id"]);
};
?> -->

<?php
$temp = 0;



?>
