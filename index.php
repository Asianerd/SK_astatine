<!DOCTYPE html>
<html>
    <head>
        <title>Astatine.eshop</title>
        <link rel="icon" type="image/x-icon" href="/favicon.ico">
        <link rel="stylesheet" href="./styles/style.css">
        <link rel="stylesheet" href="./styles/homepage.css">
        <?php

        if (isset($_COOKIE["login_new"]) && ($_COOKIE["login_new"] <= 0)) {
            if ($_COOKIE['login_new'] == 0) {
                // display log in message
                echo "<script>alert(\"Berjaya log masuk dengan akaun '{$_COOKIE["login_username"]}'.\")</script>";
            } else {
                // display sign up message
                echo "<script>alert(\"Berjaya daftar masuk akaun baharu '{$_COOKIE["login_username"]}'.\")</script>";
            }
            setcookie("login_new", 1, time() + (86400 * 14), "/"); // after alert, increment so it doesnt alert again
        }

        require __DIR__ . '/client/CPU.php'; // import cpu class

        Item::initialize();
        // initialized twice, once here and another in fetch_cpu but thats fine

        ?>
    </head>
    <body>
        <?php include './prefabs/sidebar.php'; ?>
        <?php include './prefabs/login_popup.html'; ?>
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
                            <label for="sort-options-core" title="Nombor teras">
                                <img src='/assets/logos/core.png'>
                            </label>
                            <input type="radio" name="sort-option" id="sort-options-frequency" value="2">
                            <label for="sort-options-frequency" title="Frekuensi">
                                <img src='/assets/logos/frequency.png'>
                            </label>
                            <input type="radio" name="sort-option" id="sort-options-price" value="3">
                            <label for="sort-options-price" title="Harga">
                                <img src='/assets/logos/money.png'>
                            </label>
                            <input type="radio" name="sort-option" id="sort-options-liked" value="4">
                            <label for="sort-options-liked" title="Nombor pilihan">
                                <img src='/assets/logos/white_heart.png'>
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
            <div style="width:60%;">
                <div id="search-bar">
                    <div id="image-container">
                        <img src="./assets/logos/search.png">
                    </div>
                    <hr>
                    <input class="typing-effect" data-period="2000" data-rotate='<?php 
                    $cpu_names = [];
                    // empty array

                    foreach (Item::$collection as $cpu) {
                        // push the names of all cpus into the array
                        array_push($cpu_names, "\"Eg: {$cpu->name}\"");
                    }

                    // randomize the arrangement
                    shuffle($cpu_names);

                    // turn the list into a string parseable by js
                    echo '['.implode(',', $cpu_names).']';
                    ?>' type="text">
                </div>
                <div class="query-result">
                    <!-- all cpu entities + extra info are here -->
                </div>
            </div>
        </div>
        <div style="height:50vh;"></div>
        <script src="./scripts/main_script.js"></script>
        <script src="./scripts/homepage.js"></script>
        <script src="./scripts/entity_events.js"></script>
    </body>
</html>