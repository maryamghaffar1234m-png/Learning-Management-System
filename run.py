from flask import Flask
from backend.routes.auth import auth_bp
from backend.routes.courses import course_bp
from backend.routes.student import student_bp   # Musfira ka module
from backend.routes.teacher import teacher_bp   # Maham ka module
from backend.database import init_db

app = Flask(__name__)

# Database setup
init_db()

# Blueprints register karein
app.register_blueprint(auth_bp)
app.register_blueprint(course_bp)
app.register_blueprint(student_bp)
app.register_blueprint(teacher_bp)

if __name__ == '__main__':
    app.run(debug=True)
    
    