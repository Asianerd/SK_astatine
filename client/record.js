class Record {
    static collection = [];

    constructor (userID, itemID, time = undefined) {
        if (time == undefined) {
            this.time = 0; // set to current time
        } else {
            this.time = time;
        }

        this.userID = userID;
        this.itemID = itemID;
    }
}