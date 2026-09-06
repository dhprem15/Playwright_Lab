# valid_anagram.py - Turing Screening Task (Frequency Counter O(N))

def is_anagram(s: str, t: str) -> bool:
    # బేస్ కండిషన్: పొడవు వేరుగా ఉంటే అనగ్రామ్ అయ్యే అవకాశమే లేదు
    if len(s) != len(t):
        return False

    char_counts = {}

    # మొదటి పదం 's' లోని అక్షరాల ఫ్రీక్వెన్సీని లెక్కించడం
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # రెండవ పదం 't' లోని అక్షరాలను సరిపోల్చడం
    for char in t:
        # అక్షరం డిక్షనరీలో లేకపోయినా లేదా కౌంట్ సున్నా అయిపోయినా మ్యాచ్ కాదు
        if char not in char_counts or char_counts[char] == 0:
            return False
        char_counts[char] -= 1

    return True

# టెస్ట్ వెరిఫికేషన్
print("Case 1 ('anagram', 'nagaram'):", is_anagram("anagram", "nagaram"))
print("Case 2 ('rat', 'car'):", is_anagram("rat", "car"))
print("Case 3 ('listen', 'silent'):", is_anagram("listen", "silent"))