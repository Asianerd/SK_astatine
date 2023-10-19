function like_entity(id) {
    var raw_cookies = decodeURIComponent(document.cookie).split("; ");
    cookies = {};
    raw_cookies.forEach(element => {
        // key = first value
        // value = everything else
        cookies[element.split("=")[0]] = element.split("=").slice(1).join("=");
        // need to slice and join for the value due to edgecases like '=' in the username
        // user_id=1 -> 'user_id', '1'
        // login_username=test>>{}|?<=!@#!12310871 -> 'login_username', 'test>>{}|?<=!@#!12310871'
    });

    // guard clause if no user_id
    if (cookies['user_id'] == undefined) {
        // shows login popup if not logged in
        toggleLoginPopup();
        return;
    }

    var entity = document.querySelector(`#instantiated_entity_${id}`); // fetch dom item with same id
    entity.ariaLabel = entity.ariaLabel == "liked" ? "" : "liked"; // sets label to liked/unliked

    document.querySelector(`#instantiated_entity_${id} #like_indicator`).src = '../assets/logos/' + (entity.ariaLabel == 'liked' ? '' : 'white_') + 'heart_filled.png';
    // updates heart icon
    // filled heart = liked
    // unfilled heart = unliked
    var like_amount = document.querySelector(`#instantiated_entity_${id} #like_amount`);
    like_amount.innerHTML = parseInt(like_amount.innerHTML) + (entity.ariaLabel == 'liked' ? 1 : -1);
    // increments like amount by 1/-1

    var http = new XMLHttpRequest();
    http.onreadystatechange = function() {
        if ((this.readyState == 4) && (this.status == 200)) {
            // everything went well
            console.log(this.responseText);
        }
    }

    http.open("POST", `../server/like_cpu.php`, true);
    http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    http.send(`user=${cookies['user_id']}&cpu=${id}&action=${entity.ariaLabel == "liked" ? 1 : 0}`);
    // send request to backend for like event
    // sent to like_cpu.php file
}
