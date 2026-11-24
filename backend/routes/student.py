from flask import Blueprint, render_template

student_bp = Blueprint('student', __name__)

@student_bp.route('/student/dashboard')
def dashboard():
    # Mock Data (Baad mein database se aayega)
    student_info = {
        "name": "Musfira",
        "roll_no": "041",
        "enrolled_courses": 4,
        "pending_assignments": 2
    }
    
    courses = [
        {"title": "Software Construction", "instructor": "Mam Unzila"},
        {"title": "Database Systems", "instructor": "Mam Fatima"}
    ]
    
    materials = [
        {"title": "SCM Plan Notes", "course": "Software Construction", "type": "PDF"},
        {"title": "ER Diagram Guide", "course": "Database Systems", "type": "Doc"}
    ]
    
    assignments = [
        {"title": "SCM Plan Assignment", "course": "Software Construction", "deadline": "Nov 25, 2026"},
        {"title": "SQL Queries Task", "course": "Database Systems", "deadline": "Nov 28, 2026"}
    ]
    
    quizzes = [
        {"title": "Quiz 1: Basics of SCM", "course": "Software Construction"},
        {"title": "Quiz 1: Normalization", "course": "Database Systems"}
    ]
    
    results = [
        {"assessment": "Assignment 1 (SCM)", "marks": "18/20", "feedback": "Excellent work!"},
        {"assessment": "Quiz 1 (DB)", "marks": "15/15", "feedback": "Keep it up!"}
    ]

    return render_template('student/dashboard.html', 
                           student=student_info, 
                           courses=courses, 
                           materials=materials, 
                           assignments=assignments, 
                           quizzes=quizzes, 
                           results=results)
