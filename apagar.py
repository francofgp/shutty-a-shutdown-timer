import os
from datetime import datetime, timedelta


while True:
    shutdown = input(
        "Input the time in seconds to shutdown your computer, press 'exit' to abandon: ")

    if shutdown == 'exit':
        exit()

    else:
        try:
            seconds = int(shutdown)
            time = datetime.now() + timedelta(seconds=seconds)

            print(
                f"your computer will shutdown at {str(time)[:-7]}")
            os.system(f"shutdown /s /t {shutdown}")
            break
        except Exception:
            print("That's not an valid number or command!")
