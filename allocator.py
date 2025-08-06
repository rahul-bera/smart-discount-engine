from utils import generate_justification

def allocate_discounts_featurewise(site_kitty, agents):
    fields = [
        "performanceScore",
        "seniorityMonths",
        "targetAchievedPercent",
        "activeClients",
        "customerFeedback",
        "bonusClosedDeals"
    ]

    num_fields = len(fields)
    split_amount = site_kitty / num_fields

    agent_map = {agent["id"]: 0 for agent in agents}

    for field in fields:
        total = sum(agent[field] for agent in agents)
        for agent in agents:
            if total == 0:
                share = split_amount / len(agents)
            else:
                share = (agent[field] / total) * split_amount
            agent_map[agent["id"]] += share

    allocations = []
    for agent in agents:
        final_amount = round(agent_map[agent["id"]], 2)
        allocations.append({
            "id": agent["id"],
            "assignedDiscount": final_amount,
            "justification": generate_justification(agent)
        })

    total_alloc = sum(a["assignedDiscount"] for a in allocations)
    diff = int(site_kitty - total_alloc)
    if diff != 0:
        allocations[0]["assignedDiscount"] += diff

    return {"allocations": allocations}