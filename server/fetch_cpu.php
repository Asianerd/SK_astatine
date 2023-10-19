<?php

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

require __DIR__ . '/..' . '/client/CPU.php'; // import cpu class

Item::initialize();

$sort_dict = array(
    0=>"id_CPU",
    1=>"nombor_teras",
    2=>"frekuensi_tertinggi",
    3=>"harga",
    4=>"bilangan_interaksi"
);

$query_statement = "";
switch ($_REQUEST['request-mode']) {
    case "liked":
        // fetch all cpus the user liked
        $query_statement = "SELECT * FROM cpu
        INNER JOIN pilihan
        ON cpu.id_CPU = pilihan.id_CPU
        WHERE pilihan.user_id = {$_COOKIE['user_id']}";
        break;
    case "filtered":
        // fetch all cpus that match the criteria
        $query_statement = "SELECT * FROM cpu WHERE
        (nombor_teras BETWEEN {$_REQUEST['core-low']} AND {$_REQUEST['core-high']}) AND
        (frekuensi >= {$_REQUEST['frequency-low']} AND frekuensi_tertinggi <= {$_REQUEST['frequency-high']}) AND
        (harga BETWEEN {$_REQUEST['price-low']} AND {$_REQUEST['price-high']})".
        (empty($_REQUEST['search_input']) ? "" : "AND model LIKE '%{$_REQUEST['search_input']}%' ").
        "ORDER BY {$sort_dict[$_REQUEST['sort']]} " . ($_REQUEST['direction'] == 1 ? "DESC" : "ASC");
        break;
    default:
        $query_statement = "SELECT * FROM cpu";
}

$siftedCollection = [];
$db = new mysqli($hostname='localhost', $username='astatine', $password='password', $database='astatine_data');
// login to db
foreach ($db->query($query_statement) as $record) {
    // push items to $siftedCollection
    array_push($siftedCollection, Item::from_dict($record));
}

$result = [];
if (isset($_COOKIE["user_id"])) {
    foreach ($db->query("SELECT * FROM PILIHAN WHERE {$_COOKIE['user_id']} = user_id") as $record) {
        array_push($result, $record["id_CPU"]);
    }
}

$final = "";
foreach($siftedCollection as $i) {
    if (empty($_REQUEST['search_input'])) {
        $name = $i->name;
    } else {
        $name = str_ireplace($_REQUEST['search_input'], "<mark>".$_REQUEST['search_input']."</mark>", $i->name);
    }
    $liked = in_array($i->id, $result);
    $final = $final . "<div class='entity' id='instantiated_entity_{$i->id}' onclick='like_entity({$i->id})'".($liked ? "aria-label='liked'" : "").">
    <div id='showcase-image'>
        <img src='./assets/cpu/{$i->image_url}'>
    </div>
    <div id='info-section'>
        <div id='header'>
            <div id='cores'>
                <h1>{$i->cores}</h1>
                <img src='./assets/logos/core.png'>
                <hr>
            </div>
            <h1>{$name}</h1>
        </div>
        <hr>
        <div id='info'>
            <div id='data'>
                <h1>{$currencyFormatter->formatCurrency($i->price, 'MYR')}</h1>
                <div>
                    <h1 id='like_amount'>{$numberFormatter->format($i->interaction_count)}</h1>
                    <img id='like_indicator' src='./assets/logos/".($liked ? '' : 'white_')."heart_filled.png'>
                </div>
            </div>
            <div id='hz'>
                <div>
                    <h1>".number_format($i->frequency, 1)."</h1>
                    <img src='./assets/logos/dash.png'>
                    <h1>".number_format($i->boosted_frequency, 1)."GHz</h1>
                </div>
            </div>
        </div>
    </div>
</div>";
}

foreach ($db->query("SELECT COUNT(*) as count FROM cpu") as $r) {
    $count = $r['count'];
}

if ($final == "") {
    $final = "
<h1 id='empty-query'>
    Tiada produk CPU yang mengikuti kriteria diminta 😢😢😢
</h1>";
}

echo "<div class='item-container'>{$final}</div>";
echo "<h3 id='query-count'>Menunjukkan ". count($siftedCollection) ." daripada {$count} produk.</h3>";
echo "<h2 id='query-print' onclick='window.print()'>Cetak</h2>";
?>