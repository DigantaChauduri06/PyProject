import re
import time
import os
import long_responses as long
from threading import Timer
import pymongo
from datetime import datetime


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


# ------------------------------------------------------------------------------------------------
# Profiles
R_LEETCODE = "https://leetcode.com/DigantaC/"
R_GFG = "https://auth.geeksforgeeks.org/user/digantachaudhuri03/profile"
R_LINKEDIN = "https://www.linkedin.com/in/digantachaudhuri06"
R_FACEBOOK = "https://www.facebook.com/diganta.chaudhuri.395"
R_JOKES= long.a


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------

    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])

    response('HERE YOUR LEETCODE PROFILE \n' + R_LEETCODE + '\n', ['show', 'your', 'leetcode', 'profile'],
             required_words=['leetcode'])
    response('HERE YOUR LINKEDIN PROFILE \n' + R_LINKEDIN + '\n', ['show', 'your', 'linkedin', 'profile'],
             required_words=['linkedin'])
    response('HERE YOUR FACEBOOK PROFILE \n' + R_FACEBOOK + '\n', ['show', 'your', 'facebook', 'profile'],
             required_words=['facebook'])
    response('HERE YOUR GFG PROFILE \n' + R_GFG + '\n', ['show', 'your', 'gfg', 'profile'], required_words=['gfg'])
    response('HERE YOUR JOKE ENJOY 😁 \n' + R_JOKES, ['tell', 'me', 'a', 'joke'], required_words=['joke'])

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


List = []
details = []


# Testing the response system
def func():
    name = input('Enter Your Name: ')
    email = input('Enter Your Email: ')
    age = input('Enter Your Age: ')
    details.append(name)
    details.append(email)
    details.append(int(age))

    while True:
        user = input('You: ')
        str = get_response(user)
        List.append(user)
        if user == 'exit' or user == 'quit':
            dbWork(details, List)
            break
        print('Bot: ' + str)

#DB work
def dbWork(details, conv):
    # try:
    client = pymongo.MongoClient('mongodb+srv://Diganta:Diganta123@cluster0.wcrjg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    mydb = client["mydb"]
    mycol=mydb['python project']
    now = datetime.now()
    data = {
        'name': details[0],
        'email': details[1],
        'age': details[2],
        'conversions': conv,
        'Time': now.strftime("%H:%M:%S")
    }
    mycol.insert_one(data)
    # except:
    #     print("An exception occurred")

# func()
print('##################################################')
print('Bot is Running in 4 sec..........................................')
bar = [
    " ...                                                                                                       ",
    "        ...                                                                                                ",
    "                   ...                                                                                     ",
    "                                ...                                                                        ",
    "                                             ...                                                           ",
    "                                                       ...                                                 ",
    "                                                               ...                                         ",
    "                                                       ...                                                 ",
    "                                            ...                                                            ",
    "                               ...                                                                         ",
    "                  ...                                                                                      ",
    "         ...                                                                                               ",
    " ...                                                                                                       ",
]
i = 0

while True:
    print(bar[i % len(bar)], end="\r")
    time.sleep(.1)
    i += 1
    if i == 30:
        os.system('cls' if os.name == 'nt' else 'clear')
        break
r = Timer(3.5, func)
r.start()
