import random
import requests
import json

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"



def unknown():
    response = ["Its better if you can search this thing on google ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response


def jokes(f):
    try:
        data = requests.get(f)
        tt = json.loads(data.text)
        if 'joke' in tt.keys():
            return tt['joke']
        return tt['setup'] + ' ' + tt['delivery']
    except:
        return 'Error Happen while retreving joke'

f = r"https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Dark,Pun,Spooky,Christmas"
a = jokes(f)
