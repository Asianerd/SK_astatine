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
        $query_statement = "SELECT * FROM cpu
        INNER JOIN pilihan
        ON cpu.id_CPU = pilihan.id_CPU
        WHERE pilihan.user_id = {$_COOKIE['user_id']}";
        break;
    case "filtered":
        $query_statement = "SELECT * FROM cpu WHERE
        (nombor_teras BETWEEN {$_REQUEST['core-low']} AND {$_REQUEST['core-high']}) AND
        (frekuensi >= {$_REQUEST['frequency-low']} AND frekuensi_tertinggi <= {$_REQUEST['frequency-high']}) AND
        (harga BETWEEN {$_REQUEST['price-low']} AND {$_REQUEST['price-high']})".
        (empty($_REQUEST['search_input']) ? "" : "AND model LIKE '%{$_REQUEST['search_input']}%' ").
        "ORDER BY {$sort_dict[$_REQUEST['sort']]} " . ($_REQUEST['direction'] == 1 ? "DESC" : "ASC");
        // $query_statement = "SELECT * FROM cpu WHERE
        // (nomber_teras BETWEEN {$_REQUEST['core-low']} AND {$_REQUEST['core-high']})
        // (nombor_teras >= {$_REQUEST['core-low']} AND nombor_teras <= {$_REQUEST['core-high']}) AND
        // (frekuensi >= {$_REQUEST['frequency-low']} AND frekuensi_tertinggi <= {$_REQUEST['frequency-high']}) AND
        // (harga >= {$_REQUEST['price-low']} AND harga <= {$_REQUEST['price-high']})
        // ORDER BY {$sort_dict[$_REQUEST['sort']]} " . ($_REQUEST['direction'] == 0 ? "DESC" : "ASC");
        break;
    default:
        $query_statement = "SELECT * FROM cpu";
}

$siftedCollection = [];
$db = new mysqli($hostname='localhost', $username='astatine', $password='password', $database='astatine_data');
foreach ($db->query($query_statement) as $record) {
    array_push($siftedCollection, Item::from_dict($record));
}

// // get value of sliders from url parameters
// $coreLow = $_REQUEST["core-low"];
// $coreHigh = $_REQUEST["core-high"];

// $frequencyLow = $_REQUEST["frequency-low"];
// $frequencyHigh = $_REQUEST["frequency-high"];

// $priceLow = $_REQUEST["price-low"];
// $priceHigh = $_REQUEST["price-high"];

// $sortType = $_REQUEST["sort"]; // cores, frequency, price, liked
// $sortDirection = $_REQUEST["direction"]; // 0 is descending, 1 is ascending


// $siftedCollection = [];
// $final = "";
// foreach(Item::$collection as $i) {
//     $match = true;
//     // if the cpu fails any of these checks, they dont get added to $siftedCollection
//     if (($i->cores < $coreLow) || ($i->cores > $coreHigh)) {
//         $match = false;
//     }
//     if (($i->frequency < $frequencyLow) || ($i->frequency > $frequencyHigh)) {
//         $match = false;
//     } else {
//         // maybe the boosted frequency reaches the target, but not the base
//         if (($i->boosted_frequency < $frequencyLow) || ($i->boosted_frequency > $frequencyHigh)) {
//             $match = false;
//         }
//     }
//     if (($i->price < $priceLow) || ($i->price > $priceHigh)) {
//         $match = false;
//     }

//     if (!$match) {
//         // if even one of the checks fail, the for loop skips to the next element
//         continue;
//     }

//     // adds the cpu to the list
//     array_push($siftedCollection, $i);
// }

// $sort_dict = array(
//     1=>"cores",
//     2=>"boosted_frequency",
//     3=>"price",
//     4=>"interaction_count"
// );

// if ($sortType != 0) {
//     //$attributeName = $sortType == 1 ? "cores" : ($sortType == 2 ? "boosted_frequency" : "price");
//     $attributeName = $sort_dict[$sortType];
//     usort($siftedCollection, function ($a, $b) use ($attributeName, $sortDirection) { // 'use' keyword so that a few variables can be used
//         return $a->$attributeName == $b->$attributeName ? 0 :           // same = 0
//             ($a->$attributeName > $b->$attributeName ? $sortDirection : // greater = 1
//                 -1 * $sortDirection);                                   // lesser = -1
//                 // multiplied by $sortDirection to invert the direction
//     });
// }

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