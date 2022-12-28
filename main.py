def acronym():
  userInput = input("Please provide a phrase to turn into an acronym: ")

  ### Optional Exclusions
  exclusions = userInput.replace("and","")
  wordArr = exclusions.split(' ')

  acronym = ""
  for word in wordArr:
    if(word != ""):
      acronym += word[0]

  acronym = acronym.upper()
  print(f'Your acronym is: {acronym}')

if __name__ == "__main__":
  while True:
    acronym()
