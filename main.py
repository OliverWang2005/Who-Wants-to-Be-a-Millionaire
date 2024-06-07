#How to be a millionaire, most likely without visuals but potentially with. A series of questions, with 4 multiple choice answers each, each question progressively increasing in chronological order from easiest to hardest. Each question answered correctly will add to the monetary prize pool up until 1 million dollars. Single player. Will potentially have questions revolving the year of 2021. Will provide user with lifelines (computer generated hints). user can quit whenever


#FUNCTIONS 

import random

#use of a function
def generateQuestion(list_of_questions, position_of_question, list_of_answers, fifty_flag, audience_flag, phone_flag, fifty_fifty_questions, flag):
  length_of_list = len(list_of_questions)
  length_of_list = int(length_of_list)
  position_of_question = random.randint(1, length_of_list)
  position_of_question = int(position_of_question)
  position_of_question -= 1
  user_answer = input(str(list_of_questions[position_of_question]) + "\n As mentioned in the introduction, you have 3 lifelines to choose from: \n 50:50, phone-a-friend, and ask the audience \n To select 50:50, please enter \"fifty\". To phone a friend, please enter \"phone\". To ask the audience, please enter \"audience\". If you choose to use one of your lifelines, you cannot change your mind \n")
  #use of while loop
  while flag: 
    if not user_answer.isalpha:
      user_answer = input("Please enter A, B, C, D, fifty, phone, or audience \n")
    else:
      user_answer = user_answer.upper()
      if user_answer == "FIFTY":
        if fifty_flag == 1:
          letter_one = fifty_fifty_questions[position_of_question][0]
          letter_one_upper = letter_one.upper()
          letter_two = fifty_fifty_questions[position_of_question][2]
          letter_two_upper = letter_two.upper()
          user_answer = input("Two of four possible answers have been removed. You are left with " + str(letter_one.upper()) + " and " + str(letter_two.upper()) + "\n")
          #use of nested loop
          while (user_answer != letter_one) and (user_answer != letter_two) and (user_answer != letter_one_upper) and (user_answer != letter_two_upper):
            user_answer = input(str(user_answer) + " is not one of the options. Please choose either " + str(letter_one.upper()) + " or " + str(letter_two.upper()) + "\n")
          user_answer = user_answer.upper()
          del fifty_fifty_questions[position_of_question]
          fifty_flag = 0
          flag = False
        elif fifty_flag == 0:
          user_answer = input("You have already used this lifeline. Please choose another lifeline or answer the question \n")
        else:
          errorMessage()
      elif user_answer == "PHONE":
          if phone_flag == 1:
            game_master_guess = random.choice("ABCD")
            user_answer = input("How unfortunate, it seems that you have no friends. Since I, the game master, feel bad for you, I'll tell you what I think. My gut tells me that the answer is " + str(game_master_guess) + " . You don't have to listen to me though, I won't get offended I promise \n")
            while (user_answer != "A") and (user_answer != "B") and (user_answer != "C") and (user_answer != "D") and (user_answer != "a") and (user_answer != "b") and (user_answer != "c") and (user_answer != "d"):
              user_answer = input("Please enter A, B, C, or D \n")
            user_answer = user_answer.upper()
            phone_flag = 0
            flag = False
          elif phone_flag == 0:
            user_answer = input("You have already used this lifeline. Please choose another lifeline or answer the question \n")
          else:
            errorMessage()
      elif user_answer == "AUDIENCE":
        if audience_flag == 1:
          correct_answer = list_of_answers[position_of_question][0]
          total_percentage = 100
          #use of dictionary
          audience_dictionary = {}
          if correct_answer == "A":
            percentage_a = random.randint(30, total_percentage - 10)
            audience_dictionary.update({"A": str(percentage_a) + "%"})
            total_percentage -= percentage_a
            percentage_b = random.randint(1, total_percentage - 9)
            total_percentage -= percentage_b
            audience_dictionary.update({"B": str(percentage_b) + "%"})
            percentage_c = random.randint(1, total_percentage)
            total_percentage -= percentage_c
            audience_dictionary.update({"C": str(percentage_c) + "%"})
            percentage_d = total_percentage
            audience_dictionary.update({"D": str(percentage_d) + "%"})
          elif correct_answer == "B":
            percentage_b = random.randint(30, total_percentage - 10)            
            total_percentage -= percentage_b
            percentage_c = random.randint(1, total_percentage - 9)
            total_percentage -= percentage_c
            percentage_d = random.randint(1, total_percentage)
            total_percentage -= percentage_d
            percentage_a = total_percentage
            audience_dictionary.update({"A": str(percentage_a) + "%"})
            audience_dictionary.update({"B": str(percentage_b) + "%"})
            audience_dictionary.update({"C": str(percentage_c) + "%"})
            audience_dictionary.update({"D": str(percentage_d) + "%"})
          elif correct_answer == "C":
            percentage_c = random.randint(30, total_percentage - 10)            
            total_percentage -= percentage_c
            percentage_d = random.randint(1, total_percentage - 9)
            total_percentage -= percentage_d            
            percentage_a = random.randint(1, total_percentage)
            total_percentage -= percentage_a            
            percentage_b = total_percentage
            audience_dictionary.update({"A": str(percentage_a) + "%"})
            audience_dictionary.update({"B": str(percentage_b) + "%"})
            audience_dictionary.update({"C": str(percentage_c) + "%"})
            audience_dictionary.update({"D": str(percentage_d) + "%"})
          elif correct_answer == "D":
            percentage_d = random.randint(30, total_percentage - 10)            
            total_percentage -= percentage_d
            percentage_a = random.randint(1, total_percentage - 9)
            total_percentage -= percentage_a            
            percentage_b = random.randint(1, total_percentage)
            total_percentage -= percentage_b            
            percentage_c = total_percentage            
            audience_dictionary.update({"A": str(percentage_a) + "%"})     
            audience_dictionary.update({"B": str(percentage_b) + "%"})   
            audience_dictionary.update({"C": str(percentage_c) + "%"})   
            audience_dictionary.update({"D": str(percentage_d) + "%"})
          else:
            errorMessage()
          print("The audience poll has come in !")
          print(audience_dictionary)
          user_answer = input("Can you trust the audience? hmmmm \n")
          while (user_answer != "A") and (user_answer != "B") and (user_answer != "C") and (user_answer != "D") and (user_answer != "a") and (user_answer != "b") and (user_answer != "c") and (user_answer != "d"):
            user_answer = input("Please enter A, B, C, or D \n")
          user_answer = user_answer.upper()
          audience_dictionary.clear()
          audience_flag = 0
          flag = False
        elif audience_flag == 0:
          user_answer = input("You have already used this lifeline. Please choose another lifeline or answer the question \n")
        else:
          errorMessage()
      elif (user_answer == "A") or (user_answer == "B") or (user_answer == "C") or (user_answer == "D"):
        flag = False
      elif user_answer == "QUIT":
        user_answer = input("You cannot quit during the question stage. Please enter A, B, C, or D \n")
      else:
        user_answer = input("Please enter A, B, C, or D \n")
  del list_of_questions[position_of_question]
  return position_of_question, user_answer, fifty_flag, phone_flag, audience_flag

