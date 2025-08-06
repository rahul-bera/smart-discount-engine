# Smart Discount Allocation Engine

A Python-based system to fairly distribute a fixed discount amount (₹10,000) among multiple sales agents based on performance-related metrics.

---

##  Approach

- The total discount kitty is split **equally across all input features**.
- For each feature, agents are awarded a **proportional share** of that portion.
- The final score is the **sum of each agent’s shares** across all features.
- Justification messages are generated based on a rule-based performance evaluation.
- Any rounding difference is adjusted by assigning the remaining amount to the first agent.

---

##  Assumptions Made

- The total kitty (₹10,000) is constant and split evenly across all features.
- All agents contain valid numeric scores for each of the following fields:
  - `performanceScore`
  - `seniorityMonths`
  - `targetAchievedPercent`
  - `activeClients`
  - `customerFeedback`
  - `bonusClosedDeals`
- The input JSON is properly formatted.
- All agents have unique `id` fields.

---

## How to Run
```

###  Run Program:
```bash
python main.py
```
You’ll be prompted to choose from 3 input test cases:
```
1. sample_input_normal.json
2. sample_input_same.json
3. sample_input_rounding.json
```


###  Output Format
```json
{
  "allocations": [
    {
      "id": "A1",
      "assignedDiscount": 4235.61,
      "justification": "Consistently high performance and long-term contribution"
    },
    ...
  ]
}
```
