# Decompose the following function and share your results via a GitHub link.
# See the function below:

import datetime

# def log_event(event_type, user_id, message):
#     """Logs an event to a file with timestamp, event type, user ID, and message."""
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     log_message = f"[{timestamp}] [{event_type}] User: {user_id} - {message}\n"
#     with open("rental_log.txt", "a") as log_file:
#         log_file.write(log_message)

def build_log_message(event_type, user_id, message):
    current_time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{current_time_stamp}] [{event_type}] User: {user_id} - {message}\n"
    return log_message

def write_to_log_file(log_message):
    with open("rental_log.txt", "a") as log_file:
        log_file.write(log_message)

    """
    Decomposed the function into two smaller sub functions.
    1st to build the log message
    2nd to write the log message to the file
    This helps to make the code more readable and easier to understand due to the separation of concerns.
    """
def log_event(event_type, user_id, message):
    log_message = build_log_message(event_type, user_id, message)
    write_to_log_file(log_message)


if __name__ == "__main__":
    log_event("login", "123456", "User logged in")