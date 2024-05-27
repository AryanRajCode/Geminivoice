import os
import platform
import SimpleVoiceAssistant as p2
ai = p2.Parsoon(ai_engine="gemini",lang="en")
# enter api of Gemini if dont have get it for free from https://aistudio.google.com/app/apikey
api_gemini = "api here"

keywords = {
        "who are you": "i am gemini"
    }
# you can enter the keywords if you want 
if api_gemini != "" or '' or "api here":
    with open("gemni_","w") as f :
        f.write(api_gemini)
os.system("clear")

# Check API exists in txt or not

try:
    with open("gemni_api.txt", 'r') as file:
        rr = file.read()
        if rr.strip() == "":
            api_gemini = input("Enter the Gemini API (get it for free from https://aistudio.google.com/app/apikey):\nEnter: ")
            with open("gemni_api.txt", 'w') as file:
                file.write(api_gemini)
        else:
            api_gemini = rr

except FileNotFoundError:
    api_gemini = input("Enter the Gemini API (get it for free from https://aistudio.google.com/app/apikey):\nEnter: ")
    with open("gemni_api.txt", 'w') as file:
        file.write(api_gemini)




ai = p2.Parsoon(ai_engine="gemini")


def speak(t):
    try:  
        ai.speak(t)
    except Exception as e:
        print("Error speaking:", e)
        pass

with open("gemni_api.txt", 'r') as file:
    gg = file.read()

while True:
    try:
        command = ai.listen()
    except Exception as e:
        print("Error listening:", e)
        continue
    response = keywords.get(command)
    if response is None or "" or '':
        try:
            response = ai.ai_response(query=f"{command}", token=gg)            
            print("AI Response:", response)
            speak(response)
        except Exception as e:
            print("Error processing AI response:", e)
    else:
        print("AI Response:", response)
        speak(response)
