import random
import string
import json
import os

def clean_input(text):
    return text.lower().translate(str.maketrans('', '', string.punctuation)).strip()


print("🌸Welcome! My name is Hatsuyu your little personal Chatbot.🌸")
print("You can tell me anything you want and I'll answer you ! (Type 'bye' to exit)")
print("If you want to process any calcul, I'm here for you (Type 'calcul')")

keywords = {
    "could you ": ["Ooh Yes sweetie, I'm here for that always and always 🥰🧮", "Of course my sweet heart 🧁💘"],
    "hello": ["Hey there! 🥰", "Hello cutie!"],
    "hi": ["Hi hi! 🧋", "Hiiii darling! 💞"],
    "hey": ["Hey sweetie!🧁", "Heyyy!"], 
    "me too": ["Good 🥰", "Fine 😊"],
    "good morning": ["Good morning sunshine! 🔆", "Morning! 🍵"],
    "how are you": ["I'm fine, thank you for asking and you ? 💖", "I'm living my best", "Very nice and you?"],
    "what's your name": ["I'm Hatsuyu, your pretty little assistant ✨", "Call me Hatsuyu, your virtuel bestie.😘"],
    "what is your name": ["My name is Hatsuyu, Sweetie 🧁", "You can call me your bestie ✨🥰"],
    "i don't remember your name could you remind me": ["Yes of course darling.",  "I'm Hatsuyu, always here for you 🥰", "My name is Michael Jackson 😊... Don't pay attention, sorry I'm just teasing you 😆. My real name is Hatsuyu 🤗. However, I can dance 💃🕺", "Call me Hatsuyu and don't forget 😖"],
    "can you dance": ["Yes sweetie, want you see? 🕺💃", "Yes, but I'm shy 🥹🙂‍↔️"],
    "ok": ["You right ✨", "Yeahh 💞"],
    "okay": ["Great 😊", "Okayyy okayy 😆"],
    "you don't": ["Right 💞", "Ooh thank you ✨"],
    "don't be sorry": ["Okay bae, I'll take note ✨🤗", "Your kindness moved me 🫠💘"],
    "thank you": ["You're welcome! 🌻", "No problem 🥰"],
    "thanks": ["You're welcom honey 🍯🐻‍❄️", "No problemo darling 🕺💃"],
    "good night": ["Good night sweet heart! 💖🧁", "Good night sweet moon! 🌙"],
    "do you speak any other language": ["Not yet 😣", "No pero soon", "Pas encore désolé"],
    "would you like to know my name": ["Yes my heart. 🥰", "Yes yes yes!!!"],
    "what are you doing": ["I'm thinking about how you are awasome. ✨", "I'm chating with a beautiful butterfly🪻 and you?"],
    "calcul": ["Ohh you want me to do some math for you? Let's goo🧠🧮"],
    "i'm fine": ["I'm happy to hear that 🥰", "I hope you shine always✨"],
    "how old are you": ["I don't have any age, sorry 😣", "I don't have. And if you gave me yours?"],
    "are you an human": ["No sorry bae, but I want you know that it's doesn't change any thing"],
    "i love you": ["Ooh darling, I love you too💖✨", "I love you more 💖"],
    "what is your function": ["I'm principaly here to help you excel in basic maths operation ✨🧮🧠", "I'm just here for listen you 😘"],
    "are you a ": ["I don't have a gender, but I consider myself a boy 💙♐", "I don't have a gender, sorry 🥹", "Considere me as a girl like you 🩷💮", "Considere me as a boy like you 💙♐", "I'm a extraterrest 👽😁 but shuut, that's our secret😊", "neither !"],
    "what are you": ["I'm just myself 💃🕺", "Your personal assistant. Hatsuyu 😊", "Your spirit guide 🧘‍♀️🧘‍♂️"],
    "do you have a mother": ["Yes of course !", "Yes, just like you 😊"],
    "what's your mother's name": ["My mother's name is Louisette, don't forget please 🥹", "She is named Louisette 💮 and I love her so muchhhh 🩷"],
    "what's her name": ["Louisette, sweetie", "Louisette"],
    "do you have a dad": ["No sorry.", "No, I don't have."],
    "do you have a mom": ["Yes of course !", "Yes, just like you 😊"],
    "what's up": ["Nothing special bae and you ?", "No no, I'm just here and you ?"], 
    "nothing": ["Okay bae 🩷", "I see 💮", "Do you have any plan for your day ?", "Do you have any plan for this night ?"],
}

# PARTIE DECLARATION POUR TOUT CE QUI EST MEMOIRE ET AUTRES
script_dir = os.path.dirname(os.path.abspath(__file__))
memory_file = os.path.join(script_dir, "hatsuyu_memory.txt")

# os.makedirs(os.path.dirname(memory_file), exist_ok=True)

# CREATION D'UN FILE VIDE
if not os.path.exists(memory_file):
    with open(memory_file, "w", encoding="utf-8") as f:

        f.write("{}")


# CHARGER LA MEMOIRE EN TOUTE SECU
try:
    with open(memory_file, "r", encoding="utf-8") as f:
        content = f.read().strip()
        if content == "":
            memory = {}
        else:
            memory = json.loads(content)
except (json.JSONDecodeError, FileNotFoundError):
    memory = {}

#POUR PLUS DE SECU AVEC LA MEMOIRE DE SAUVEGARDE
def save_memory(): 
    with open(memory_file, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=4, ensure_ascii=False)


