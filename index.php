<!DOCTYPE html>
<html>
    <head>
        <title>Astatine.eshop</title>
        <script type="text/javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <link rel="icon" type="image/x-icon" href="/favicon.ico">
        <link rel="stylesheet" href="./styles/style.css">
        <link rel="stylesheet" href="./styles/homepage.css">
        <?php

        if (isset($_COOKIE["login_new"]) && ($_COOKIE["login_new"] <= 0)) {
            setcookie("login_new", 1, time() + (86400 * 14), "/"); // after alert, increment so it doesnt alert again
            //echo "<script>alert(\"Successfully logged in as {$_COOKIE["login_username"]}.\")</script>";
            echo "<script>alert(\"Berjaya log masuk dengan akaun {$_COOKIE["login_username"]}.\")</script>";
        }

        require __DIR__ . '/client/CPU.php'; // import cpu class

        Item::initialize();
        // initialized twice, once here and another in fetch_cpu but thats fine

        ?>
    </head>
    <body>
        <div id="prefab_header"></div>
        <div id="prefab_login_popup" aria-label="inactive"></div>
        <!-- <img src="/assets/outrun.gif" id="background-image"> -->
        <!-- <div id="prefab_item_filter"></div> -->
        <div id="content-parent">
            <div class="item-filter">
                <div id="input">
                    <div id="title">
                        <h1>Teras</h1>
                        <h2 class="slider-text">0Hz - 2.4Hz</h2>
                    </div>
                    <div class="slider-range" id="core">
                        <input type="range"
                            value="<?php echo Item::$slider_ranges["cores-start"];?>"
                            min="<?php echo Item::$slider_ranges["cores-start"];?>"
                            max="<?php echo Item::$slider_ranges["cores-end"];?>"
                            step="1">
                        <input type="range"
                            value="<?php echo Item::$slider_ranges["cores-end"];?>"
                            min="<?php echo Item::$slider_ranges["cores-start"];?>"
                            max="<?php echo Item::$slider_ranges["cores-end"];?>"
                            step="1">
                    </div>
                </div>
                <div id="input">
                    <div id="title">
                        <h1>Frekuensi</h1>
                        <h2 class="slider-text">0Hz - 2.4Hz</h2>
                    </div>
                    <div class="slider-range" id="frequency">
                        <input type="range"
                            value="<?php echo Item::$slider_ranges["frequency-start"];?>"
                            min="<?php echo Item::$slider_ranges["frequency-start"];?>"
                            max="<?php echo Item::$slider_ranges["frequency-end"];?>"
                            step="0.1">
                        <input type="range"
                            value="<?php echo Item::$slider_ranges["frequency-end"];?>"
                            min="<?php echo Item::$slider_ranges["frequency-start"];?>"
                            max="<?php echo Item::$slider_ranges["frequency-end"];?>"
                            step="0.1">
                    </div>
                </div>
                <div id="input">
                    <div id="title">
                        <h1>Harga</h1>
                        <h2 class="slider-text">0Hz - 2.4Hz</h2>
                    </div>
                    <div class="slider-range" id="price">
                    <input type="range"
                            value="<?php echo Item::$slider_ranges["price-start"];?>"
                            min="<?php echo Item::$slider_ranges["price-start"];?>"
                            max="<?php echo Item::$slider_ranges["price-end"];?>"
                            step="0.01">
                        <input type="range"
                            value="<?php echo Item::$slider_ranges["price-end"];?>"
                            min="<?php echo Item::$slider_ranges["price-start"];?>"
                            max="<?php echo Item::$slider_ranges["price-end"];?>"
                            step="0.01">
                    </div>
                </div>
                <div id="sorting">
                    <h1>
                        Isih mengikut :
                    </h1>
                    <div id="sort-options">
                        <div id="sort-types">
                            <input type="radio" name="sort-option" id="sort-options-core" value="1">
                            <label for="sort-options-core">
                                <h3>Teras</h3>
                            </label>
                            <input type="radio" name="sort-option" id="sort-options-frequency" value="2">
                            <label for="sort-options-frequency">
                                <h3>Frekuensi</h3>
                            </label>
                            <input type="radio" name="sort-option" id="sort-options-price" value="3">
                            <label for="sort-options-price">
                                <h3>Harga</h3>
                            </label>
                        </div>
                        <div id="sort-direction" onclick="sortDirectionClick();">
                            <img src="./assets/logos/up_chevron.png">
                            <h3>
                                Menaik
                            </h3>
                        </div>
                    </div>
                </div>
            </div>
            <div class="item-container" style="width:60%;">
                <!-- all cpu entities are here -->
            </div>
        </div>
        <div style="height:50vh;"></div>
        <script src="./scripts/main_script.js"></script>
        <script src="./scripts/homepage.js"></script>
        <script src="./scripts/entity_events.js"></script>
    </body>
</html>