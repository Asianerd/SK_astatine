<?php

class Item {
    // #region Statics
    public static array $collection; // holds all cpu items
    public static array $slider_ranges;
    static array $data_ranges;

    public static function initialize() {
        Item::$collection = array();
        Item::$slider_ranges = [];
        Item::$data_ranges = [
            // for the start and end of the slider range
            "cores" => [2^32, 0],
            "frequency" => [2^32, 0.0],
            "boosted_frequency" => [2^32, 0.0],
            "price" => [2^32, 0]
        ];
        

        // connect to database
        $db = new mysqli($hostname='localhost', $username='astatine', $password='temp', $database='astatine_data');
        
        // loop through every cpu in database
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
    public $id, $name, $price, $interaction_count, $cores, $frequency, $boosted_frequency;

    public function __construct($id, $name, $price, $interaction_count, $cores, $frequency, $boosted_frequency) {
        $this->id = $id;
        $this->name = $name;
        $this->price = $price;
        $this->interaction_count = $interaction_count;
        $this->cores = $cores;
        $this->frequency = $frequency;
        $this->boosted_frequency = $boosted_frequency;
    }

    public static function from_dict($x) {
        // for convenience
        return new Item(
            $x['cpu_id'],
            $x['name'],
            $x['price'],
            $x['interaction_count'],
            $x['cores'],
            $x['frequency'],
            $x['boosted_frequency']
        );
    }
    // #endregion
}

?>