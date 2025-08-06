import unittest
from allocator import allocate_discounts_featurewise

class TestDiscountAllocator(unittest.TestCase):
    def test_seven_agents_fixed_kitty(self):
        agents = [
            { "id": "A1", "performanceScore": 90, "seniorityMonths": 18, "targetAchievedPercent": 85, "activeClients": 12 },
            { "id": "A2", "performanceScore": 70, "seniorityMonths": 6,  "targetAchievedPercent": 60, "activeClients": 8 },
            { "id": "A3", "performanceScore": 50, "seniorityMonths": 12, "targetAchievedPercent": 70, "activeClients": 10 },
            { "id": "A4", "performanceScore": 40, "seniorityMonths": 8,  "targetAchievedPercent": 50, "activeClients": 5 },
            { "id": "A5", "performanceScore": 85, "seniorityMonths": 20, "targetAchievedPercent": 95, "activeClients": 15 },
            { "id": "A6", "performanceScore": 65, "seniorityMonths": 5,  "targetAchievedPercent": 45, "activeClients": 6 },
            { "id": "A7", "performanceScore": 55, "seniorityMonths": 10, "targetAchievedPercent": 72, "activeClients": 9 }
        ]
        result = allocate_discounts_featurewise(10000, agents)
        self.assertEqual(sum([x['total'] for x in result['allocations']]), 10000)

if __name__ == "__main__":
    unittest.main()
