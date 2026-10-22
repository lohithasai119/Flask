from flask import Flask
import uuid
app = Flask(__name__)
#build a student routing app
#student default page
#student id 
#student attendence
#file path
#student uuid 
@app.route('/')
def home():
    return "welcome to the pfs-4 batch"
@app.route('/student_id/<uuid:stu_id>')
def student_id(stu_id):
    return f'The search for student is {stu_id}' 
@app.route('/attendence/<float:stu_attendence>')
def stu_att(stu_attendence):
    return f'The student attendance is {stu_attendence}'    
@app.route('/skills/<s1>/<s2>')
def skills(s1,s2):
    return f'student has {s1} and {s2} skills'  
@app.route('/details/<path:file_path>')
def details(file_path):
    return f'The path is {file_path}'      
@app.route('/search_studentid')
def generate():
    id = uuid.uuid4().hex
    print(id)
    return f'The student search is:{id}'   
if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5002,debug=True)     