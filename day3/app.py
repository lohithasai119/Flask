from flask import Flask
app = Flask(__name__)
@app.route('/')
@app.route('/home/')
def home():
    return f'welcome to Day-3 learning about static vs dynamic routes'
@app.route('/profile/')
def details():
    return f'Hello this is lohitha'
#static routing --> /name/<name>
#dynamic routing --> /name/<name>
@app.route('/name/lohitha') #static route
def data():
    return f'welcome lohitha....'  
@app.route('/name/<name>')  #dynamic route 
def student_name(name):
    return f'hello {name}'
#now we want to create related to course names
@app.route('/courses/<course_name>')
def courses(course_name):
    return f'<b>This Course is:{course_name}<b/>'   
#converters --> int,str,float,path,uuid
#integer converters
@app.route('/students/<int:student_id>')
def studentid(student_id):
    return f'The ID of student is {student_id}' 
#float converters    
@app.route('/percentages/<float:percentage>')
def stupercentages(percentage):
    return f'The percentage of student is {percentage}'
#path converters     
@app.route('/path/<path:file_name>')
def filepath(file_name):
    return f'The path is {file_name}'  
#UUID --> universal unique Identifier 
@app.route('/student_id/<uuid:stu_id>')
def student_id(stu_id):
    return f'The search for student is {stu_id}'          
if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5001,debug=True)

#port range is 1 to 65535            
