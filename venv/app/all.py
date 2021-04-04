from flask import Blueprint,request,jsonify
import os
import json
import requests
from .task import make_file,read_csv
from celery.task.control import inspect

bp = Blueprint("all",__name__)

@bp.route("/")
def index():
    return "Hello"

@bp.route("/<string:fname>/<string:content>")
def makefile(fname,content):
    fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),fname)
    print(fpath)
    make_file.delay(fpath,content)
    return f"Find your file @ <code>{fpath}</code>"
@bp.route('/api/read_csv/',methods=['GET','POST'])
def readcsv():
    content = request.get_json()
    task_Id= read_csv.apply_async(args=[content])
    print('Queue Id:',task_Id)
    return ""
@bp.route('/api/curlrequest/',methods=['GET','POST'])
def curlrequest():
    # import pdb,pdb.set_trace()
    url="http://localhost:5000/api/read_csv/"
    location=['Noida','Delhi','Gurgaon','Pune','Mumbai']
    for loc in location:
        data={'csv_name':'Asset_'+loc,'Location':loc,'row_count':1000,'message':done}
        headers = {'Content_type':'application/json','Accept':'text/plain'}
        r = requests.post(url,data=json.dumps(data),headers=headers)
        r.status_code
        return ""
    