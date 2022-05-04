/**
 * Writen by Iuliia (Julia) Poliakova
 * Meditation Activity is responsible for maintaining the timer counting down the end of the meditation activity
 * Once the timer runs out, the button for submission of the reflection appears to allow to submit the reflection
 */

/**
 * Input Type: Integer
 * 0 is invalid input, which will break the logic, causing the timer to be 1 hour long 
 * the `mins` variable can be used to modify the length of the timer
 */
const mins = 1; 

/**
 * future_time is date and time at which timer should stop
 */
let future_time = new Date(new Date().getTime() + mins*60000);

/**
 * myFunc is responsible for countdown of the timer
 * Updates and recalculates time left between current time and future_time every second
 * The function is called each 1000 miliseconds (same as 1 second) until the timer runs out
 */
let myfunc = setInterval(function() {
    // the current difference between the time at which timer started and at which it should end
    let curr_time = new Date();

    //uses difference in miliseconds between two dates with times to calculate remaining seconds
    let left_time = new Date(future_time - curr_time); 

    //getting minutes and seconds out of Date 
    let minutes = left_time.getMinutes();
    let secs = left_time.getSeconds();

    //formats `minutes` and `secs` into the format of timer "minutes:seconds"
    let time_str = "0" + minutes + ":"    
    if (secs < 10) {
        time_str += "0" + secs;
    } else {
        time_str += secs;
    }

    //inserts time_str with current timer value into the meditation html page
    document.getElementById("timer").innerHTML = time_str;

    //once timer runs out, the button is shown with the help of the class "show_button"
    if ((minutes==0) && (secs == 0)) {
        document.getElementById('reflect_button').classList.add('show_button');
        clearInterval(myfunc);
    }
}, 1000);
