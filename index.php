<!DOCTYPE html>
<html>
    <head>
        <title>Astatine.shop</title>
        <script type="text/javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <link rel="icon" type="image/x-icon" href="/favicon.ico">
        <link rel="stylesheet" href="./styles/style.css">
        <link rel="stylesheet" href="./styles/homepage.css">
        <?php

        if (isset($_COOKIE["login_new"]) && ($_COOKIE["login_new"] <= 0)) {
            setcookie("login_new", 1, time() + (86400 * 14), "/"); // after alert, increment so it doesnt alert again
            echo "<script>alert(\"Successfully logged in as {$_COOKIE["login_username"]}.\")</script>";
        }

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

        require __DIR__ . '/client/CPU.php'; // import cpu class

        Item::initialize();

        ?>
    </head>
    <body>
        <div id="prefab_header"></div>
        <!-- <img src="/assets/outrun.gif" id="background-image"> -->
        <div id="prefab_item_filter"></div>
        <div>
            <div style="height:10vh"></div>
            <div class="item-container" style="width:90%; margin-top:2cm;">
                <?php
foreach(Item::$collection as $i) {
echo "<div class='entity'>
    <div id='showcase-image'>
        <img src='./assets/sample-images/i9.png'>
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
                    <img src='./assets/logos/eye.png'>
                    <h1>{$numberFormatter->format($i->interaction_count)} views</h1>
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
                ?>
            </div>
        </div>
        <div style="height:200vh;"></div>
        <script src="./scripts/main_script.js"></script>
    </body>
</html>