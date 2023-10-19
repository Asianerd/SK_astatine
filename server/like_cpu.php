<?php
if (!(isset($_POST["user"]) && isset($_POST["cpu"]) && isset($_POST["action"]))) {
    echo "user, cpu, action not set";
    return;
}

$db = new mysqli($hostname='localhost', $username='astatine', $password='password', $database='astatine_data');
// log into db

// 0 -> unlike
// 1 -> like
if ($_POST["action"] == 0) {
    // unlike
    $db->query("DELETE FROM pilihan WHERE id_CPU = {$_POST['cpu']} AND user_id = {$_POST['user']}");

    echo "unliked";
} else {
    // like
    // refer to signup.php for explanation about this algorithm
    $current_record_id = 0;
    $found = false;
    foreach ($db->query("SELECT id_pilih FROM pilihan ORDER BY id_pilih ASC") as $rows) {
        $current = (int)$rows["id_pilih"];
        $current_record_id++;
        if ($current != $current_record_id) {
            $found = true;
            break;
        }
    };
    if (!$found) {
        $current_record_id++;
    }

    $db->query("INSERT INTO pilihan VALUES ({$current_record_id}, {$_POST['user']}, {$_POST['cpu']})");
    echo "liked";
}
// update the interaction count on the cpu
$likes = 0;
foreach ($db->query("SELECT COUNT(user_id) FROM pilihan WHERE id_CPU = {$_POST['cpu']}") as $element) {
    // set $likes to the amount of counts of user_id of the id_CPU = {id} query
    $likes = $element['COUNT(user_id)'];
}
echo $db->query("UPDATE cpu SET bilangan_interaksi = {$likes} WHERE id_CPU = {$_POST['cpu']}");
?>