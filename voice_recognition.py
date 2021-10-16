import speech_recognition as sr
from colorama import init, Fore, Back, Style

# STYLE
beg = Fore.GREEN + "[" + Fore.YELLOW + "+" + Fore.GREEN + "] " + Style.RESET_ALL

recognizer = sr.Recognizer()

class voiceRecognizer:
    __recorder_audio = None
    __text = ""
    @staticmethod
    def recorder():
        with sr.Microphone() as source:
            print(beg + "Adjusting noise ")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print(beg + "Start recording")
            voiceRecognizer.__recorder_audio = recognizer.listen(source, timeout=10)
            print(beg + "Done recording")
            voiceRecognizer.decoder()

    @staticmethod
    def decoder():
        try:
            print(beg + "Recognizing the text")
            voiceRecognizer.__text = voiceRecognizer.__text + ". " + recognizer.recognize_google(
                voiceRecognizer.__recorder_audio, 
                language="fr-FR"
            )
            
            if voiceRecognizer.__text.split(' ')[-1] != "terminé" and voiceRecognizer.__text.split(' ')[-1] != "terminer": 
                voiceRecognizer.recorder()
            else:
                print(beg + "Decoded Text : {}".format(voiceRecognizer.__text))
        except Exception as ex:
            print(ex)


voiceRecognizer.recorder()
