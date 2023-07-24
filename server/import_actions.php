<?php

$db = new mysqli($hostname='localhost', $username='astatine', $password='password', $database='astatine_data');

switch ($_REQUEST['type']) {
    case 'overwrite':
        $db->query("UPDATE cpu SET id_CPU=".$_REQUEST['id'].", model='".$_REQUEST['name']."', harga=".$_REQUEST['price'].", bilangan_interaksi=".$_REQUEST['interaction'].", nombor_teras=".$_REQUEST['cores'].", frekuensi=".$_REQUEST['freq'].", frekuensi_tertinggi=".$_REQUEST['boosted_freq']." WHERE id_CPU={$_REQUEST['id']};");
        break;
    case 'add_new':
        // this algorithm is explained in signup.php
        $current_cpu_id = 0;
        $found = false;
        foreach ($db->query("SELECT id_CPU FROM `cpu` ORDER BY id_CPU ASC") as $rows) {
            $current = (int)$rows["id_CPU"];
            $current_cpu_id++;

            if ($current != $current_cpu_id) {
                $found = true;
                break;
            }
        };
        if (!$found) {
            $current_cpu_id++;
        }
        //echo "UPDATE cpu SET id_CPU=$current_cpu_id, model='".$_REQUEST['name']."', harga=".$_REQUEST['price'].", bilangan_interaksi=".$_REQUEST['interaction'].", nombor_teras=".$_REQUEST['cores'].", frekuensi=".$_REQUEST['freq'].", frekuensi_tertinggi=".$_REQUEST['boosted_freq']." WHERE id_CPU={$_REQUEST['id']};";
        //echo "INSERT INTO `cpu` (id_CPU, model, harga, bilangan_interaksi, nombor_teras, frekuensi, frekuensi_tertinggi) VALUES ({$current_cpu_id}, \"{$_REQUEST['name']}\", {$_REQUEST['price']}, {$_REQUEST['interaction']}, {$_REQUEST['cores']}, {$_REQUEST['freq']}, {$_REQUEST['boosted_freq']})";
        $db->query("INSERT INTO `cpu` (id_CPU, model, harga, bilangan_interaksi, nombor_teras, frekuensi, frekuensi_tertinggi) VALUES ({$current_cpu_id}, \"{$_REQUEST['name']}\", {$_REQUEST['price']}, {$_REQUEST['interaction']}, {$_REQUEST['cores']}, {$_REQUEST['freq']}, {$_REQUEST['boosted_freq']})");
        echo $current_cpu_id;
        break;
    default:
}
?>