#use of control structure, if, elif, else
def checkAnswer(user_answer, list_of_answers, position_of_question, prize):
  correct_answer = list_of_answers[position_of_question][0]
  print("The correct answer is " + str(correct_answer))
  del list_of_answers[position_of_question]
  if user_answer == correct_answer:
    print("Congratulations! You have answered correctly. You may now proceed to the next question") 
  elif user_answer != correct_answer:
    print("LOL! You answered incorrectly. Like most things in life, there are no second chances and you messed up your first")
    if (prize <= 1000) and (prize >= 100):
      print("Since you didn't even answer enough questions to make it past the first checkpoint, you leave empty handed. Have a good day :pepelaugh:")
      quit()
    elif (prize <= 32000) and (prize >= 2000):
      print("Since you made it past the first checkpoint, even though you answered incorrectly, you leave with a fat stack in your pocket. Maybe buy a new iPhone or a kidney")
      quit()
    elif (prize <= 500000) and (prize >= 64000):
      print("Impressive, you've passed the second checkpoint. Have fun spending 32 grand")
      quit()
    elif (prize == 1000000):
      print("Wow. You really answered the last question wrong. You could've been a millionaire but not you're stuck with just $32000")
      quit()
    else:
      errorMessage()

def continuePlaying(prize):
  keep_playing = input("Would you like to continue playing? Enter \"continue\" to continue or enter \"quit\" to stop playing and to leave with your earnings. If you choose to quit now, you would be $" + str(prize) + " richer \n")
  while (keep_playing != "continue") and (keep_playing != "quit"):
    keep_playing = input("Please type \"continue\" to keep playing or \"quit\" to leave with your winnings \n")
  if keep_playing == "quit":
    print("You have won $" + str(prize) + ". Have a good day")
    quit()

