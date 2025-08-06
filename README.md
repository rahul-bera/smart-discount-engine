# Smart Discount Allocation Engine

Distributes a ₹10,000 kitty among sales agents based on:
- `performanceScore`
- `seniorityMonths`
- `targetAchievedPercent`
- `activeClients`

Each feature gets ₹2,500. Agents earn proportionally based on their scores.

---

##  Features
- Fair, mathematical distribution
- Feature-wise breakdown
- Professional justifications
- Easy JSON-based input

---

##  Run the Project

```bash
python main.py
```

You’ll get:
- Agent ID
- Total discount
- Breakdown per feature
- Justification

---

##  Run Tests

```bash
python test_engine.py
```

---

##  Add Agents

Edit `sample_input.json`:

```json
{ "id": "A9", "performanceScore": 72, "seniorityMonths": 10, "targetAchievedPercent": 80, "activeClients": 9 }
```

---

## 📌 Use Cases
- Internal reward systems
- Recruiter tools
- Transparent field performance reviews