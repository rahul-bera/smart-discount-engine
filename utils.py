import json

def read_input(filename):
    with open(filename) as f:
        return json.load(f)

def write_output(data):
    print(json.dumps(data, indent=2))

def generate_justification(agent):
    performance = agent["performanceScore"]
    seniority = agent["seniorityMonths"]
    targets = agent["targetAchievedPercent"]
    clients = agent["activeClients"]

    if performance > 90 and seniority > 24 and targets > 90 and clients > 15:
        return "Outstanding leadership with elite sales performance"
    elif performance > 85 and seniority > 12 and targets > 80 and clients > 10:
        return "Consistently high performance and long-term contribution"
    elif performance > 70 and targets > 60:
        return "Moderate performance with potential for growth"
    elif performance < 50 and targets < 50 and clients < 5:
        return "Needs improvement across performance, targets, and client engagement"
    elif seniority > 18 and performance < 60:
        return "Veteran team member with room to boost productivity"
    elif targets > 90 and performance < 60:
        return "Strong target achievement despite lower overall performance"
    elif clients > 12 and performance < 60:
        return "High client responsibility with opportunity to scale performance"
    else:
        reasons = []
        if performance > 80:
            reasons.append("Top performer")
        if seniority > 12:
            reasons.append("Loyal contributor")
        if targets > 75:
            reasons.append("Target crusher")
        if clients > 10:
            reasons.append("Handles many clients")
        return ", ".join(reasons) or "General contribution with stable output"
