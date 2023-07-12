from datetime import datetime


def is_time_after_current(time_string):
    try:
        input_time = datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")
        current_time = datetime.now()

        if input_time > current_time:
            return True
        else:
            return False
    except ValueError:
        return False
# print(is_time_after_current())