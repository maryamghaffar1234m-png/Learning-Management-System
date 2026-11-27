from flask import Flask
from backend.routes.auth import auth_bp
from backend.routes.courses import course_bp
from backend.routes.student import student_bp
from backend.routes.teacher import teacher_bp
from backend.routes.results import results_bp
from backend.database import init_db

app = Flask(__name__)

# Database aur tables initialize karein
init_db()

# Saare modules ke blueprints register karein
app.register_blueprint(auth_bp)
app.register_blueprint(course_bp)
app.register_blueprint(student_bp)
app.register_blueprint(teacher_bp)
app.register_blueprint(results_bp)

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    