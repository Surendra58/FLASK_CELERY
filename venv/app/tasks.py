from app import celery
import json
import time

@celery.task()
def make_file(fname,context):
    with open(fname,"w") as f:
        f.write(context)

@celery.task(bind=True)
def read_csv(self,jsondata):
    time.sleep(10)
    print('#'*100)
    print("I am in task queue",type(jsondata))
    # Pretty Printing JSON string back
    print(json.dumps(jsondata,indent=4,sort_keys=True))
