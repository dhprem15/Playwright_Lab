# valid_palindrome.py - Turing Screening (Two-Pointer Technique O(1) Space)

def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        # ఎడమవైపు అక్షరం లేదా సంఖ్య కాకపోతే ముందుకు జరపడం
        while left < right and not s[left].isalnum():
            left += 1

        # కుడివైపు అక్షరం లేదా సంఖ్య కాకపోతే వెనక్కి జరపడం
        while left < right and not s[right].isalnum():
            right -= 1

        # అక్షరాలను లోయర్‌కేస్‌లోకి మార్చి సరిపోల్చడం
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

# టెస్ట్ వెరిఫికేషన్
case_1 = "A man, a plan, a canal: Panama"
case_2 = "race a car"

print(f"Case 1 ('{case_1}') -> Result:", is_palindrome(case_1))
print(f"Case 2 ('{case_2}') -> Result:", is_palindrome(case_2))