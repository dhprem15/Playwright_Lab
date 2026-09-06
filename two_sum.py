# two_sum.py - Turing Coding Assessment (Optimized O(N) Hash Map)

def two_sum(nums: list[int], target: int) -> list[int]:
    # చూసిన సంఖ్యలు, వాటి ఇండెక్స్‌లను నిల్వ చేసే హ్యాష్ మ్యాప్
    seen_numbers = {}

    for current_index, current_num in enumerate(nums):
        complement = target - current_num

        # కావలసిన జత ఇప్పటికే హ్యాష్ మ్యాప్‌లో ఉందో లేదో O(1) సమయంలో చూస్తాం
        if complement in seen_numbers:
            return [seen_numbers[complement], current_index]

        # లేకపోతే ప్రస్తుత సంఖ్యను, దాని ఇండెక్స్‌ను మ్యాప్‌లో రాసుకుంటాం
        seen_numbers[current_num] = current_index

    return []

# టెస్ట్ వెరిఫికేషన్
test_nums = [2, 7, 11, 15]
test_target = 9
result = two_sum(test_nums, test_target)

print(f"Target: {test_target}")
print(f"Input Array: {test_nums}")
print(f"Result Indices: {result}")