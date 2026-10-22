from flask import Flask,redirect,render_template,url_for,request
#create a flask application instance
app = Flask(__name__)
@app.route('/')
#name = saketh,email = saketh@codegnan.com
#GET --> fetching the data from db
#POST --> store the data in db, forms
#PUT --> update the data (entire row)
#DELETE --> delete the data (entrie row)
#PATCH --> update a specific column in a row 
def home():
    #return f'Flask server is running'
    return render_template("index.html")
#name  = lohitha,email = lohithasai119@gmail.com
@app.route('/getData',methods=['GET'])
def getData():
    name = request.args.get('name')
    email = request.args.get('email')
    return f'The name is {name} and email is {email}'

@app.route('/postData',methods=['POST'])
def postData():
    data = request.get_json()
    name = data['name']
    email = data['email']
    return f'The name is {name}, email is {email}'

@app.route('/GetDataFromPost',methods=['POST'])
def GetDataFromPost():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    if name is None or len(name) < 5:
        return render_template('index.html',
                                err="Invalid name")
    if email is None:
        return render_template('index.html',
                                err="Invalid email")
    if password is None or len(password) < 4:
        return render_template('index.html',
                                err="password is wrong")                            
    return render_template('index.html',
                            msg="Successful")

@app.route('/updateData/<email>',methods=['PUT'])
def updateData(email):
    data = request.get_json()
    email1 = data['email'] 
    print(email1)
    #database logic for PUT
    return f"Data is upadated Successfully for {email}"

@app.route('/deleteData/<email>',methods=['DELETE'])    
def deleteData(email):
    #database logic for DELETE
    return f"Data is deleted successfully for {email}"

@app.route('/register',methods=['GET','POST'])
def register():
    #here we will mention our condition it can be
    #either GET or POST 
    if request.method == "GET":
        name = request.args.get('name')
    if request.method == "POST":
        data = request.get_json()
        #in POST method we will store the data in JSON
        name = data['name']
    return f'The name is {name}'    

if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5003,debug=True)    

#hash values are hexa decimal values (0-f)