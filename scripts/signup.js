var inputFields = {}; // hashmap of <name, dom obj>
var inputData = {}; // hashmap of   <name, text in input field>
var statusText = document.getElementById("status");
var regexTable = {
    "Nama perlu antara 8 hingga 32 aksara panjang.":["name", /^[\s\S]{8,32}$/], // all whitespace and non-whitespace characters, amount between 8-32

    "Username perlu antara 8 hingga 32 aksara panjang.":["username", /^[\s\S]{8,32}$/],
    "Username tidak boleh mempunyai jarak aksara atau aksara unik. (!,@,#,$,%,^,etc)":["username", /^[a-zA-Z0-9_\.]+$/], // checks a-z, A-Z, 0-9, _ and .

    "Kata laluan perlu mempunyai sekurang-kurangnya satu huruf besar.":["password",/(?=.*[A-Z])/],          // checks A-Z
    "Kata laluan perlu mempunyai sekurang-kurangnya satu huruf kecil.":["password",/(?=.*[a-z])/],          // checks a-z
    "Kata laluan perlu mempunyai sekurang-kurangnya satu nombor.":["password",/(?=.*[0-9])/],               // checks 0-9
    "Kata laluan perlu mempunyai sekurang-kurangnya satu tanda baca.":["password",/(?=.*[-+_!@#$%^&*.,?])/],// checks if has one of these: -+_!@#$%^&*.,?
    "Kata laluan perlu antara 4 hingga 8 aksara panjang.":["password", /^[\s\S]{4,8}$/],                    // amount between 4-8
    "Kata laluan tidak boleh mempunyai jarak aksara.":["password", /(?=.*\s)/]                              // checks whitespace characters, amount greater than 0
};

var passwordCriterias = document.querySelectorAll("#password_criteria > div > img");
var passwordRegex = [
    /^[\s\S]{4,8}$/,
    /(?=.*[A-Z])/,
    /(?=.*[a-z])/,
    /(?=.*[0-9])/,
    /(?=.*[-+_!@#$%^&*.,?])/,
    /(?=.*\s)/
];

[...document.getElementsByClassName("signup_inputField")].forEach(function (value, i) {
    // adding DOM objects to inputFields dict
    inputFields[[
        "name",
        "username",
        "password",
        "confirm_password"
    ][i]] = value;
    // output:
    // {
    //      "name": obj
    //      "username": obj
    //      "password": obj
    //      "confirm_password": obj
    // }
});

function onPasswordUpdate() {
    console.log("form changed");
    passwordRegex.forEach(function(value, index) {
        passwordCriterias[index].src = `./assets/logos/${
            // sets image based on the output of regex expression
            (index == 5 ?
                !!value.test(inputFields["password"].value) :
                !value.test(inputFields["password"].value)) ? "cross" : "check"
            // same as
            //  if index == 5 {
            //      if !!value.test(inputFields["password"].value) {
            //          image = cross
            //      } else {
            //          image = check
            //      }
            //  } else {
            //      if !value.test(inputFields["password"].value) {
            //          image = cross
            //      } else {
            //          image = check
            //      }
            //  }
        }.png`
    })
}

onPasswordUpdate();

function validateForm() {
    // ran on form submit
    // return false when form doesnt pass all regex checks
    var _result = false;
    ["name", "username", "password", "confirm_password"].forEach(element => {
        // copy data from inputFields into inputData
        inputData[element] = inputFields[element].value; // sets values in inputData for ease of use
        if (!!inputData[element]) {
            // bang bang operator
            // converts empty string to false, then inverts it to true
            // converts occupied string to true, then inverts it to false

            // if the value is empty, break
            _result = true;
            // sadly cant return from inside foreach so this is a workaround
            // if the loop is broken, not all inputData elements will be updated as well
        }
    })
    statusText.innerHTML = ""; // clear the status text
    if (!_result) {
        // if all 4 input fields are empty, return false
        // dont set status text if all 4 fields are empty
        return false;
    }

    /*
    reference for password regex : /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-])$/
        one uppercase
        one lowercase
        one number
        one special character

        no spaces
     */

    // use regex to check validity
    for(let [key, value] of Object.entries(regexTable)) {
        // if (regex .test( text in inputField ))
        //      statusText.innerHTML = error text
        
        // edge case for space detection
        if ((key == "Kata laluan tidak boleh mempunyai jarak aksara.") ^ (!value[1].test(inputData[value[0]]))) {
            // bitwise XOR operator
            //      1 ^ 1 = false
            //      0 ^ 1 = true
            //      1 ^ 0 = true
            //      0 ^ 0 = false
            // if key == "Password must not include spaces.", then inverts the next condition
            statusText.innerHTML = key;
            return false;
        }
    }

    if (inputData["password"] != inputData["confirm_password"]) {
        statusText.innerHTML = "Kata laluan mesti sama."
        return false;
    }

    return true;
}
