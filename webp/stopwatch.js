// Define variables
let timer;
let hours = 0;
let minutes = 0;
let seconds = 0;
let milliseconds = 0;
let isRunning = false;

// Function to start the stopwatch
function start() {
    if (!isRunning) {
        timer = setInterval(runStopwatch, 10); // Update every 10 milliseconds
        isRunning = true;
    }
}

// Function to stop the stopwatch
function stop() {
    clearInterval(timer);
    isRunning = false;
}

// Function to reset the stopwatch
function reset() {
    clearInterval(timer);
    isRunning = false;
    hours = 0;
    minutes = 0;
    seconds = 0;
    milliseconds = 0;
    updateDisplay();
}

// Function to run the stopwatch
function runStopwatch() {
    milliseconds += 10;
    if (milliseconds == 1000) {
        milliseconds = 0;
        seconds++;
    }
    if (seconds == 60) {
        seconds = 0;
        minutes++;
    }
    if (minutes == 60) {
        minutes = 0;
        hours++;
    }
    updateDisplay();
}

// Function to update the display with current time
function updateDisplay() {
    let display = document.getElementById("display");
    display.textContent = 
        (hours < 10 ? "0" + hours : hours) + ":" +
        (minutes < 10 ? "0" + minutes : minutes) + ":" +
        (seconds < 10 ? "0" + seconds : seconds) + ":" +
        (milliseconds < 100 ? (milliseconds < 10 ? "00" + milliseconds : "0" + milliseconds) : milliseconds);
}
