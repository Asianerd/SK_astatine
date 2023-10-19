<?php

class Item {
    // #region Statics
    public static $COLUMN_COUNT = 7;
    public static $collection; // holds all cpu items
    public static $slider_ranges;
    static $data_ranges;

    public static function initialize() {
        Item::$collection = array();
        Item::$slider_ranges = [];
        Item::$data_ranges = [
            // for the start and end of the slider range
            "cores" => [PHP_INT_MAX, 0],
            "frequency" => [PHP_INT_MAX, 0.0],
            "boosted_frequency" => [PHP_INT_MAX, 0.0],
            "price" => [PHP_INT_MAX, 0]
        ];

        // connect to database
        $db = new mysqli($hostname='localhost', $username='astatine', $password='password', $database='astatine_data');
        
        // populate $collection with all records from db
        foreach($db->query('SELECT * FROM `cpu`') as $row) {
            // add to $collection
            array_push(Item::$collection, Item::from_dict($row));
        }

        foreach(Item::$collection as $cpu) {
            // loop through every cpu
            foreach (array_keys(Item::$data_ranges) as $key) {
                // loops through each key in associative array
                // reads first element (start)
                if (Item::$data_ranges[$key][array_key_first(Item::$data_ranges[$key])] > $cpu->$key) { // current cpu's data is lower
                    Item::$data_ranges[$key][array_key_first(Item::$data_ranges[$key])] = $cpu->$key; // set as new lowest value
                }
                // reads last element (end)
                if (Item::$data_ranges[$key][array_key_last(Item::$data_ranges[$key])] < $cpu->$key) { // current cpu's data is higher
                    Item::$data_ranges[$key][array_key_last(Item::$data_ranges[$key])] = $cpu->$key; // set as new highest value
                }
            }
        }

        // echo "<br>";
        // echo "<br>";
        // echo "<br>";
        // echo "<br>";
        // echo "<br>";
        // echo "<br>";
        // foreach(Item::$data_ranges as $k => $v) {
        //     echo $k;
        //     foreach($v as $y) {
        //         echo $y . ",";
        //     }
        // }

        foreach(Item::$data_ranges as $key => $value) {
            Item::$slider_ranges[$key . "-start"] = $value[array_key_first($value)];
            Item::$slider_ranges[$key . "-end"] = $value[array_key_last($value)];
        }

        if (Item::$slider_ranges["boosted_frequency-start"] < Item::$slider_ranges["frequency-start"]) {
            Item::$slider_ranges["frequency-start"] = Item::$slider_ranges["boosted_frequency-start"];
        }
        if (Item::$slider_ranges["boosted_frequency-end"] > Item::$slider_ranges["frequency-end"]) {
            Item::$slider_ranges["frequency-end"] = Item::$slider_ranges["boosted_frequency-end"];
        }
    }

    static function displayAll() {
        foreach (Item::$collection as $i) {
            var_dump($i);
        }
    }
    // #endregion

    // #region Instance
    public $id, $name, $price, $interaction_count, $cores, $frequency, $boosted_frequency, $image_url;

    public function __construct($id, $name, $price, $interaction_count, $cores, $frequency, $boosted_frequency) {
        $this->id = (int)$id;
        $this->name = $name;
        $this->price = (float)$price;
        $this->interaction_count = (int)$interaction_count;
        $this->cores = (int)$cores;
        $this->frequency = (float)$frequency;
        $this->boosted_frequency = (float)$boosted_frequency;
        $this->image_url = "default.png";

        if (count(explode("i", $this->name)) > 1) {
            foreach (explode("i", $this->name) as $s) {
                $next = substr($s, 0, 1);
                // i3, i5, i7, i9 cores
                if (($next == '3') ||
                    ($next == '5') ||
                    ($next == '7') ||
                ($next == '9')) {
                    $this->image_url = 'i' . $next . '.png';
                    break;
                }
            }
        }
    }

    public static function from_dict($x) {
        // for convenience
        return new Item(
            $x['id_CPU'],
            $x['model'],
            $x['harga'],
            $x['bilangan_interaksi'],
            $x['nombor_teras'],
            $x['frekuensi'],
            $x['frekuensi_tertinggi']
        );
    }
    // #endregion
}

?>