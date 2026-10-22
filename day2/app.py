from flask import Flask 
#create a flask application instance 
app = Flask(__name__) 
#__name__ is saying its flask object
#now we will start defining the routes
@app.route('/')
def home():
    """Default home page"""
    return "Hello students keep going"
@app.route('/lohitha')
def details():
    """details about lohitha"""
    return "Lohitha is a python full stack trainee at codegnan"   
@app.route('/students')
def data():
    """students info"""
    return "students are good at frontend"    
if __name__ == "__main__":
    #if port is already in use change the port numbers 
    app.run(host='0.0.0.0',
            port=5000,debug=True) 

