window.onload = function () {
    let day = new Date().getDay();
    // 0 - sunday, 1 - monday, 2 - tuesday, 3 - wednesday, 4 - thursday, 5 - friday, 6 - saturday
    let isFriday = false;
    if (day != 5) {
        disableButton(day);
    } else {
        document.getElementById('disabled_msg').remove();
    }

    function disableButton(day) {
        if (day == 5) {
            return;
        }

        let pdpr_button = document.getElementById('pdpr');

        if ((typeof (pdpr_button) == 'undefined') || (pdpr_button == null)) {
            return;
        }
        pdpr_button.disabled = 'true';
        pdpr_button.style.backgroundColor = "rgba(82, 114, 110, 0.8)";
    }

};