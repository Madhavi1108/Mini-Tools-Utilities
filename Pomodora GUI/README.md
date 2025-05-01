# pomodora_gui

## Code Explanation

### Overview

This is a simple Pomodoro timer application built using Python's Tkinter library. The Pomodoro Technique is a time management method where work is divided into intervals (usually 25 minutes), separated by short breaks. After four work intervals, a longer break is taken. This app implements that technique with adjustable work and break times.

### Features

* **Timer Display:** Shows the countdown for work sessions, short breaks, and long breaks.
* **Pomodoro Cycle:** Alternates between work sessions and breaks based on a typical Pomodoro cycle.
* **Check Marks:** Displays check marks to track completed work sessions.
* **Start/Reset Button:** Allows the user to start the timer and reset it whenever needed.

### How to Use

1.  **Start the Timer:**
    * Click the **Start** button to begin a Pomodoro cycle.
    * The timer will count down for a work session, followed by a short break, and after every 4 work sessions, it will take a long break.

2.  **Reset the Timer:**
    * Click the **Reset** button at any time to cancel the current timer and reset the countdown to `00:00`.
    * The check marks will also be reset.

3.  **Work Sessions & Breaks:**
    * Work sessions are 30 minutes by default.
    * Short breaks are 5 minutes, and long breaks are 20 minutes.

    The cycle follows this pattern:
    * Work (30 minutes) → Short Break (5 minutes) → Work (30 minutes) → Short Break (5 minutes) → Work (30 minutes) → Short Break (5 minutes) → Work (30 minutes) → Long Break (20 minutes) → (Repeat)

4.  **Tracking Progress:**
    * The app displays check marks to show the number of completed work sessions (each pair of work sessions is followed by a break).

### Technical Details

* **Timer Mechanism:**
    The `start_timer()` function starts the timer, switching between work and break sessions. It also increments the `reps` counter, which tracks the number of completed sessions.

* **Countdown Mechanism:**
    The `count_down()` function runs the timer by decreasing the time by 1 second every time and updates the display. When the timer reaches zero, it starts the next session (either work or break).

* **UI Setup:**
    * The window is created using Tkinter, and the UI consists of a title, a canvas with a tomato image, the timer display, and buttons for starting and resetting the timer.

* **Reset Timer:**
    The `reset_timer()` function stops the timer and resets all UI elements, including the check marks.

### Customization

You can easily adjust the times for work sessions and breaks by modifying the following constants in the code:

```python
WORK_MIN = 30        # Work time in minutes
SHORT_BREAK_MIN = 5    # Short break time in minutes
LONG_BREAK_MIN = 20     # Long break time in minutes
```

Feel free to change these values to suit your needs.

### Acknowledgements

* The Pomodoro Timer concept was created by Francesco Cirillo.
* The tomato image used in the UI is assumed to be available in the same directory as the script.
```

