from utils.model_loader import load_model
from utils.validators import validate_input
from core.feature_builder import build_features
from core.recommender import generate_recommendations

model=load_model()

feature_cols=['total_click',
              'early_click',
              'early_active_days',
              'first_activity_day',
              'pre_course_engaged'
              ]
def predict_and_recommend(student_dict):
    validate_input(student_dict)
    input_df=build_features(student_dict)
    risk_probability=model.predict_proba(input_df)[0][1]

    if risk_probability>=0.7:
        risk_level="High"
    elif risk_probability>=0.4:
        risk_level="Medium"
    else:
        risk_level="Low"

    observations,actions=generate_recommendations(risk_probability,student_dict)

    tree_explanation=explain_tree_decision(model,input_df,feature_cols)

    result={
        'risk_probability':round(float(risk_probability),3),
        'risk_level':risk_level,
        'observations':observations,
        'recommendations':actions,
        'model_explanation':tree_explanation
    }
    return result


def explain_tree_decision(model,input_df,feature_names):
    node_indicators=model.decision_path(input_df)
    feature=model.tree_.feature
    threshold=model.tree_.threshold

    explanation=[]

    for node_id in node_indicators.indices:
        if feature[node_id]!=-2:
            fname=feature_names[feature[node_id]]
            thresh=threshold[node_id]
            val=input_df.iloc[0][fname]

            if val<=thresh:
                explanation.append(
                    f"{fname.replace('_',' ').title()}<={int(thresh)}"
                )
            else:
                explanation.append(
                    f"{fname.replace('_',' ').title()}>{int(thresh)}"
                )
    return explanation