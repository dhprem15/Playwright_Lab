# first_unique_char.py - Turing Coding Assessment (Two-Pass Hash Map O(N))

def first_uniq_char(s: str) -> int:
    char_counts = {}

    # పాస్ 1: ప్రతి అక్షరం ఎన్నిసార్లు వచ్చిందో లెక్కించడం
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # పాస్ 2: కౌంట్ 1 ఉన్న మొదటి అక్షరం ఇండెక్స్‌ను కనుగొనడం
    for index, char in enumerate(s):
        if char_counts[char] == 1:
            return index

    # పునరావృతం కాని అక్షరం లేకపోతే -1 రిటర్న్ చేయడం
    return -1

# టెస్ట్ వెరిఫికేషన్
print("Test 1 ('leetcode'):", first_uniq_char("leetcode"))
print("Test 2 ('loveleetcode'):", first_uniq_char("loveleetcode"))
print("Test 3 ('aabb'):", first_uniq_char("aabb"))