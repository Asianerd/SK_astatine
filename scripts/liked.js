function updateEntityList() {
    var http = new XMLHttpRequest(); // create new http request
    http.onreadystatechange = function() {
        if ((this.readyState == 4) && (this.status == 200)) {
            // if there isnt any error from http, set the container innerhtml
            document.getElementsByClassName("query-result")[0].innerHTML = this.response;
        }
    }

    http.open("GET", `../server/fetch_cpu.php?request-mode=liked`, true);
    http.send();
    // send it to the fetch_cpu.php file
}

updateEntityList();
