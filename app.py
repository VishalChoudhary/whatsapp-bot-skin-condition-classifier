from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse,Message
from twilio.rest import Client
from controller.util import driver

app = Flask(__name__)

client_SID = "AC07b717405115f000412bae282aaead25"
authToken = "fd7bfea8a710454cd6d6b40623e769f4"

def disease():
    nv= 'Melanocytic nevi (nv)'
    mel= 'Melanoma (mel)'
    bkl= 'Benign keratosis-like lesions (bkl)'
    bcc= 'Basal cell carcinoma (bcc)'
    akiec= 'Actinic keratoses (akiec'
    vasc= 'Vascular lesions (vasc)'
    df='Dermatofibroma (df)'

client = Client(client_SID,authToken)
@app.route("/bot",methods=["POST"])
def bot():
    sender = request.values.get("From")
    if request.values['NumMedia'] != '0' :
        img_url = request.values['MediaUrl0']
        body = driver(img_url) 
    else:
        body="Please upload a *single* image of the affected area"
    message = client.messages.create(to=sender,from_="whatsapp:+14155238886",body=body)
    # print(resp)
    return str(message)    
    

if __name__=="__main__":
    app.run(debug=True)
