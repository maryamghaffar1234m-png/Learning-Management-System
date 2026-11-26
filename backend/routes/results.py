from flask import Blueprint, render_template

results_bp = Blueprint('results', __name__)

@results_bp.route('/results')
def view_results():
    # Mock Data (Baad mein database se connect hoga)
    student_info = {
        "name": "Musfira",
        "roll_no": "041",
        "semester": "5th"
    }
    
    # Results Data
    results_data = [
        {"course": "Software Construction", "assessment": "Assignment 1 (SCM)", "obtained": 18, "total": 20},
        {"course": "Software Construction", "assessment": "Quiz 1", "obtained": 9, "total": 10},
        {"course": "Database Systems", "assessment": "Assignment 1", "obtained": 15, "total": 20},
        {"course": "Database Systems", "assessment": "Quiz 1", "obtained": 14, "total": 15}
    ]
    
    # Teacher Feedback Data
    feedback_data = [
        {"course": "Software Construction", "teacher": "Mam Unzila", "comment": "Excellent work on the SCM plan! Keep it up."},
        {"course": "Database Systems", "teacher": "Mam Fatima", "comment": "Good attempt on the ER diagram, but you missed the cardinality constraints. Please review them."}
    ]

    # Total aur Percentage Calculate karna
    total_obtained = sum(item['obtained'] for item in results_data)
    total_max = sum(item['total'] for item in results_data)
    percentage = round((total_obtained / total_max) * 100, 1) if total_max > 0 else 0

    return render_template('results/view_results.html', 
                           student=student_info, 
                           results=results_data, 
                           feedbacks=feedback_data,
                           total_obtained=total_obtained,
                           total_max=total_max,
                           percentage=percentage)