def errorMessage():
  print("ERROR. This program will self destruct in \n 3 \n 2 \n 1")
  quit()



#PROGRAM

#use of list
questions_easy = ["Amateur investors banded together in January to squeeze Wall Street hedgefunds, sending one stock's value up by more than $10 billion. Which stock was this? \n A: Bitcoin \n B: Amazon \n C: Tesla \n D: Gamestop", "Which member of the Royal Family past away in April of 2021 at the age of 99? \n A: Prince Phillip \n B: Queen Elizabeth \n C: Prince Charles \n D: Winston Churchill", "Mark Zuckerberg announced that Facebook will be changing its corporate name amid public scrutiny over leaked internal documents. What is being changed to? \n A: Raise \n B: Meta \n C: Metaverse \n D: Facebook (no change)", "YouTube, in November, rolled out a controversial change to its site that still continues to anger users and creators on the platform. What did they do? \n A: Made YouTube Rewind 2021 \n B: Tightened Copyright regulations and fair use \n C: Removed the dislike button \n D: Banned sponsored content", "A record was broken during an online auction held by Christie's in March of 2021 for the sale of a particular piece of digital artwork, closing at $69 (nice) million. What was it? \n A: Bored Ape Yacht Club NFT \n B: Nyan Cat NFT \n C: Jack Dorsey first ever tweet NFT \n D: Everydays - The First 5000 Days by Beeple (NFT Collage)", "This former world leader made the news in January for having all their social media accounts suspended, a decision that has been upheld for the entirety of 2021. Who was it? \n A: Donald Trump \n B: Stephen Harper \n C: Xi Jinping \n D: Barack Obama", "In a rare interview with the New York Times Magazine, one critically acclaimed filmmaker confirmed he would be coming out of retirement yet again. Who was it? \n A: Francis Ford Coppola \n B: Martin Scorsese \n C: Hayao Miyazaki \n D: Wilson Yip", "Critically acclaimed manga author Miura Kentaro passed away in May of 2021 at age 54 from an acute aortic dissection. What series was he most known for? \n A: Berserk \n B: Vagabond \n C: Death Note \n D: Hunter x Hunter", "A piece of artwork, famous for half-shredding itself in its frame upon the closure of the bidding, was sold in October of 2021 for $25 million at auction in its damaged state. Who was the creator of this self-mutilating work? \n A: Jackson Pollock \n B: Banksy \n C: Takashi Murakami \n D: Anselm Kiefer", "Amazon came under fire last year over the working conditions at its warehouses. What did employees report they had to do while working? \n A: Dress up as elves and sing \n B: Work 12 hour shifts without breaks \n C: Urinate in bottles \n D: Union busting", "The Black Vault, a site dedicated to \"exposing government secrets\" released in January a collection of declassified documents it purchased from the CIA. What did they contain? \n A: Snowden's whereabouts \n B: Internationnal savings accounts of world leaders \n C: UFOs \n D: Aliens", "What Korean drama premiered on Netflix in September of 2021, eventually becoming the most viewed Netflix show in history? \n A: Squid Game \n B: Alice in Borderland \n C: Sweet Home \n D: Hotel Del Luna", "This billionaire made a record $25 billion in one day in October of 2021 pushing his estimated net worth to $255 billion, likely making him the richest person ever, according to Forbes. Who was this person? \n A: Jeff Bezos \n B: Sundar Pichai \n C: Mark Zukerberg \n D: Larry Ellison", "Who won the 2021 Eurocup? \n A: England (not a city) \n B: Italy \n C: Spain \n D: Denmark", "In which of the following canals did the container ship, Ever Given, run aground? \n A: Corinth Canal \n B: Suez Canal \n C: Panama Canal \n D: Beijing-Hanzhou Canal"]

