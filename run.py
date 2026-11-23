from flask import Flask
from backend.routes.auth import auth_bp
from backend.routes.courses import course_bp
from backend.database import init_db  # <-- Yeh line zaroori hai

app = Flask(__name__)

# Database aur tables banane ke liye yeh function call karna zaroori hai
init_db()  # <-- Yeh line tables banayegi

# Authentication aur Course dono ko register karein
app.register_blueprint(auth_bp)
app.register_blueprint(course_bp)

if __name__ == '__main__':
    app.run(debug=True)
    
    