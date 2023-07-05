<?php

require __DIR__ . '/admin_check.php'; // check if admin

enum registerStatus {
    case Unset;
    case Success;
    case ModelExists;
    case FieldNotSet;
}

$status = registerStatus::Unset;

if (isset($_POST["daftar_name"]) &&
    isset($_POST["daftar_price"]) &&
    isset($_POST["daftar_cores"]) &&
    isset($_POST["daftar_frequency"]) &&
isset($_POST["daftar_boosted_frequency"])) {
    $db = new mysqli($hostname='localhost', $username='astatine', $password='password', $database='astatine_data');
    $query = $db->query("SELECT * FROM `cpu` WHERE model = '{$_POST['daftar_name']}'");
    if ($query->num_rows == 0) {

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

        $db->query("INSERT INTO `cpu` (id_CPU, model, harga, bilangan_interaksi, nombor_teras, frekuensi, frekuensi_tertinggi)
            VALUES ({$current_cpu_id}, \"{$_POST["daftar_name"]}\", \"{$_POST["daftar_price"]}\", 0, \"{$_POST["daftar_cores"]}\", \"{$_POST["daftar_frequency"]}\", \"{$_POST["daftar_boosted_frequency"]}\")");
        $status = registerStatus::Success;
        // unset($_POST["daftar_name"]);
        // unset($_POST["daftar_price"]);
        // unset($_POST["daftar_cores"]);
        // unset($_POST["daftar_frequency"]);
        // unset($_POST["daftar_boosted_frequency"]);
    } else {
        $status = registerStatus::ModelExists;
    }
} else {
    $status = registerStatus::FieldNotSet;
}

?>
<!DOCTYPE html>
<html>
    <head>
        <title>Daftar CPU</title>
        <link rel="stylesheet" href="../styles/style.css">
        <link rel="stylesheet" href="../styles/login.css">
        <link rel="stylesheet" href="../styles/admin/daftar.css">
    </head>
    <body>
        <?php include '../prefabs/sidebar.php'; ?>
        <div style="height:100vh;width:100vw;margin:0;padding:0;display:flex;justify-content:center;align-items:center;">
            <div class="parent">
                <h1>Daftar CPU</h1>
                <h2 id="<?php
                echo $status == registerStatus::Success ? "success" : "error";
                ?>"><?php
                switch ($status) {
                    case registerStatus::ModelExists:
                        echo "Model '{$_POST['daftar_name']}' sudah didaftar.";
                        break;
                    case registerStatus::Success:
                        echo "Model '{$_POST['daftar_name']}' didaftar.";
                        break;
                    default:
                }
                ?></h2>
                <a id="import_file" href="../admin/import_file.php">
                    Import fail
                </a>
                <form class="form" action="daftar.php" method="post" autocomplete="on">
                    <div id="fields">
                        <!-- model, harga, nombor_teras, frekuensi, frekuensi_tertinggi -->
                        <h2>Model : </h2>
                        <input placeholder="Eg: Intel Core i9-13900KS" type="text" name="daftar_name" required="" maxlength="50" oninvalid="this.setCustomValidity('Sila masukkan model yang sah.')" oninput="setCustomValidity('')">
                        <h2>Harga : </h2>
                        <input placeholder="Mata wang MYR sahaja" type="number" step="0.01" max="1000000000000000000" name="daftar_price" required="" oninvalid="this.setCustomValidity('Sila masukkan harga yang sah.')" oninput="setCustomValidity('')">
                        <h2>Nombor teras : </h2>
                        <input placeholder="Nombor bulat sahaja" type="number" name="daftar_cores" required="" oninvalid="this.setCustomValidity('Sila masukkan nombor teras yang sah.')" oninput="setCustomValidity('')">
                        <h2>Frekuensi : </h2>
                        <input placeholder="Dalam unit GHz" type="number" step="0.1" name="daftar_frequency" required="" oninvalid="this.setCustomValidity('Sila masukkan frekuensi yang sah.')" oninput="setCustomValidity('')">
                        <h2>Frekuensi tertinggi : </h2>
                        <input placeholder="Dalam unit GHz" type="number" step="0.1" name="daftar_boosted_frequency" required="" oninvalid="this.setCustomValidity('Sila masukkan frekuensi tertinggi yang sah.')" oninput="setCustomValidity('')">
                    </div>
                    <input id="submit" type="submit" value="Daftar">
                </form>
            </div>
        </div>
        <script src="/scripts/main_script.js"></script>
    </body>
</html>