easy_answers = ["D: Gamestop", "A: Prince Phillip", "B: Meta", "C: Removed the dislike button", "D: NFT Collage by Beeple", "A: Donald Trump", "C: Hayao Miyazaki", "A: Berserk", "B: Banksy", "C: Urinate in bottles", "C: UFOS", "A: Squid Game", "A: Lord Bezos", "B: Italy", "B: The Suez Canal"]

fifty_fifty_easy = ["a/d", "a/c", "b/c", "c/d", "c/d", "a/c", "a/c", "a/b", "b/d", "c/d", "a/c", "a/c", "a/b", "a/b", "b/c"]

questions_medium = ["In October of 2021, the ICIJ published an 11.9 million leaked documents exposing the secret offshore bankaccounts of world leaders, billionares, celebreties and business leaders. What were these documents called? \n A: The X-Files \n B: Jeff Bezos \n C: The Panama Papers \n D: The Pandora Papers", "A Los Angeles county judge ruling has granted popstar Britney Spears a decisive victory, putting an end to a 13 year long legal arrangement. What was this case about? \n A: Conservatorship \n B: Divorce and ownership of child \n C: Past crime reaching statute of limiations \n D: Ownership of her families cottage in Minnesota", "The following is a quote from a press junket interview for a movie released this year. Which movie was being promoted \n \"I would rush through scenes just to get to that moment where you would get kissed\" \n A: Dune \n B: 007 No Time to Die \n C: The Matrix Ressurections \n D: Free Guy", "In March of 2021, it was annouced that 6 books from a popular childrens' author would no longer be published due to use of racist and insensitive imagery. Who is this author? \n A: J.K. Rowling \n B: Roald Dahl \n C: Dr. Suess \n D: E.B. White", "A single issue of this comic book broke records, selling for $3.25 million at auction in April of 2021. What was this comic? \n A: Superman \n B: Spiderman \n C: Spiderman \n D: One Piece", "2021 saw the continuation of the billionaires space race, with a number of billionaires themselves flying into space in July of 2021. Which one of the following was one of these billionaires? \n A: Elon Musk \n B: Jack Ma \n C: Richard Branson \n D: Bill Gates", "What major international event was finally held in July of 2021, to much concern and controversy following a series of resignitions of its top officials, after a one year delay due to the pandemic? \n A: The League of Legends World Championship \n B: The 2020 Summer Olympics Tokyo Japan \n C: CES \n D: E3", "On June 4th, Prince Harry and wife Meghan Markle announced the birth of their daughter whose name pays tribute to Queen Elizabeth II. What is her name? \n A: Queenie \n B: Lilibet \n C: Elizabeth \n D: Alexandra", "Which female tennis player was the surprise winner of the US Open in 2021? \n A: Naomi Osaka \n B: Leylah Fernandez \n C: Ashleigh Barty \n D: Emma Raducanu", "Which of these is the name of a hurricane which struck at the end of August 2021? \n A: Hurrican Ira \n B: Hurricane Ida \n C: Hurricane Irma \n D: Hurricane Isla", "What was the name of the 2021 United Nations Climate Change Conference which took place in Scotland? \n A: COP26 \n B: MOP21 \n C: CAP96 \n D: BOP28"]

medium_answers = ["D: The Pandora Papers", "A: Convservatorship (her dad had ownership of all her stuff)", "B: 007 No Time to Die", "C: Dr. Suess", "A: Superman", "C: Richard Branson", "B: The Tokyo Olympics", "B: Lilibet", "D: Emma Raducanu", "B: Hurrican Ida",  "A: COP26"]

fifty_fifty_medium = ["b/d", "a/b", "b/c", "b/c", "a/b", "a/c", "b/d", "b/c", "a/d", "b/c", "a/d"]

