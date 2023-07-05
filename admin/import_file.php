<?php
require __DIR__ . '/admin_check.php'; // check if admin

enum uploadStatus {
    case Unset;
    case Success;
    case WrongType;
    case ErrorParsing;
}
$status = uploadStatus::Unset;
$raw_data = array();

if (!empty($_FILES["file"]["name"])) {
    if (!in_array($_FILES["file"]["type"], array(
        'text/x-comma-separated-values',
        'text/comma-separated-values',
        'application/octet-stream',
        'application/vnd.ms-excel',
        'application/x-csv',
        'text/x-csv',
        'text/csv',
        'application/csv',
        'application/excel',
        'application/vnd.msexcel',
        'text/plain'
    ))) {
        $status = uploadStatus::WrongType;
    } else {
        $status = uploadStatus::Success;
        $file_stream = fopen($_FILES["file"]["tmp_name"], "r");
        while(($l = fgetcsv($file_stream)) !== FALSE) {
            array_push($raw_data, $l);
        }
        fclose($file_stream);
    }
}

require __DIR__ . '/../client/CPU.php';

Item::initialize();

enum itemStatus {
    case Success;
    case Unset;
    case Less; // less fields than whats required
    case More; // more fields than whats required
    case Invalid; // fields are invalid type of data
    case OverrideOption; // provide option to override if id already exists
}

$result = array();
foreach ($raw_data as $row) {
    $i = array(
        "status"=>itemStatus::Success
    );

    if (count($row) < Item::$COLUMN_COUNT) {
        $i["status"] = itemStatus::Less;
    } else if (count($row) > Item::$COLUMN_COUNT) {
        $i["status"] = itemStatus::More;
    }

    for ($index=0; $index < Item::$COLUMN_COUNT; $index++) {
        if ($index == 1) {
            // skip the model column
            continue;
        }

        if (!is_numeric($row[$index])) {
            $i["status"] = itemStatus::Invalid;
            $i["invalid_column"] = $index;
            break;
        }
    }

    if ($i["status"] == itemStatus::Success) {
        if (array_key_exists($row[0], array_map(function($item) {
            return $item->id;
        }, Item::$collection))) {
            $i["status"] = itemStatus::OverrideOption;
        }

        $i["item"] = new Item(
            $row[0],
            $row[1],
            $row[2],
            $row[3],
            $row[4],
            $row[5],
            $row[6]
        );
    }

    array_push($result, $i);
}

?>
<!DOCTYPE html>
<html>
    <head>
        <title>Import fail</title>
        <link rel="stylesheet" href="../styles/style.css">
        <link rel="stylesheet" href="../styles/login.css">
        <link rel="stylesheet" href="../styles/admin/daftar.css">
        <link rel="stylesheet" href="../styles/admin/import_file.css">
    </head>
    <body>
        <?php include '../prefabs/sidebar.php'; ?>
        <div style="display:flex;justify-content:center;align-items:center;flex-direction:column;">
            <div class="parent">
                <h1>Import fail</h1>
                <p style="color:white">
                    <?php
                    var_dump($result);
                    switch($status) {
                        case uploadStatus::WrongType:
                            echo "Jenis fail tidak disokong. Sila muat naik fail jenis csv sahaja.";
                            break;
                        case uploadStatus::ErrorParsing:
                            echo "Fail tidak dapat diproses. Sila pastikan sintaks fail adalah betul.";
                            break;
                        default:
                    };
                    ?>
                </p>
                <form method="post" class="file-drop" action="import_file.php" enctype="multipart/form-data">
                <!-- <form method="post" class="file-drop" action="import_file.php" enctype="multipart/form-data" style="display:<?php
                // echo $status == uploadStatus::Success ? 'none' : 'flex'
                ?> !important;"> -->
                    <label for="file">
                        <input type="file" name="file" id="file">
                        <div>
                            <img src="/assets/logos/file_upload.png">
                            <div>
                                <h3>
                                    Muat naik fail anda
                                </h3>
                                <h2>
                                    Hanya jenis fail CSV diterima
                                </h2>
                            </div>
                        </div>
                    </label>
                    <input type="submit">
                </form>
            </div>
            <div class="parent log" style="<?php echo ($status == uploadStatus::Success ? 'display:flex;' : 'display:none;'); ?>">
                <h1>
                    Log pengimportan fail
                </h1>
                <div>
                    <h2>
                        <?php echo count($result)?> item diproses
                    </h2>
                    <table>
                        <tr>
                            <th>id_CPU</th>
                            <th>model</th>
                            <th>harga</th>
                            <th>bilangan_interaksi</th>
                            <th>nombor_teras</th>
                            <th>frekuensi</th>
                            <th>frekuensi_tertinggi</th>
                        </tr>
                        <?php
                        foreach ($result as $item) {
                            if (!(($item["status"] == itemStatus::Success) || ($item["status"] == itemStatus::OverrideOption))) {
                                continue;
                            }
                            echo "
                            <tr>
                                <td>{$item['item']->id}</td>
                                <td>{$item['item']->name}</td>
                                <td>{$item['item']->price}</td>
                                <td>{$item['item']->interaction_count}</td>
                                <td>{$item['item']->cores}</td>
                                <td>{$item['item']->frequency}</td>
                                <td>{$item['item']->boosted_frequency}</td>
                                ".
                                ($item['status'] == itemStatus::OverrideOption ?
                                '<td>
                                    <div>
                                        <h2>
                                            📝
                                        </h2>
                                        <h2>
                                            ➕
                                        </h2>
                                        <h2>
                                            ❌
                                        </h2>
                                    </div>
                                </td>' : '')
                                ."
                            </tr>
                            ";
                        }
                        ?>
                        <!-- <tr>
                            <td>id_CPU</td>
                            <td>model</td>
                            <td>harga</td>
                            <td>bilangan_interaksi</td>
                            <td>nombor_teras</td>
                            <td>frekuensi</td>
                            <td>frekuensi_tertinggi</td>
                        </tr> -->
                    </table>
                </div>
            </div>
        </div>
        <script src="/scripts/main_script.js"></script>
    </body>
</html>