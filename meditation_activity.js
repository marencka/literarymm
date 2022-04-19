// for mins default is 2
// NEVER SET TO 0 -> IT WILL BREAK THE LOGIC RESPONSIBLE TO COUNTING AND SET TIMER TO 1 HR
let mins = 1; 
let future_time = new Date(new Date().getTime() + mins*60000);

let myfunc = setInterval(function() {
    // code goes here
    let curr_time = new Date();
    let left_time = new Date(future_time - curr_time);
    let minutes = left_time.getMinutes();
    let secs = left_time.getSeconds();

    let time_str = "0" + minutes + ":"    
    if (secs < 10) {
        time_str += "0" + secs;
    } else {
        time_str += secs;
    }
    console.log(time_str);

    document.getElementById("timer").innerHTML = time_str;

    if ((minutes==0) && (secs == 0)) {
        document.getElementById('reflect_button').classList.add('show_button');
        interaction();
        clearInterval(myfunc);
    }
}, 1000);

function interaction() {
    const reflect_button = document.getElementById('reflect_button');
    const modal_container = document.getElementById('modal_container');
    const later_button = document.getElementById('later_button');
    const submit_button = document.getElementById('submit_button');

    reflect_button.addEventListener('click', () => {
        modal_container.classList.add('show');
    });

    later_button.addEventListener('click', () => {
        modal_container.classList.remove('show');
    });

// TODO: add code to submit_button to send info to the server
}