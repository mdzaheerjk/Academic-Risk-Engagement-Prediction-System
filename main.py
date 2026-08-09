from core.predictor import predict_and_recommend

def main():
    student_input={
        'total_click':800,
        'early_click':0,
        'early_active_days':0,
        'first_activity_day':15,
        'pre_course_engaged':0
    }
    try:
        result=predict_and_recommend(student_input)
        print(result)
    except Exception as e:
        print(f"An error occurred during analysis: {e}")

if __name__ == "__main__":
    main()