questions_hard = ["The Italain Performers in this year's Eurovision Song Contest were embroiled in controversy after one of its members was accused of being caught doing something on camera. What were they accused of doing? \n A: Picking his nose \n B: Intercourse \n C: A line of cocaine \n D: Physically assaulting another band member", "In June, American Abhimanyu Mishra became the youngest ever to be granted a particular title at 12 years, 4 months and 25 days old. What was his title? \n A: Olympic Gold Medalist \n B: Chess Grandmaster \n C: Chess World Champion \n D: Violin Concerto Soloist", "During the 2021 Summer Olympics held in Tokyo Japan, what item was withheld from the olympiads that is normally given out every year? \n A: Water \n B: Medals \n C: Condoms \n D: Marijuana", "Four lawsuits filed against a game development studio in December 2020 over a game's release have been consolidated a year later into a class action and now will be subject to potential common court proceedings. Which game has been the subject of these lawsuits? \n A: Red Dead Redemption 2 \n B: Resident Evil Village \n C: Cyberpunk 2077 \n D: Valorant", "How many views made Squid Game the most viewed show on Netflix? \n A: 200 million \n B: 330 million \n C: 159 million \n D: 118 million", "The following are audience reviews on MAL for an anime movie released this year. What movie are they talking about? \n \"cinematically, the film.... could almost be called disastrous\" \n \"over 8 years of waiting for this, what a disappointment\" \n \"lives up to its predecessor by being another obnoxius cluster****\" \n A: Evangelion 3.0 + 1.0 \n B: Cowboy Bebop: The Movie \n C: Princess Mononoke \n D: Made in Abyss Movie 3: Fukaki Tamashii no Reimei", "At the time of their release in September, Canadians Michael Kovrig and Michael Spavor spent more than 1,000 days in a Chinese prison cell. What were they accused of? \n A: Lobbying against Huawei for the Canadian government \n B: Spying and providing state secrets to entities outside of China \n C: Protesting the treatment of the Uyghur ethnic minority by the Chinese government \n D: Playing more than the Chinese government's mandated limit of three hours of video games per week", "On 10 January 2021, North Korean Supreme Leader Kim Jong-un was elected general secretary of the Workers Party of Korea. Who did he replace? \n A: His late father, Kim Jong-il, who died in 2011, but held the office for a decade posthumously \n B: His late grandfather Kim Il-Sung, who died in 1994, but held the office for 27 years posthumously \n C: His uncle Jang Song-thaek, who was executed for treason in 2014 \n D: His sister Kim Yo-jong, who became a social media sex symbol in 2020", "Adele’s long-awaited album, 30, was the bestselling LP of 2021. But just how bestselling was it in its first week of release? \n A: It outsold the rest of the Billboard Top 10 combined \n B: It outsold the rest of the Billboard Top 20 combined \n C: It outsold the rest of the Billboard Top 40 combined \n D: It outsold the rest of the Billboard Top 50 combined", "Having been postponed by the pandemic, Euro 2020 finally got under way in June and was the highest-scoring in the tournament’s history. Despite this, goals by which method outstripped Ronaldo’s top-scoring tally of six goals? \n A: Penalties \n B: Own goals \n C: Goals disallowed by video-assisted refereeing \n D: Each of the above", "Notorious restaurateur Nusret Gökçe, better known by the meme-begotten soubriquet Salt Bae, opened a restaurant in Knightsbridge this year, attracting attention for its eye-wateringly high prices. Other than wine, what is understood to be the most expensive single item on its menu? \n A: A truffle-infused hotdog, priced at £800 \n B: A goldleaf-laden giant tomahawk steak, at £1,450 \n C: A “billionaire burger” served with diamond shavings for £2,450 \n D: One can of Red Bull energy drink, costing £4,765", "The Omicron variant is the latest sortie in Covid’s ongoing war to forcibly teach us the Greek alphabet. Which of the following is not to be found within that ancient alphabetic script’s 24 letters? \n A: Pi \n B: Phi \n C: Psi \n D: Si"]

hard_answers = ["C: He was doing a line of cocaine on live television", "B: Youngest chess grandmaster in history", "C: Condoms", "C: Cyberpunk 2077", "D: 118 million views on Netflix", "A: Evangelion 3.0 + 1.0 (4.0)", "B: Spying and providing state secrets to entities outside of China", "A: Kim Jong-un replaced Kim Jong-il", "D: 30 outsold the entirety of the Billboard Top 50 combined", "D: Each of the above: 9 penalties, 11 own goals, and 7 disallowed by VAR", "B: The goldleaf tomahawk steak", "D: Si is not a Greek letter"]

