import random

GREETING_INPUTS = ("bonjour", "salut", "yo", "salutations", "sup","hey",)
GREETING_RESPONSES = ["Bonjour", "Yo", "Salut!", "Salutations", "hey"]

def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

NAME_INPUTS:("Marina","Nory","Adrien","Hugo")
PHONE_INPUTS =("tel", "numero", "num","telephone")
PHONE_RESPONSES=["le numéro de téléphone de Marina est: ","pour joindre Marina c'est"]

def phone(sentence):
    for word in sentence.split():
        if word.lower() in PHONE_INPUTS:
            return random.choice(PHONE_RESPONSES)




flag=True
print("BobOt: Je m'appel BoBot. Demandes-moi ce que tu veux sur la promo Data IA. Si tu veux partir, écris Bye!")


while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("BobOt: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("BobOt: "+greeting(user_response))
            elif(phone(user_response)!=None):
                print("BobOt: "+phone(user_response))
            else:
                print("BobOt: ",end="")
    else:
        flag=False
        print("BobOt: Bye!")
