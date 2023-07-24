var form_container = document.getElementsByClassName("file-drop")[0];
form_container.addEventListener('change', () => {
    file_input = form_container.querySelector('input[type="file"]');
    console.log(file_input.files);
    if (file_input.files.length >= 1) {
        form_container.querySelector('label > div > div h4').innerHTML = file_input.files[0].name;
        form_container.querySelector('label > div > div h3').innerHTML = "";
        form_container.querySelector('label > div > div h2').innerHTML = "";
    }
})

document.querySelector('#log').scrollIntoView({
    behavior: 'smooth'
});

function overwrite(id, name, price, interaction, cores, freq, boosted_freq) {
    var http = new XMLHttpRequest();
    http.onreadystatechange = function() {
        if ((this.readyState == 4) && (this.status == 200)) {
            // everything went well
            console.log(this.responseText);
        }
    }

    http.open("POST", `../server/import_actions.php`, true);
    http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    http.send(`type=overwrite&id=${id}&name=${name}&price=${price}&interaction=${interaction}&cores=${cores}&freq=${freq}&boosted_freq=${boosted_freq}`);

    document.querySelector(`#instantiated_log_${id}`).className = "";
    document.querySelector(`#instantiated_log_${id} #actions`).innerHTML = "";
}

async function add_new(id, name, price, interaction, cores, freq, boosted_freq) {
    var http = new XMLHttpRequest();
    http.onreadystatechange = function() {
        if ((this.readyState == 4) && (this.status == 200)) {
            // everything went well
            console.log(this.responseText);
            document.querySelector(`#instantiated_log_${id} > td:first-child`).innerHTML = this.responseText;
        }
    }

    http.open("POST", `../server/import_actions.php`, true);
    http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    http.send(`type=add_new&id=${id}&name=${name}&price=${price}&interaction=${interaction}&cores=${cores}&freq=${freq}&boosted_freq=${boosted_freq}`);

    document.querySelector(`#instantiated_log_${id}`).className = "added_new";
    document.querySelector(`#instantiated_log_${id} #actions`).innerHTML = "";
}

function dispose(id) {
    action_tab = document.querySelector(`#instantiated_log_${id}`).innerHTML = "";
}

function overwrite_all() {
    document.querySelectorAll("#actions").forEach(element => {
        element.querySelectorAll("h2:nth-child(1)").forEach(i => {
            i.click();
        })
    });
}

function dispose_all() {
    document.querySelectorAll("#actions").forEach(element => {
        element.querySelectorAll("h2:nth-child(3)").forEach(i => {
            i.click();
        })
    });
}
