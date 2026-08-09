
REQUIRED_FIELS=['total_click',
                'early_click',
                'first_activity_day',
                'pre_course_engaged'
                ]

def validate_input(student_dict):
    missing=[k for k in REQUIRED_FIELS if k not in student_dict]
    if missing:
        raise ValueError(f"Missing required fields: {missing}")