
#omise basic checkout


from flask import Flask, render_template, request, abort, redirect, url_for, session
import os
import omise
import uuid
app = Flask(__name__)

PUBLIC_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
SECRET_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"


@app.route('/')
def index():
    return render_template('xxx.html', key=PUBLIC_KEY)

@app.route("/charge", methods=["POST"])
def charge():
    token = request.form.get("omiseToken")
    source = request.form.get("omiseSource")
    omise.api_secret = SECRET_KEY
    amount = 12345
    order_id = uuid.uuid4()
    charge = omise.Charge.create(
      amount=amount,
      currency="jpy",
      description=str(order_id),
      card=token
    )
    return("ok")



if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
