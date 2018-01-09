import random
from flask import Flask
from flask import abort
from flask import request
import time
app = Flask(__name__)

ok_response = {'msg':'Ok', 'code':200}
error_responses = [
    {'msg':'Error', 'code':400},
    {'msg':'Error', 'code':401},
    {'msg':'Error', 'code':403},
    {'msg':'Error', 'code':404},
    {'msg':'Error', 'code':500},
    {'msg':'Error', 'code':501},
    {'msg':'Error', 'code':502},
    {'msg':'Error', 'code':503},
    {'msg':'Error', 'code':504},
    ]

@app.route("/", methods=['GET', 'POST'])
def rand():
    pct = request.args.get('pct_errors') or 0
    max_timeout = request.args.get('max_timeout') or 0
    max_timeout = int(max_timeout)
    if max_timeout != 0:
        time.sleep(random.randint(1,max_timeout))
    pct = int(pct)
    if pct == 0:
        return ok_response['msg'], ok_response['code']
    else:
        if random.randint(0,100) <= pct:
            res = random.choice(error_responses)
            abort(res['code'])
        else:
            return ok_response['msg'], ok_response['code']

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001)