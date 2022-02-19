import json
from joblib import load
import numpy

def handler(event,context):
    inputArr = json.loads(event['body'])
    npArr = numpy.array(inputArr)

    model = load('models/model.joblib')
    ans = model.predict(npArr)
    body = {
        "input":inputArr,
        "ans":int(ans[0])
    }
    response = {
        "statusCode":200,
        "body":json.dumps(body)
    }
    return response