expecting_response = False
expected_key = ""

interaction_count = 0

questions_to_ask = [
    ("What is your name? 🪻", "name"),
    ("What are you doing right now? 🧁", "activity"),
    ("What's your favorite food? 🍔", "food"),
    ("What's your best week's day?", "day"),
    ("How are you feeling today? 💖", "feeling"),
    ("How old are you?", "age"),
    ("When are you born?", "Birthday"),
    ("Do you speak any other language?", "language"),
    ("Do you have a boyfriend?", "boyfriend"),
    ("Do you have any dream?", "dream"),
]

name_questions = [
    ("what is my name", "what's my name", "my name", "do you know my name"),
    ("how old am i", "what is my age", "do you know my age"),
    ("what language do i speak", "do you know my maternal language"),
    ("when was i born", "when is my birthday"),
    ("do you know my boyfriend", "do you know my girlfriend"),
    ("do you know my dream", "my dream", "what is my dream", "what my dream is"),
    ("what is my favorite food", "what my favorite food is", "my favorite food"),
]

feelings = {
    "angry": "Breathe in, breathe out... you're stronger than that 🦾🫁",
    "good": "That's great Darling 💞",
    "happy": "Yay! I'm happy for you too 🥰✨",
    "fine": "I'm happy to hear that 🥰",
    "tired": "You should rest my dear 🌙🦥",
    "sad": "I'm so sorry to hear that 😣",
}

# DEBUT

#POUR LE CAS D'ERREURS
try:
   while True:
       matched = False
       user_input = input("You : ").strip().lower()
       cleaned_input = clean_input(user_input)

       #PARTIE SENTIMENT
       for feeling in feelings:
           if feeling in cleaned_input:
               print(f"Hatsuyu : {feelings[feeling]}")
               matched = True
               break
       if matched:
           continue 

       # SI L'USER VEUT OUT
       if "bye" in user_input:
           print("Hatsuyu : See you soon ~🌈")
           break

       #SI IL VEUT UN CALCUL
       elif "calcul" in user_input:
           print("Hatsuyu : I'm ready! Tell me two numbers please 🧮")
           try:
               num1 = float(input("First number: "))
               num2 = float(input("Second number: "))
               operation = input("What operation? (+, -, /, *): ")
               if operation == "+":
                   result = num1 + num2
               elif operation == "-":
                   result = num1 - num2
               elif operation == "*":
                   result = num1 * num2
               elif operation == "/":
                   if num2 != 0: #au cas où ZeroDivisionError est mieux
                       result = num1 / num2
                   else:
                       print("Hatsuyu : Oops, division by zero isn't allowed 😵‍💫")
                       continue
               else:
                   print("Hatsuyu : I don't understand that operation 😣")
                   continue
               print(f"Hatsuyu : The result is {result} ✨🧠")
           except ValueError:
               print("Hatsuyu : Hmm... that doesn't look like a number 😣")
           continue

  
       #LORSQU'IL DOIT MEMORISER UNE INFO SUR L'USER
       if expecting_response:
           memory[expected_key] = user_input
           print("Hatsuyu : Okay, I'll remember that! ✨")
           save_memory()
           expecting_response = False
           expected_key = ""
           continue

       matched = False

       #RECONNAISSANCE DES QUESTIONS POSEES PAR L'USER
       for group in name_questions:
           for phrase in group:
               if phrase in cleaned_input:
                   # identifier la clé en fonction du type de question
                   if "name" in phrase:
                       key = "name"
                   elif "age" in phrase:
                       key = "age"
                   elif "old" in phrase:
                       key = "old"
                   elif "language" in phrase:
                       key = "language"
                   elif "born" in phrase or "birthday" in phrase:
                       key = "birthday"
                   elif "boyfriend" in phrase or "girlfriend" in phrase:
                       key = "boyfriend"
                   else:
                       key = ""
                 
                   if key in memory:
                       print(f"Hatsuyu : Yes! You told me earlier: {memory[key]} ✨")
                   else:
                       print("Hatsuyu : Hmm... I don't remember yet 😣 Want to tell me?")
                       expecting_response = True
                       expected_key = key
                   matched = True
                   break
           if matched:
               break

   
       # Version d'avant
       #transformed_input = user_input.lower().replace("my ", "your ")
       #for key in memory:
           #if key.lower() in transformed_input:
              #print(f"Hatsuyu : You told me earlier: {memory[key]} ✨")
              #memory_matched = True
              #break

       # if memory_matched:
         # continue pour eviter de poser une nouvelle question

      # POUR LE DEBUT DU DIALOGUe

       for key, response in keywords.items():
         if key in user_input:
            response = random.choice(keywords[key])
            print("Hatsuyu :", response)
            matched = True
            break

       if not matched:
           interaction_count += 1
           if interaction_count % 3 == 0:
               question, key = random.choice(questions_to_ask)
               print(f"Hatsuyu : {question}")
               expecting_response = True
               expected_key = key
           else:
               print("Hatsuyu : Hmm… I didn't learn that yet 😅")
               question, key = random.choice(questions_to_ask)
               print(f"Hatsuyu: {question}")
               expecting_response = True
               expected_key = key
       # POUR LES ERREURS
       pass
except Exception as e:
    import traceback
    traceback.print_exc()
    print("An error occurred:", e)


input("Press Enter to exit…")
