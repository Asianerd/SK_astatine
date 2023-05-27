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

// get value of sliders from url parameters
$coreLow = $_REQUEST["core-low"];
$coreHigh = $_REQUEST["core-high"];

$frequencyLow = $_REQUEST["frequency-low"];
$frequencyHigh = $_REQUEST["frequency-high"];

$priceLow = $_REQUEST["price-low"];
$priceHigh = $_REQUEST["price-high"];

$sortType = $_REQUEST["sort"]; // cores, frequency, price
$sortDirection = $_REQUEST["direction"]; // 0 is descending, 1 is ascending


$siftedCollection = [];
$final = "";
foreach(Item::$collection as $i) {
    $match = true;
    // if the cpu fails any of these checks, they dont get added to $siftedCollection
    if (($i->cores < $coreLow) || ($i->cores > $coreHigh)) {
        $match = false;
    }
    if (($i->frequency < $frequencyLow) || ($i->frequency > $frequencyHigh)) {
        $match = false;
    } else {
        // maybe the boosted frequency reaches the target, but not the base
        if (($i->boosted_frequency < $frequencyLow) || ($i->boosted_frequency > $frequencyHigh)) {
            $match = false;
        }
    }
    if (($i->price < $priceLow) || ($i->price > $priceHigh)) {
        $match = false;
    }

    if (!$match) {
        // if even one of the checks fail, the for loop skips to the next element
        continue;
    }

    // adds the cpu to the list
    array_push($siftedCollection, $i);
}

if ($sortType != 0) {
    $attributeName = $sortType == 1 ? "cores" : ($sortType == 2 ? "boosted_frequency" : "price");
    usort($siftedCollection, function ($a, $b) use ($attributeName, $sortDirection) { // 'use' keyword so that a few variables can be used
        return $a->$attributeName == $b->$attributeName ? 0 :           // same = 0
            ($a->$attributeName > $b->$attributeName ? $sortDirection : // greater = 1
                -1 * $sortDirection);                                   // lesser = -1
                // multiplied by $sortDirection to invert the direction
    });
}

$result = [];
if (isset($_COOKIE["user_id"])) {
    $db = new mysqli($hostname='localhost', $username='astatine', $password='password', $database='astatine_data');
    foreach ($db->query("SELECT * FROM PILIHAN WHERE {$_COOKIE['user_id']} = user_id") as $record) {
        array_push($result, $record["id_CPU"]);
    }
}

foreach($siftedCollection as $i) {
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
            <h1>{$i->name}</h1>
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

echo $final;
?>