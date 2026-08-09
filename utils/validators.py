
REQUIRED_FIELDS=['total_click',
                 'early_click',
                 'early_active_days',
                 'pre_course_engaged'
                 ]

def validate_input(student_dict):
    missing=[k for k in REQUIRED_FIELDS if k not in student_dict]
    if 'first_activity_day' not in student_dict and 'first_active_day' not in student_dict:
        missing.append('first_activity_day')
    if missing:
        raise ValueError(f"Missing required fields: {missing}")