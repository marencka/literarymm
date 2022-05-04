/**
 * Written by Iuliia (Julia) Poliakova
 * This JavaScript file is responsible for disabling Parkinson's Disease Report button until Friday
 * since the client requested the report to be completed only on Friday
 */
window.onload = function () {
    // Retrieves the day of the week as an integer:
    // 0 - sunday, 1 - monday, 2 - tuesday, 3 - wednesday, 4 - thursday, 5 - friday, 6 - saturday
    let day = new Date().getDay();
   
    if (day != 5) {
        disableButton(day);
    } else {
        document.getElementById('disabled_msg').remove();
    }

    function disableButton(day) {
        if (day == 5) {
            return; //if the day is Friday, then don't disable the button
        }

        let pdpr_button = document.getElementById('pdpr');
        let pdpr_class = document.getElementById('pdpr_class');

        //if the button for the report doesn't exist, that means that 
        //the current version of the website is being used by non Parkinsons disease user
        //meaning that there is nothing to be done
        if ((typeof (pdpr_button) == 'undefined') || (pdpr_button == null)) {
            return; 
        }

        //otherwise style and disable the button
        pdpr_button.disabled = 'true';
        pdpr_class.style.display = 'none';
        pdpr_button.style.backgroundColor = "rgba(82, 114, 110, 0.8)";
    }

};