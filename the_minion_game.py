# The main game logic
def minion_game(s):
  s = s.upper()
  string_length = len(s)
  stuart_score = 0
  kevin_score = 0

  # Iterate over each letter of the stdin input
  for i in range(string_length):
    # Check if char s[i] is constant
    if constant_checker(s[i]):
      # Add to the current score the number of character
      # of the string slice s[i : len(s) - i]
      stuart_score += string_length - i

    # Check if char s[i] is vowel
    if vowel_checker(s[i]):
      # Add to the current score the number of character
      # of the string slice s[i : len(s) - i]      
      kevin_score += string_length - i

  announce_winner(stuart_score, kevin_score)           

# Function to evaluate and print winner
def announce_winner(stuart_score, kevin_score):
  if kevin_score == stuart_score:
    print("Draw")
  else:
    # Create dictionary:
    # key: score as integer
    # value: name as string
    scores = {stuart_score: "Stuart", kevin_score: "Kevin"}
    # Determine winner with the max function
    winner = {scores.get(max(scores)): max(scores)}
    # print winner as key-value pair
    print(list(winner.keys())[0], list(winner.values())[0])    

# Function to check if given arg letter is vowel
def vowel_checker(letter):
  vowels = ['A', 'E', 'I', 'O', 'U']
  if letter in vowels:
    return True
  return False

# Function to check if given arg letter is constant
def constant_checker(letter):
  constants = ['B', 'C', 'D', 'F', 'G',
    'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q',
    'R', 'S', 'T', 'V', 'X', 'Z', 'W', 'Y']
  if letter in constants:
    return True
  return False   

if __name__ == '__main__':
  s = input("Enter string: ")
  minion_game(s)
  