from flask import Flask, render_template,jsonify,request,redirect,url_for

app= Flask(__name__)
app.config['SECERET_KEY']='THISISTHESECRETKEYFORTHEAPP'

@app.route('/api/auth/register', methods = ['GET','POST'])
def regigister():
    user = {}
    users=[]
    auth= request.authorization
    
    user = request.get_json()
    users.append(user)
    return render_template('UI/signup.html')



@app.route('/api/auth/login', methods = ['GET','POST'])
def login_user():

    return render_template('login.html')


@app.route('/api/create',  methods = ['GET','POST'])
def create():
    event = request.get_json()
    events.append(event)
    j=jsonify(events)

    return render_template('create.html'),j

@app.route('/api/auth/reset-password',  methods = ['POST'])
def reset_password():

    return ""


@app.route('/api/events', methods = ['POST'])
def create_event():

    event = request.get_json()
    events.append(event)
    return jsonify(events)


@app.route('/api/events/<eventId>', methods = ['PUT'])
def update_event(eventId):

    return ""

@app.route('/api/events/<eventId>', methods = ['DELETE'])
def delete_event(eventId):
    return jsonify({'message':'event deleted'})


@app.route('/api/events', methods = ['GET'])
def retrieve_event():
    return jsonify({"message":"retrieved event"})


@app.route('/api/event/<eventId>/rsvp', methods = ['POST'])
def rsvp_event(eventId):
    return jsonify({"message":"Reserved event"})


@app.route('/api/event/<eventId>/rsvp', methods = ['GET'])
def retrieve_all_guests(eventId):
    return jsonify({"message":"retrieved guests in attendance"})

if __name__ == "__main__":
    app.run(debug=True)