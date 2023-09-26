import pyttsx3
import speech_recognition as sr
import random,re
from find import find
import threading ,subprocess ,os
from play_yt import play
import webbrowser 
from search import Search
class library:
	def __init__(self):
		self.greetings=["Hy",
				"Hello",
				"Hi there",
				"Howdy",
				"Greetings",
				"Hey, What’s up?",
				"What’s going on?",
				"Hey! There",
				"How’s everything?",
    			"How are things?",
				"Good to see you",
				"Great to see you",
				"Nice to see you"
				]
		self.leaving=[	"Goodbye",
				"Bye bye",
				"Bye",
				"See you later",
				"See you",
				"Quit"]
		self.questions=["what", 	
				"when", 	
				"where", 	
				"which", 	
				"who", 	
				"whom", 	
				"whose", 
				"why",	
				"why don't", 	
				"how"]
		
class Friday():
	def __init__(self):
		self.e=pyttsx3.init()
		voices=self.e.getProperty('voices')
		newVoiceRate = 165
		self.lib=library()
		self.e.setProperty('rate',newVoiceRate)		
		self.e.setProperty('voice',voices[1].id)
		self.name="Friday"
		self.owner=""
		#threading.Thread(target=find,daemon=True).start()
	def speak(self,s):
		self.e.say(s)
		self.e.runAndWait()

	def parse(self,sentence,wordList:list)->bool:
		for i in wordList:
			if(i.lower() in sentence):
				return True
		return False
	def listen(self):
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print("Listening...")
			r.pause_threshold = 0.8
			audio = r.listen(source)

		try:
			print("Recognising...")
			query = r.recognize_google(audio, language='en-in')
			query = str(query).lower()
		except Exception:
			return "Say That Again Please..."

		return query
	def run(self):
                self.speak("HEllO WORLD")
                while True:
                        cmd=self.listen()
                        print("User: "+cmd)
                        rep=None
                        if(cmd.capitalize() in library().greetings):
                                        rep=random.choice(library().greetings)
                                        self.speak(rep)
                        elif(cmd.capitalize() in library().leaving):
                                        rep=random.choice(library().leaving)
                                        self.speak(rep)
                                        exit(0)
			elif("what is your name" in cmd.lower())
				rep=f"my name is {self.name}" 
				self.speak(rep)
                        elif("play" in cmd and "song" in cmd):
                                cmd=cmd.replace("from youtube","")
                                self.speak("Playing "+cmd.replace("play","")+"from youtube")
                                play(cmd)				
                        elif(self.parse(cmd,self.lib.questions)):
                                print("Searching...")
                                self.speak("Searching...")
                                result=Search().search(cmd)
                                print(result)
                                self.speak(result)
                        if not rep is None:
                                print("Friday: "+rep)
if __name__=="__main__":
	Friday().run()
