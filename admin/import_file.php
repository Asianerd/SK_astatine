<?php
require __DIR__ . '/admin_check.php'; // check if admin

$numberFormatter = new \NumberFormatter(
    'en_US',
    \NumberFormatter::PADDING_POSITION
);

$currencyFormatter = new \NumberFormatter(
    'en_US',
    \NumberFormatter::CURRENCY
);

function formatHZ($hz) {
    return number_format($hz, 1); // makes string interpolation easier
}

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
        if (in_array(intval($row[0]), array_map(function($item) {
            return $item->id;
        }, Item::$collection))) {
            $i["status"] = itemStatus::OverrideOption;
        }

        $i["item"] = new Item(
            $row[0],
            $row[1],
            floatval($row[2]),
            floatval($row[3]),
            floatval($row[4]),
            floatval($row[5]),
            floatval($row[6])
        );
    }

    array_push($result, $i);
}

$db = new mysqli($hostname='localhost', $username='astatine', $password='password', $database='astatine_data');

foreach ($result as $item) {
    if ($item["status"] != itemStatus::Success) {
        continue;
    }

    $db->query("INSERT INTO cpu VALUES ({$item['item']->id}, '{$item['item']->name}', {$item['item']->price}, {$item['item']->interaction_count}, {$item['item']->cores}, {$item['item']->frequency}, {$item['item']->boosted_frequency})");
    //echo "INSERT INTO cpu VALUES ({$item['item']->id}, '{$item['item']->name}', {$item['item']->price}, {$item['item']->interaction_count}, {$item['item']->cores}, {$item['item']->frequency}, {$item['item']->boosted_frequency})";
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
        <?php
        if ($status == uploadStatus::Success) {
            echo '<script>alert("Berjaya import fail")</script>';
        }
        ?>
        <div style="display:flex;justify-content:center;align-items:center;flex-direction:column;">
            <div class="parent">
                <h1>Import fail</h1>
                <h2>
                    <?php
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
                </h2>
                <form method="post" class="file-drop" action="import_file.php" enctype="multipart/form-data">
                    <label for="file">
                        <input type="file" name="file" id="file">
                        <div>
                            <img src="/assets/logos/file_upload.png">
                            <div>
                                <h4>
                                </h4>
                                <h3>
                                    Muat naik fail anda
                                </h3>
                                <h2>
                                    Hanya jenis fail CSV diterima
                                </h2>
                            </div>
                        </div>
                    </label>
                    <input type="submit" value="Import fail">
                </form>
            </div>
            <div class="parent log" id="log" style="<?php echo ($status == uploadStatus::Success ? 'display:flex;' : 'display:none;'); ?>">
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
                            <tr id='instantiated_log_{$item['item']->id}' ".($item['status'] == itemStatus::OverrideOption ? 'class="override_option"' : '').">
                                <td>{$item['item']->id}</td>
                                <td>{$item['item']->name}</td>
                                <td>{$currencyFormatter->formatCurrency($item['item']->price, 'MYR')}</td>
                                <td>{$numberFormatter->format($item['item']->interaction_count)}</td>
                                <td>{$item['item']->cores}</td>
                                <td>".formatHZ($item['item']->frequency)."</td>
                                <td>".formatHZ($item['item']->boosted_frequency)."</td>
                                ".
                                ($item['status'] == itemStatus::OverrideOption ?
                                "<td id='actions'>
                                    <div>
                                        <h2 title='Kemas kini' onclick='overwrite({$item['item']->id}, \"{$item['item']->name}\", \"{$item['item']->price}\", \"{$item['item']->interaction_count}\", \"{$item['item']->cores}\", \"{$item['item']->frequency}\", \"{$item['item']->boosted_frequency}\")'>
                                            📝
                                        </h2>
                                        <h2 title='Tambah sebagai baharu' onclick='add_new({$item['item']->id}, \"{$item['item']->name}\", \"{$item['item']->price}\", \"{$item['item']->interaction_count}\", \"{$item['item']->cores}\", \"{$item['item']->frequency}\", \"{$item['item']->boosted_frequency}\")'>
                                            ➕
                                        </h2>
                                        <h2 title='Abaikan' onclick='dispose({$item['item']->id})'>
                                            ❌
                                        </h2>
                                    </div>
                                </td>" : '')
                                ."
                            </tr>
                            ";
                        }
                        ?>
                    </table>
                    <div id="all-options">
                        <h2>
                            Untuk semua id bercanggah : 
                        </h2>
                        <div>
                            <h2 onclick="overwrite_all()">
                                📝 Kemas kini dengan data baharu
                            </h2>
                            <!-- <h2 onclick="add_new_all()"> removed due to async issues
                                ➕ Tambah dengan id baharu
                            </h2> -->
                            <h2 onclick="dispose_all()">
                                ❌ Jangan ambil tindakan
                            </h2>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <script src="/scripts/main_script.js"></script>
        <script src="/scripts/import_file.js"></script>
    </body>
</html>