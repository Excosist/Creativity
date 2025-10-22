from win11toast import toast
from datetime import datetime
import time

while True:
    f = toast('Hi', 'Did you drink water?', buttons= ["Yes", "No"])

    if f.get("arguments") == 'http:Yes':
        now = datetime.now()
        current_date = now.date()
        current_time = now.time()
        print(f"yes at {current_date} {current_time}")
        toast('😊', 'Keep it up!')

    elif f.get("arguments") == 'http:No':
        now = datetime.now()
        current_date = now.date()
        current_time = now.time()
        print(f"no at {current_date} {current_time}")
        toast('😤', 'Do it next time!!')
    
    time.sleep(1800)