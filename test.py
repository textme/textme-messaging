from textme_messaging.mms.message import MMSMessage, MMSMessagePage
import base64
from array import array

def cleanup_form_data(data):
    found=0
    pos = data.find("\r\n\r\n")
    if pos:
        boundpos = data.find("\r\n--_boundary",pos+4)
        if boundpos:
            dat=data[pos+4:boundpos]
            return dat
    return data

data = "b64encoded form-data"

b = cleanup_form_data(base64.b64decode(data))

print("----------")
print b
print("----------")

dat = array("B",b)

mms = MMSMessage.from_data(dat)

print mms.headers['Message-Type']  # m-send-req
print mms.smil
