from tkinter import *
from tkinter import ttk
import pyaudio
from multiprocessing import Queue
from threading import Thread
import subprocess
#import time
from googletrans import Translator 
import speech_recognition as sr 
#import os
import threading
#import sys
from tkinter import filedialog



silence= False
#btnstoptxt="Pause"
fromLanguage="ar"
toLanguage="en"


fromLangList=['afrikaans', 'af', 'albanian', 'sq', 
	'amharic', 'am', 'arabic', 'ar', 
	'armenian', 'hy', 'azerbaijani', 'az', 
	'basque', 'eu', 'belarusian', 'be', 
	'bengali', 'bn', 'bosnian', 'bs', 'bulgarian', 
	'bg', 'catalan', 'ca', 'cebuano', 
	'ceb', 'chichewa', 'ny', 'chinese (simplified)', 
	'zh-cn', 'chinese (traditional)', 
	'zh-tw', 'corsican', 'co', 'croatian', 'hr', 
	'czech', 'cs', 'danish', 'da', 'dutch', 
	'nl', 'english', 'en', 'esperanto', 'eo', 
	'estonian', 'et', 'filipino', 'tl', 'finnish', 
	'fi', 'french', 'fr', 'frisian', 'fy', 'galician', 
	'gl', 'georgian', 'ka', 'german', 
	'de', 'greek', 'el', 'gujarati', 'gu', 
	'haitian creole', 'ht', 'hausa', 'ha', 
	'hawaiian', 'haw', 'hebrew', 'he', 'hindi', 
	'hi', 'hmong', 'hmn', 'hungarian', 
	'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian', 
	'id', 'irish', 'ga', 'italian', 
	'it', 'japanese', 'ja', 'javanese', 'jw', 
	'kannada', 'kn', 'kazakh', 'kk', 'khmer', 
	'km', 'korean', 'ko', 'kurdish (kurmanji)', 
	'ku', 'kyrgyz', 'ky', 'lao', 'lo', 
	'latin', 'la', 'latvian', 'lv', 'lithuanian', 
	'lt', 'luxembourgish', 'lb', 
	'macedonian', 'mk', 'malagasy', 'mg', 'malay', 
	'ms', 'malayalam', 'ml', 'maltese', 
	'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian', 
	'mn', 'myanmar (burmese)', 'my', 
	'nepali', 'ne', 'norwegian', 'no', 'odia', 'or', 
	'pashto', 'ps', 'persian', 'fa', 
	'polish', 'pl', 'portuguese', 'pt', 'punjabi', 
	'pa', 'romanian', 'ro', 'russian', 
	'ru', 'samoan', 'sm', 'scots gaelic', 'gd', 
	'serbian', 'sr', 'sesotho', 'st', 
	'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si', 
	'slovak', 'sk', 'slovenian', 'sl', 
	'somali', 'so', 'spanish', 'es', 'sundanese', 
	'su', 'swahili', 'sw', 'swedish', 
	'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu', 
	'te', 'thai', 'th', 'turkish', 
	'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur', 
	'ug', 'uzbek', 'uz', 
	'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh', 
	'yiddish', 'yi', 'yoruba', 
	'yo', 'zulu', 'zu']




toLangList=['afrikaans', 'af', 'albanian', 'sq', 
	'amharic', 'am', 'arabic', 'ar', 
	'armenian', 'hy', 'azerbaijani', 'az', 
	'basque', 'eu', 'belarusian', 'be', 
	'bengali', 'bn', 'bosnian', 'bs', 'bulgarian', 
	'bg', 'catalan', 'ca', 'cebuano', 
	'ceb', 'chichewa', 'ny', 'chinese (simplified)', 
	'zh-cn', 'chinese (traditional)', 
	'zh-tw', 'corsican', 'co', 'croatian', 'hr', 
	'czech', 'cs', 'danish', 'da', 'dutch', 
	'nl', 'english', 'en', 'esperanto', 'eo', 
	'estonian', 'et', 'filipino', 'tl', 'finnish', 
	'fi', 'french', 'fr', 'frisian', 'fy', 'galician', 
	'gl', 'georgian', 'ka', 'german', 
	'de', 'greek', 'el', 'gujarati', 'gu', 
	'haitian creole', 'ht', 'hausa', 'ha', 
	'hawaiian', 'haw', 'hebrew', 'he', 'hindi', 
	'hi', 'hmong', 'hmn', 'hungarian', 
	'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian', 
	'id', 'irish', 'ga', 'italian', 
	'it', 'japanese', 'ja', 'javanese', 'jw', 
	'kannada', 'kn', 'kazakh', 'kk', 'khmer', 
	'km', 'korean', 'ko', 'kurdish (kurmanji)', 
	'ku', 'kyrgyz', 'ky', 'lao', 'lo', 
	'latin', 'la', 'latvian', 'lv', 'lithuanian', 
	'lt', 'luxembourgish', 'lb', 
	'macedonian', 'mk', 'malagasy', 'mg', 'malay', 
	'ms', 'malayalam', 'ml', 'maltese', 
	'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian', 
	'mn', 'myanmar (burmese)', 'my', 
	'nepali', 'ne', 'norwegian', 'no', 'odia', 'or', 
	'pashto', 'ps', 'persian', 'fa', 
	'polish', 'pl', 'portuguese', 'pt', 'punjabi', 
	'pa', 'romanian', 'ro', 'russian', 
	'ru', 'samoan', 'sm', 'scots gaelic', 'gd', 
	'serbian', 'sr', 'sesotho', 'st', 
	'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si', 
	'slovak', 'sk', 'slovenian', 'sl', 
	'somali', 'so', 'spanish', 'es', 'sundanese', 
	'su', 'swahili', 'sw', 'swedish', 
	'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu', 
	'te', 'thai', 'th', 'turkish', 
	'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur', 
	'ug', 'uzbek', 'uz', 
	'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh', 
	'yiddish', 'yi', 'yoruba', 
	'yo', 'zulu', 'zu']