fifty_fifty_hard = ["c/d", "b/d", "b/c", "a/c", "c/d", "a/c", "b/d", "a/d", "b/d", "c/d", "b/d", "a/d"]

fifty_flag = 1

audience_flag = 1

phone_flag = 1

flag = True

user_answer = "kekw"

position_of_question = 0

money_list = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]

name = input("Hello player! Welcome to who wants to be a millionaire, hosted by the one and only OLIVER. What is your name? \n")

print("Hello " + str(name) + ". Now to explain the rules: \n You will be asked a series of 15 questions, progressively increasing in difficulty. The more questions you answer correctly, the more money you make. If you answer all 15 questions correctly, you win a million dollars, hence the name who wants to be a millionaire. Each question will have 4 multiple choice answers. \n You have 3 lifelines at your disposal if you get stuck: 50:50, phone-a-friend, and ask the audience. \n 50:50 removes half of the available answers, leaving one correct and one incorrect option. \n Phone-a-friend allows you to call a friend who may know the answer. \n Ask the audience takes the vote of the audience members, who vote for the answer that they think is correct (or not). \n After every correct guess, you have the option to leave with your winnings. On the other hand, if you choose to proceed and guess incorrectly, you loose all of your winnings. There are 2 thresholds, $1000 and $32000. If you guess incorrectly after passing these thresholds, you get to leave with the amount of the threshold in your pocket.")

#use of input and output functions
confirm_play = input("Are you ready to play? \n")
#tests for invalid inputs
while (confirm_play != "yes") and (confirm_play != "y") and (confirm_play != "YES") and (confirm_play != "Yes"):
  if (confirm_play == "no") or (confirm_play == "n") or (confirm_play == "NO") or (confirm_play == "No"):
    confirm_play = input("I can wait \n")
  else:
    confirm_play = input("Please enter yes or no \n")

print("Today's subject will be regarding 2021 topics, hopefully you've been reading the news")

#use of for loop
for counter in range (1, 16):
  prize = money_list[counter - 1]
  print("Prize = $" + str(prize))
  print("Question Number " + str(counter) + ":")
  if (counter >= 1) and (counter <= 5):
    placeholder_variable = generateQuestion(questions_easy, position_of_question, easy_answers, fifty_flag, audience_flag, phone_flag, fifty_fifty_easy, flag)
    #use of assignment of variables
    position_of_question = placeholder_variable[0]
    user_answer = placeholder_variable[1]
    fifty_flag = placeholder_variable[2]
    phone_flag = placeholder_variable[3]
    audience_flag = placeholder_variable[4]
    checkAnswer(user_answer, easy_answers, position_of_question, prize)
    continuePlaying(prize)
  elif (counter >= 6) and (counter <= 10):
    placeholder_variable = generateQuestion(questions_medium, position_of_question, medium_answers, fifty_flag, audience_flag, phone_flag, fifty_fifty_medium, flag)
    position_of_question = placeholder_variable[0]
    user_answer = placeholder_variable[1]
    fifty_flag = placeholder_variable[2]
    phone_flag = placeholder_variable[3]
    audience_flag = placeholder_variable[4]
    checkAnswer(user_answer, medium_answers, position_of_question, prize)
    continuePlaying(prize)
  elif (counter >= 11) and (counter <= 15):
    placeholder_variable = generateQuestion(questions_hard, position_of_question, hard_answers, fifty_flag, audience_flag, phone_flag, fifty_fifty_hard, flag)
    position_of_question = placeholder_variable[0]
    user_answer = placeholder_variable[1]
    fifty_flag = placeholder_variable[2]
    phone_flag = placeholder_variable[3]
    audience_flag = placeholder_variable[4]
    checkAnswer(user_answer, hard_answers, position_of_question, prize)
    continuePlaying(prize)
  else:
    errorMessage()
print("CONGRATULATIONS!!! CONSIDER YOURSELF THE FIRST AND ONLY WINNER OF WHO WANTS TO BY A MILLIONAIRE HOSTED BY OLIVER")


