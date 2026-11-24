from flask import Blueprint, render_template

teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/teacher/dashboard')
def dashboard():
    # Mock Data (Baad mein database se aayega)
    teacher_info = {
        "name": "Maham",
        "department": "Software Engineering",
        "total_courses": 3,
        "total_students": 120
    }
    
    courses = [
        {"title": "Software Construction", "students": 45, "status": "Active"},
        {"title": "Web Engineering", "students": 38, "status": "Active"}
    ]
    
    submissions_to_grade = [
        {"student": "Musfira (041)", "assessment": "SCM Plan Assignment", "course": "Software Construction"},
        {"student": "Ayesha (012)", "assessment": "ER Diagram Task", "course": "Database Systems"}
    ]
    
    recent_feedback = [
        {"student": "Musfira (041)", "comment": "Excellent work on the SCM plan!", "date": "Today"},
        {"student": "Ayesha (012)", "comment": "Please improve the database schema.", "date": "Yesterday"}
    ]

    return render_template('teacher/dashboard.html', 
                           teacher=teacher_info, 
                           courses=courses, 
                           submissions=submissions_to_grade,
                           feedback=recent_feedback)
