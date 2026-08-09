import pandas as pd

def build_features(student_dict):
    df=pd.DataFrame([student_dict])

    features=["total_click",
              'early_click',
              'early_active_days',
              'first_active_day',
              'pre_course_engaged'
              ]
    df['first_activity_day']=df['first_activity_day'].fillna(999)

    df=df[features].fillna(0)

    return df