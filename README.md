# Pomodoro Application

This project is a Pomodoro Application built using Python and the Tkinter library. It helps users improve productivity and manage their time effectively by following the Pomodoro Technique. The application provides a customizable timer for work and break intervals, allowing users to focus on tasks and take regular breaks for optimal productivity.

## Features

1. Timer: The application includes a timer that alternates between work sessions and break intervals based on the Pomodoro Technique. Users can customize the duration of work sessions and breaks according to their preferences.

2. Task Management: Users can set a task for each work session to stay focused and track their progress. The application displays the current task and remaining time for the work session.

3. Notifications: The application provides audio and visual notifications to indicate the start and end of work sessions and breaks. This helps users stay aware of the current phase even when they are not actively looking at the application.

4. Session History: The application keeps a record of completed work sessions and break intervals, allowing users to review their productivity and track their time management.

## Prerequisites

To run the Pomodoro Application, ensure you have the following:

- Python (version 3.7 or higher) installed on your computer.
- Tkinter library installed. You can install it using the following command:
  ```
  $ pip install tkinter
  ```

## Usage

1. Clone the GitHub repository or download the project files to your local machine.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the following command to start the Pomodoro Application:
   ```
   $ python main.py
   ```

4. The application window will open, displaying the default work session duration (25 minutes) and break duration (5 minutes).

5. Click the "Start" button to begin the timer. The application will start a work session and display the remaining time for the session.

6. When the work session ends, the application will notify you with an audio alert and automatically switch to the break interval. The remaining time for the break will be displayed.

7. After the break interval, the application will again notify you with an audio alert and switch back to the work session. This cycle continues until you manually stop the timer.

8. To customize the duration of the work session and break, use the respective input fields to enter the desired durations in minutes.

9. To set a task for the work session, enter the task description in the "Task" input field. The application will display the task along with the remaining time for the work session.

10. The application keeps a record of completed work sessions and break intervals. You can view the session history by clicking the "History" button. The history will be displayed in a separate window, showing the date, start time, end time, and duration of each session.

11. To exit the application, click the "Quit" button or close the application window.

## Customization

You can customize the Pomodoro Application by modifying the code in the `main.py` file. You can change the appearance, add additional features, or enhance the functionality as per your requirements.
