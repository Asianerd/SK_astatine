var inputFields = {};
var inputData = {};
var statusText = document.getElementById("status");
var regexTable = {
    "Name must be between 8 to 32 characters long.":["name", /^[\s\S]{8,32}$/], // all whitespace and non-whitespace characters, amount between 8-32

    "Username must be between 8 to 32 characters long.":["username", /^[\s\S]{8,32}$/],
    "Username must not have spaces or special characters. (!,@,#,$,%,^,etc)":["username", /^[a-zA-Z0-9_\.]+$/], // checks a-z, A-Z, 0-9, _ and .

    "Password must have at least one uppercase letter":["password",/(?=.*[A-Z])/],          // checks A-Z
    "Password must have at least one lowercase letter":["password",/(?=.*[a-z])/],          // checks a-z
    "Password must have at least one number":["password",/(?=.*[0-9])/],                    // checks 0-9
    "Password must have at least one special character":["password",/(?=.*[-+_!@#$%^&*.,?])/],  // checks if has one of these: -+_!@#$%^&*.,?
    "Password must be between 8 to 32 characters long.":["password", /^[\s\S]{8,32}$/],
    "Password must not include spaces.":["password", /[\S]{0,}/]                            // checks whitespace characters, amount greater than 0
};

[...document.getElementsByClassName("signup_inputField")].forEach(function (value, i) {
    // adding DOM objects to inputFields dict
    inputFields[[
        "name",
        "username",
        "password",
        "confirm_password"
    ][i]] = value;
});

function onFormChange() {

}

function validateForm() {
    // ran on form submit
    var _result = false;
    ["name", "username", "password", "confirm_password"].forEach(element => {
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
        if (!value[1].test(inputData[value[0]])) {
            statusText.innerHTML = key;
            return false;
        }
    }

    if (inputData["password"] != inputData["confirm_password"]) {
        statusText.innerHTML = "Passwords must be the same."
        return false;
    }

    return true;
}

/*
!Testuser1

 */
