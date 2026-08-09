import pandas as pd

def build_features(student_dict):
    data = dict(student_dict)
    # Support both 'first_active_day' and 'first_activity_day' defensively
    if 'first_active_day' in data and 'first_activity_day' not in data:
        data['first_activity_day'] = data.pop('first_active_day')

    df = pd.DataFrame([data])

    features = [
        'total_click',
        'early_click',
        'early_active_days',
        'first_activity_day',
        'pre_course_engaged'
    ]

    for col in features:
        if col not in df.columns:
            df[col] = 999 if col == 'first_activity_day' else 0

    df['first_activity_day'] = df['first_activity_day'].fillna(999)
    df = df[features].fillna(0)

    return df