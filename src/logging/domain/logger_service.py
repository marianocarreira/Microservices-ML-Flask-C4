
def getLogs():
    return {"msg": "Return data to requester"}

def postLog(json):
    value = json['key']
    return {"msg": f"Post data with input: {value}"}