queue = Queue()
translator = Translator() 





window=Tk()
#window.geometry("1000x600")
window.attributes('-fullscreen', True)
window.title("Arabic to English")
window.configure(background='black')

frame=Frame(window)
frame.pack(side=BOTTOM)

# mytextw will display thr final text
mytextw=Text(window,wrap=WORD,yscrollcommand=YES,font=("Consolas",40),bg='black')
mytextw.pack()

#tags used to change text colors
mytextw.tag_configure("even",foreground='white')
mytextw.tag_configure("odd",foreground='yellow')
tag="even"


''' ##### debug Mic Trans and Qsize lbl

lblMicDebug=Label(frame, text="Micdebug ",background='black',fg='white',font=("Arial",10))
lblMicDebug.pack(side=RIGHT)

lblTransDebug=Label(frame, text="Transdebug ",background='black',fg='white',font=("Arial",10))
lblTransDebug.pack(side=RIGHT,padx=80)

lblqsize=Label(frame, text="qsize ",background='black',fg='white',font=("Arial",10))
lblqsize.pack(side=LEFT)'''

##### from to language lbl and dopdown ######

lblFromLang=Label(frame, text="From: ",font=("Consolas",15))
lblFromLang.pack(side=LEFT)

from_Lang_dropdown=ttk.Combobox(frame, values=fromLangList)
from_Lang_dropdown.pack(side=LEFT,padx=10)
from_Lang_dropdown.current(7)

lblToLang=Label(frame, text="To: ",font=("Consolas",15))
lblToLang.pack(side=LEFT)


to_Lang_dropdown=ttk.Combobox(frame, values=fromLangList)
to_Lang_dropdown.pack(side=LEFT,padx=10)
to_Lang_dropdown.current(43)

############### recog inisialization 

r = sr.Recognizer()


with sr.Microphone() as source:                # use the default microphone as the audio source
	r.adjust_for_ambient_noise(source, duration=1) 


print("Set minimum energy threshold to {}".format(r.energy_threshold) )
    
r.non_speaking_duration=0.2
r.pause_threshold=0.2
r.phrase_threshold=0.5
r.dynamic_energy_threshold = True


############### set languages function


def setLanguages():
    global fromLanguage, toLanguage

    fromLanguage=from_Lang_dropdown.get()
    toLanguage=to_Lang_dropdown.get()
    

################# save to file func
    
def save_to_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                text_content = mytextw.get("1.0", "end-1c")
                file.write(text_content)
            #lblMicDebug.config(text=f"File saved: {file_path}")
        except Exception as e:
            print(text=f"Error saving file: {str(e)}")
            #lblMicDebug.config(text=f"Error saving file: {str(e)}")



#8888888888888888888888888888888888888   voice capture 88888888888888888888888888888888888888888888888888888888
def recordvoice(queue): 
    
    global silence,MicDebugText, qsizetext
     
    with sr.Microphone() as source: 
         
         while True:   
                #lblMicDebug.config(text="listening" )
				
                audio = r.listen(source)
                queue.put(audio)
                #lblMicDebug.config(text="put in queu")
                silence = False
                #lblqsize.config(text=queue.qsize())
                
            
 
#8888888888888888888888888888888888888   transcribe and translate and display 88888888888888888888888888888888888888888888888888888888

def whatsaid(queue):
	global silence, qsizetext,TransDebugText,mytext,tag,fromLanguage,toLanguage
	while True:
		if (queue.qsize()!=0):
			frames = queue.get()
			try:
            
			#lblqsize.config(text=queue.qsize())
            			
				#lblTransDebug.config(text="recgnizing start")
				query = r.recognize_google(frames, language=fromLanguage) 
			except sr.UnknownValueError:
				silence=True
				print("could not understand audio")
				#lblTransDebug.config(text="recgnizing end")
			except sr.RequestError as e:
				silence=True
				print("error; {0}".format(e))
				#lblTransDebug.config(text="error; {0}".format(e))
				#lblTransDebug.config(text=repr(e)) 
				
				
				
			
			if silence==False :
				#lblTransDebug.config(text="translation start")
				text_to_translate = translator.translate(query, dest=toLanguage)
				#lblTransDebug.config(text="translation end")
				
				mytext=text_to_translate.text+ " "
			
				mytextw.insert(INSERT,mytext,tag)
				tag = "even" if tag == "odd" else "odd"
				mytextw.see("end")
            
            
 





#-------------------start the program --------------------------------------- 


def threading1():
	
	
    setLanguages()
    buttonstart.config(state='disabled')
    record = Thread(target=recordvoice,args=(queue,))
    record.start()
    transcribe = Thread(target=whatsaid,args=(queue,))
    transcribe.start()
    record.join()
    transcribe.join()
    
    
    
############################################
    
def threadingSave():
    savetext=Thread(target=save_to_file())
    savetext.start()
    savetext.join()
    

####################### menu buttons


buttonstart=Button(frame,text="Start",font=("Consolas",15),width=5,command=threading.Thread(target=threading1).start)
buttonstart.pack(side=LEFT)

buttonclose=Button(frame,text="Exit",font=("Consolas",15),width=5,command=window.destroy)
buttonclose.pack(side=LEFT)

buttonSave=Button(frame,text="Save",font=("Consolas",15),width=5,command=threading.Thread(target=threadingSave).start)
buttonSave.pack(side=LEFT)


window.mainloop()