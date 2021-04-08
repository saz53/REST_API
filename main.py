from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get('/currenttime')
def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%A %B %d, %H:%M:%S")
    return {'time': current_time} #return in json format