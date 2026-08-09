from utils.path_utils import CONFIG_PATH
import yaml

with open(CONFIG_PATH/"config.yaml") as f:
    THRESHOLDS=yaml.safe_load(f)

def generate_recommendations(risk_probability,student_input):
    observations=[]
    actions=[]

    if student_input['early_active_days']==0:
        observations.append("No engagement in early course period")
        actions.append("Start with introductory materials immediately.")
    if student_input['early_click']<THRESHOLDS['early_engagement']['min_early_click']:
        observations.append("Low early interaction with course content")
        actions.append("Watch intro videos and explore course structure")

    first_activity = student_input.get('first_activity_day', student_input.get('first_active_day', 0))
    if first_activity > 0:
        observations.append("Late course start compared to peers")
        actions.append("Follow a structured 7-day recovery plan")
    if risk_probability>=THRESHOLDS['risk_levels']['high']:
        actions.append("Schedule academic support or mentoring session")

    return observations,actions