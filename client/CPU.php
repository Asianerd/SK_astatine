<?php

class Item {
    // #region Statics
    public static array $collection;

    public static function initialize() {
        Item::$collection = array();

        $db = new mysqli($hostname='localhost', $username='astatine', $password='temp', $database='astatine_data');

        foreach($db->query('SELECT * FROM `cpu`') as $row) {
            array_push(Item::$collection, Item::from_dict($row));
        }

        // fetch all items
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
            $x['CPU_id'],
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