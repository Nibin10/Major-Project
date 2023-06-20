from django.shortcuts import render,redirect
#added
#from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Userinfo,Book
#added
#from django.contrib import messages
#from django.core.mail import send_mail
#from django.conf import settings
#import smtplib
from django.http import JsonResponse

import os
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
from gtts import gTTS
from playsound import playsound

def login(request):
    #txt="സോണിയയിലേക് സ്വാഗതം...അന്ധരായവർക്കും കാഴ്ചയില്ലാത്തവർക്കും വേണ്ടി സോണിയ ഒരു ആപ്ലിക്കേഷനാണ്. വാക്കാൽ ഇമെയിൽ സേവനം ഉപയോഗിക്കാൻ സോണിയ ഉപയോക്താവിനെ അനുവദിക്കുന്നു. ഉപയോക്താവിന് വാക്കാലുള്ള ആശയവിനിമയം ഉപയോഗിച്ച് മെയിൽ എഴുതാനും വായിക്കാനും കഴിയും. ഈ ആപ്ലിക്കേഷൻ ഒരു വെർബൽ ഇബുക്ക് ഫംഗ്ഷനും നൽകുന്നു, അവിടെ ഉപയോക്താവിന് തിരഞ്ഞെടുത്ത പുസ്തകങ്ങളുടെ ഓഡിയോ കേൾക്കാനാകും. സോണിയയുടെ വെർബൽ കാൽക്കുലേറ്റർ ഉപയോക്താവിന് മലയാളത്തിൽ കണക്കുകൂട്ടുന്നത് എളുപ്പമാക്കുന്നു. സെർച്ച് എഞ്ചിൻ പോലുള്ള മറ്റ് ആപ്ലിക്കേഷനുകളും സോണിയ ലഭ്യമാക്കിയിട്ടുണ്ട്.തുടരുന്നതിനായി സ്ക്രീനിൽ സ്പർശിക്കുക."
    #mal=gTTS(txt,lang='ml')
    #mal.save("voice.mp3")
    #playsound("voice.mp3")
    #os.remove("voice.mp3")
    return render(request,'login.html')

@login_required
def home(request):
    #txt="സോണിയയ്ക്ക് സ്വാഗതം  .ഇമെയിൽ സേവനത്തിനായി ഇമെയിൽ എന്ന് പറയുക.കാൽക്കുലേറ്റർ ഉപയോഗിക്കാൻ കാൽക്കുലേറ്റർ എന്ന് പറയുക.ഓഡിയോ ബുക്ക് സേവനത്തിനായി ഓഡിയോ ബുക്ക് എന്ന പറയുക.സെർച്ച് എഞ്ചിൻ സേവനത്തിനായി സെർച്ച് എഞ്ചിൻ എന്ന് പറയുക"
    #txt="സോണിയയിലേക് സ്വാഗതം. തുടരുന്നതിനായി സ്ക്രീനിൽ സ്പർശിക്കുക.  "
    #mal=gTTS(txt,lang='ml')
    #mal.save("home.mp3")
    #playsound("home.mp3")
    if request.method =='POST':
        #txt="സോണിയയ്ക്ക് സ്വാഗതം  .ഇമെയിൽ സേവനത്തിനായി ഇമെയിൽ എന്ന് പറയുക.കാൽക്കുലേറ്റർ ഉപയോഗിക്കാൻ കാൽക്കുലേറ്റർ എന്ന് പറയുക.ഓഡിയോ ബുക്ക് സേവനത്തിനായി ഓഡിയോ ബുക്ക് എന്ന പറയുക.സെർച്ച് എഞ്ചിൻ സേവനത്തിനായി സെർച്ച് എഞ്ചിൻ എന്ന് പറയുക"
        #txt="ഇൻസ്ട്രഷൻ വേണമെങ്കിൽ വേണം എന്ന് പറയുക വേണ്ടെങ്കിൽ വേണ്ട എന്ന് പറയുക "
        #mal=gTTS(txt,lang='ml')
        #mal.save("home1.mp3")
        playsound("home1.mp3")
        #os.remove("home1.mp3")
        talk("speak")
        listener = sr.Recognizer()
        infos=""
        def instruction():
            #talk("hello send message")
            txt="സോണിയയിലേക്ക് സ്വാഗതം  .ഇമെയിൽ സേവനത്തിനായി സന്ദേശം എന്ന് പറയുക.കാൽക്കുലേറ്റർ ഉപയോഗിക്കാൻ കാൽക്കുലേറ്റർ എന്ന് പറയുക.ഓഡിയോ ബുക്ക് സേവനത്തിനായി ഓഡിയോ ബുക്ക് എന്ന പറയുക.സെർച്ച് എഞ്ചിൻ സേവനത്തിനായി തിരയുക എന്ന് പറയുക. ലോഗൗട്ട് ചെയ്യുന്നതിനായി നിർത്തുക എന്ന് പറയുക."
            mal=gTTS(txt,lang='ml')
            mal.save("homepost.mp3")
            playsound("homepost.mp3")
            os.remove("homepost.mp3")
        try:
            with sr.Microphone() as source:
                listener.adjust_for_ambient_noise(source)
                voice=listener.record(source,duration=3)
                infos=listener.recognize_google(voice,language="ml-IN")   
        except:
                pass
        if 'വേണ്ട' in infos:
            pass
        else:
            instruction()
        
        talk("speak")  
        info=""
        try:
            with sr.Microphone() as source:
                listener.adjust_for_ambient_noise(source)
                voice=listener.record(source,duration=3)
                info=listener.recognize_google(voice,language="ml-IN")   
        except:
            pass
                
        if 'കാൽക്കുലേറ്റർ' in info:
            return JsonResponse({'result' : 'calculator'})
        elif 'സന്ദേശം' in info:
            return JsonResponse({'result' : 'email'})
        elif 'തിരയുക' in info:
            return JsonResponse({'result' : 'search'})
        elif 'ഓഡിയോ ബുക്ക്' in info:
            return JsonResponse({'result' : 'book'})
        elif 'നിർത്തുക' in info:
            return JsonResponse({'result' : 'logout'})
        else:
            #talk("hello send message")
            return JsonResponse({'result' : 'home'})
    return render(request,'home.html') 
   
def logout(request):
#    auth_logout(request)
    return render(request,'login.html')



import pyttsx3

def spell_string(string):
    # Initialize Text-to-speech engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 60)
    # Loop through each character in the string and spell it
    for char in string:
        engine.say(char)

    # Run the Text-to-speech engine and wait until it finishes
    engine.runAndWait()


 
def talk(text):
    engine =pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def send(request):
    from gtts import gTTS
    import os
    from playsound import playsound
    import speech_recognition as sr
    listener = sr.Recognizer()
    info=""
    talk("speak") 
    try:
            import speech_recognition as sr
            with sr.Microphone() as source:
                listener.adjust_for_ambient_noise(source)
                voice=listener.record(source,duration=3)
                info=listener.recognize_google(voice,language="ml-IN")   
    except:
                pass
    
    #subject = 'Code Band'
    #message = 'Sending Email through Gmail'
    #recipient = 'nibinrajroct2001@gmail.com'
    #send_mail(subject, 
    #    message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
    #messages.success(request, 'Success!')


    #server=smtplib.SMTP('smtp.gmail.com',587)
    #server.starttls()
    #server.login('nibinrajroct2001@gmail.com','nuaqvpdhpoogkklo')
    #server.sendmail('nibinrajroct2001@gmail.com',
    #'nibinrajroct2001@gmail.com',
    #'hi its me')

    #import speech_recognition as sr
    #listener = sr.Recognizer()
    #try:
    #        with sr.Microphone() as source:        
    #                voice=listener.listen(source)
    #                info=listener.recognize_google(voice)
    #                print(info)
    #except:
    #        pass

    
    #talk("hello send message")
    #listener = sr.Recognizer()
    #try:
    #    with sr.Microphone() as source:
    #        listener.adjust_for_ambient_noise(source)
    #        voice=listener.listen(source)
    #        info=listener.recognize_google(voice,language="ml-IN")   
    #except:
    #        pass
    #    
    #if 'കാൽക്കുലേറ്റർ' in info:
    #    return render(request,'calc.html')
    #elif 'ഇമെയിൽ' in info:
    #    return render(request,'email.html')
    #elif 'തിരയൽ' in info:
    #    return render(request,'search.html')

    return render(request,'email.html') 
info1=""
iout=""
def search(request):
    global info1
    global iout
    if request.method =='POST':
        from gtts import gTTS
        import os
        from playsound import playsound
        txt="ഹോം പേജിൽ പോകുന്നതിനായി നിർത്തുക എന്ന് പറയുക , അല്ലെങ്കിൽ സോണിയ യാത്ര തുടരും "
        mal=gTTS(txt,lang='ml')
        mal.save("common.mp3")
        playsound("common.mp3")
        os.remove("common.mp3")
        #talk("speak")
        import speech_recognition as sr
        listener = sr.Recognizer()
        info1=""
        iout=""
        try:
            import speech_recognition as sr
            with sr.Microphone() as source:
                listener.adjust_for_ambient_noise(source)
                voice=listener.record(source,duration=3)
                info1=listener.recognize_google(voice,language="ml-IN")   
        except:
                pass

        if 'നിർത്തുക' in info1:
            return JsonResponse({'result' : 'home'})
        else:
            from googletrans import Translator
            from playsound import playsound
            from gtts import gTTS
            import os
            trans =Translator()
            import speech_recognition as sr
            listener = sr.Recognizer()
            txt="എന്താണ് തിരയാൻ ആഗ്രഹിക്കുന്നത് . "
            mal=gTTS(txt,lang='ml')
            mal.save("dream.mp3")
            playsound("dream.mp3")
            os.remove("dream.mp3")
            info1=""
            try:
                with sr.Microphone() as source:
                    listener.adjust_for_ambient_noise(source)
                    voice=listener.record(source,duration=5)
                    info1=listener.recognize_google(voice,language="ml-IN") 
                    print(info1) 
                    request.infos=info1 
                    input=trans.translate(info1,dest="en")
                    print(input)
                    import wikipedia as wikki
                    out=wikki.summary(input.text,sentences=2)
                    output=trans.translate(out,dest="ml")
                    iout=output.text
                    outputs=gTTS(iout,lang='ml')
                    print(iout)
                    outputs.save("results.mp3")
                    playsound("results.mp3")
                    os.remove("results.mp3")
                    #print(output.text)
                    txt="സോണിയ പറഞ്ഞത് മനസിലായെന്ന് വിശ്വസിക്കുന്നു ,തുടരുന്നതിനായി സ്ക്രീനിൽ സ്പർശിക്കുക."
                    mal=gTTS(txt,lang='ml')
                    mal.save("dream.mp3")
                    playsound("dream.mp3")
                    os.remove("dream.mp3")            
            except:
            
                txt="സോണിയയോട് ക്ഷമിക്കണം , പറഞ്ഞത് മനസിലായില്ല,തുടരുന്നതിനായി സ്ക്രീനിൽ സ്പർശിക്കുക. ."
                mal=gTTS(txt,lang='ml')
                mal.save("dream.mp3")
                playsound("dream.mp3")
                os.remove("dream.mp3")
    infos=info1
    iouts=iout
    return render(request,'search.html',{'infos':infos,'iouts':iouts})
               

voice=""
def email(request): 
    global voice
    if request.method =='POST':
        userlist=Userinfo.objects.all()
        for i in userlist:
            if i.emailid==request.user.email:
                return JsonResponse({'result':'inbox'})
        txt="സോണിയയോട് താങ്കളുടെ ജിമെയിൽ പാസ്സ്‌വേർഡ്  ദയവായി പറയുക , സോണിയയെ നിങ്ങൾക്ക്  വിശ്വസിക്കാം."
        mal=gTTS(txt,lang='ml')
        mal.save("dream1.mp3")
        playsound("dream1.mp3")
        os.remove("dream1.mp3")
        voice=""
        import speech_recognition as sr
        listener = sr.Recognizer()
        try:
            import speech_recognition as sr
            with sr.Microphone() as source:
                username=request.user.username
                print(request.user.username)
                print(request.user.email)
                emailid=request.user.email
                listener.adjust_for_ambient_noise(source)
                voic=listener.record(source,duration=10) 
                voice=listener.recognize_google(voic,language="en")
                x=voice.lower()
                voice=x.replace(" ","")
                #voice="gcmhtimwcxqhuupa"
                print(voice)
                import smtplib
                import speech_recognition as sr
                from email.message import EmailMessage
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                # Make sure to give app access in your Google account
                server.login(emailid,voice)
                adduser=Userinfo(username=username,emailid=emailid,password=voice)
                adduser.save()
                #email = EmailMessage()
                #email['From'] = emailid
                #email['To'] = emailid
                #email['Subject'] = 'set'
                #email.set_content('seti')
                #server.send_message(email)
                txt="വിജയകരമായി  ലോഗിൻ ചെയ്തിരിക്കുന്നു "
                mal=gTTS(txt,lang='ml')
                mal.save("dream.mp3")
                playsound("dream.mp3")
                os.remove("dream.mp3")
                return JsonResponse({'result':'inbox'})
        except:
            txt="താങ്കൾ പറഞ്ഞ പാസ്സ്‌വേർഡ് തെറ്റാണ് ,തുടരുന്നതിനായി സ്ക്രീനിൽ സ്പർശിക്കുക. ."
            mal=gTTS(txt,lang='ml')
            mal.save("dream.mp3")
            playsound("dream.mp3")
            os.remove("dream.mp3")
            

    voices=voice     
    return render(request,'email.html',{'voices':voices})
d={}
u=[]
s=[]
def inbox(request):
    if request.method=='POST':
        global d,u,s
        from playsound import playsound
        import os
        from gtts import gTTS
        import speech_recognition as sr
        listener = sr.Recognizer()
        txt="മെസ്സേജ് വായിക്കണമെങ്കിൽ വായിക്കണം എന്ന് പറയുക ,മെസ്സേജ് അയക്കണം എങ്കിൽ അയക്കണം എന്ന് പറയുക ,ഹോം പേജിലോട്ട്  പോകണമെങ്കിൽ  നിർത്തുക എന്ന് പറയുക ."
        mal=gTTS(txt,lang='ml')
        mal.save("dream1.mp3")
        playsound("dream1.mp3")
        os.remove("dream1.mp3")
        info=""
        try:
            with sr.Microphone() as source:
                listener.adjust_for_ambient_noise(source)
                voice=listener.record(source,duration=3)
                info=listener.recognize_google(voice,language="ml-IN")
                print(info)  
        except:
            pass
                
        if 'വായിക്കണം' in info:
            import imaplib
            import email
            from datetime import datetime
            import pyttsx3
            import os
            # Connect to IMAP server
            imap_server = imaplib.IMAP4_SSL('imap.gmail.com')
            userlist=Userinfo.objects.all()
            for i in userlist:
                if i.emailid==request.user.email:
                    break
            imap_server.login(i.emailid,i.password)
            imap_server.select('inbox')
            #server.login('soniaablind@gmail.com', 'gcmhtimwcxqhuupa')
            # Search for unread emails
            from gtts import gTTS
            from playsound import playsound
            _, message_numbers_raw = imap_server.search(None, 'UNSEEN')
            message_numbers = message_numbers_raw[0].split()
            count=len(message_numbers)
            txt1="താങ്കളുടെ ഇൻബോക്സിൽ ,"
            txt2="വായിക്കാത്ത മെസ്സേജ് ഉണ്ട്"
            if count==0:
                txt="താങ്കളുടെ ഇൻബോക്സിൽ , വായിക്കാത്ത മെസ്സേജ് ഇല്ലാ .എല്ലാ മെസ്സേജും വായിച്ചതാണ്  "
            else:
                if count==1:
                    txt="താങ്കളുടെ ഇൻബോക്സിൽ , വായിക്കാത്ത ഒരു മെസ്സേജ് ഉണ്ട്"
                else:
                    txt=txt1+str(count)+txt2
            print(txt)
            mal=gTTS(txt,lang='ml')
            mal.save("home.mp3")
            playsound("home.mp3")
            os.remove("home.mp3")
            print(count )
            def talk(text):
                engine =pyttsx3.init()
                engine.say(text)
                engine.runAndWait()
            flag=0
            
            d={}
            u=[]
            s=[]
            # Print sender and subject of each unread email
            for num in message_numbers:
                text=""
                flag=flag+1
                _, message_data = imap_server.fetch(num, '(RFC822)')
                message = email.message_from_bytes(message_data[0][1])
                sender = message['From']
                sender_name=email.utils.parseaddr(message['From'])[0]
                sender_email=message['From'].split()[-1]
                subject = message['Subject']
                date = datetime.fromtimestamp(email.utils.mktime_tz(email.utils.parsedate_tz(message['Date'])))
                #print(f'From: {sender} \nSubject: {subject} \nDate: {date}')


                #exist
                """
                if message.is_multipart():
                    # If the message is a multipart (i.e., contains both plain text and HTML versions), get the plain text version
                    for part in message.get_payload():
                        if part.get_content_type() == 'text/plain':
                            text = part.get_payload(decode=True).decode('utf-8')
                else:
                    # If the message is not a multipart, get the message body as is
                    text = message.get_payload(decode=True).decode('utf-8')

                # Print the sender, subject, and text of the message"""
                #exist
                #new
                

                # Print message body
                if message.is_multipart():
                    for part in message.get_payload():
                        if part.get_content_type() == 'text/plain':
                            body = part.get_payload(decode=True).decode()
                            #print('Message:', body)
                            text=body
                else:
                    body = message.get_payload(decode=True).decode()
                    text=body
                    #print('Message:', body)
                #new
                print('Sender:', sender)
                print('sender email',sender_email)
                print('sender name',sender_name)
                print('Subject:', subject)
                #talk(subject)
                #print('Text:', text)
                #talk(text)
                print('Date:',date)
                #talk(date)
                d1={sender_name:subject}
                d.update(d1)
                print(d)
                u.append(sender_name)
                s.append(subject)
                print('-----------------------------------------')  
                txt1="മത്തെ  മെസ്സേജയച്ചിരിക്കുന്നത് ,"
                txt2=" ആണ്  . "
                txt3="എന്ന ജിമെയിലിൽ നിന്ന് ,"
                txt4=".എന്ന സമയത്താണ് മെസ്സേജയച്ചിരിക്കുന്നത് ."
                txt5="അയച്ച മെസ്സേജിന്റെ വിഷയം ."
                txt6=" ,എന്നതാണ് .മെസ്സേജിൽ പറയുന്നത് ഇനി പറയുന്നതാണ്  ,"
                txt=str(flag)+txt1+str(sender_name)+txt2+str(sender_email)+txt3+str(date)+txt4+txt5+str(subject)+txt6+str(text)
                mal=gTTS(txt,lang='ml')
                mal.save("home.mp3")
                playsound("home.mp3")
                os.remove("home.mp3")

                #new
                fname=""
                ftype=""
                for part in message.walk():
                    if part.get_content_maintype() == 'multipart':
                        continue
                    if part.get('Content-Disposition') is None:
                        continue
                    filename = part.get_filename()
                    filetype=part.get_content_type()
                    if filename:
                        print(f'Attachment: {filename}, Type: {filetype}')
                        fname=str(filename)
                        ftype=str(filetype)
                        txt=fname+"എന്ന പേരിലുള്ള "+ftype+"അറ്റാച്ച്മെന്റ് ഉണ്ട് "
                        mal=gTTS(txt,lang='ml')
                        mal.save("home.mp3")
                        playsound("home.mp3")
                        os.remove("home.mp3")

                
                
            print(d)   
            
        elif 'അയക്കണം' in info:
            return JsonResponse({'result' : 'compose'})
        elif 'നിർത്തുക' in info:
            return JsonResponse({'result' : 'home'})
        else:
            #talk("hello send message")
            return JsonResponse({'result' : 'inbox'})
    e=d
    v=u
    t=s 
    return render(request,'inbox.html',{'e':e,'v':v,'t':t})
toid=""
msg=""
sub=""
def convert_special_char(text):
    temp=text
    special_chars = ['attherate','dot','underscore','dollar','hash','star','plus','minus','space','dash']
    for character in special_chars:
        while(True):
            pos=temp.find(character)
            if pos == -1:
                break
            else :
                if character == 'attherate':
                    temp=temp.replace('attherate','@')
                elif character == 'dot':
                    temp=temp.replace('dot','.')
                elif character == 'underscore':
                    temp=temp.replace('underscore','_')
                elif character == 'dollar':
                    temp=temp.replace('dollar','$')
                elif character == 'hash':
                    temp=temp.replace('hash','#')
                elif character == 'star':
                    temp=temp.replace('star','*')
                elif character == 'plus':
                    temp=temp.replace('plus','+')
                elif character == 'minus':
                    temp=temp.replace('minus','-')
                elif character == 'space':
                    temp = temp.replace('space', '')
                elif character == 'dash':
                    temp=temp.replace('dash','-')
    return temp
def compose(request):
    global toid,msg,sub
    if request.method =='POST':
        from gtts import gTTS
        import os
        from playsound import playsound
        txt="ഹോം പേജിൽ പോകുന്നതിനായി നിർത്തുക എന്ന് പറയുക , അല്ലെങ്കിൽ സോണിയ യാത്ര തുടരും "
        mal=gTTS(txt,lang='ml')
        mal.save("common.mp3")
        playsound("common.mp3")
        os.remove("common.mp3")
        #talk("speak")
        import speech_recognition as sr
        listener = sr.Recognizer()
        info1=""
        try:
            import speech_recognition as sr
            with sr.Microphone() as source:
                listener.adjust_for_ambient_noise(source)
                voice=listener.record(source,duration=3)
                info1=listener.recognize_google(voice,language="ml-IN")   
        except:
                pass

        if 'നിർത്തുക' in info1:
            return JsonResponse({'result' : 'home'})
        else:
            def askmsg():
                global msg
                txt="അയക്കണ്ട മെസ്സേജ് എന്താണ് ."
                mal=gTTS(txt,lang='ml')
                mal.save("common.mp3")
                playsound("common.mp3")
                os.remove("common.mp3")
                msg=""
                try:
                    with sr.Microphone() as source:
                        listener.adjust_for_ambient_noise(source)
                        voice=listener.record(source,duration=20)
                        msg=listener.recognize_google(voice,language="ml-IN")
                        print(msg) 
                        mal=gTTS(msg,lang='ml')
                        mal.save("common.mp3")
                        playsound("common.mp3")
                        os.remove("common.mp3")
                        txt="സോണിയ പറഞ്ഞത് ശരിയാണെങ്കിൽ ശരി എന്ന്  പറയുക , ശരിയല്ലെങ്കിൽ ശരിയല്ല എന്ന് പറയുക . "
                        mal=gTTS(txt,lang='ml')
                        mal.save("common.mp3")
                        playsound("common.mp3")
                        os.remove("common.mp3")
                        listener.adjust_for_ambient_noise(source)
                        voice=listener.record(source,duration=3)
                        info=listener.recognize_google(voice,language="ml-IN")
                        if 'ശരി' in info:
                            print("success")
                        else:
                            askmsg()
                except:
                    txt="സോണിയയോട് ക്ഷമിക്കണം,"
                    mal=gTTS(txt,lang='ml')
                    mal.save("common.mp3")
                    playsound("common.mp3")
                    os.remove("common.mp3")
                    print("error")
                    askmsg()
            def asksub():
                global sub
                txt="അയക്കണ്ട മെസ്സേജിന്റെ വിഷയം എന്താണ് ."
                mal=gTTS(txt,lang='ml')
                mal.save("common.mp3")
                playsound("common.mp3")
                os.remove("common.mp3")
                sub=""
                import speech_recognition as sr
                listener = sr.Recognizer()
                try:
                    import speech_recognition as sr
                    with sr.Microphone() as source:
                        listener.adjust_for_ambient_noise(source)
                        voice=listener.record(source,duration=10)
                        sub=listener.recognize_google(voice,language="ml-IN")
                        print(sub) 
                        mal=gTTS(sub,lang='ml')
                        mal.save("common.mp3")
                        playsound("common.mp3")
                        os.remove("common.mp3")
                        txt="സോണിയ പറഞ്ഞത് ശരിയാണെങ്കിൽ ശരി എന്ന്  പറയുക , ശരിയല്ലെങ്കിൽ ശരിയല്ല എന്ന് പറയുക . "
                        mal=gTTS(txt,lang='ml')
                        mal.save("common.mp3")
                        playsound("common.mp3")
                        os.remove("common.mp3")
                        listener.adjust_for_ambient_noise(source)
                        voice=listener.record(source,duration=3)
                        info=listener.recognize_google(voice,language="ml-IN")
                        if 'ശരി' in info:
                            print("success")
                            askmsg()
                        
                        else:
                            asksub()
                except:
                    txt="സോണിയയോട് ക്ഷമിക്കണം,"
                    mal=gTTS(txt,lang='ml')
                    mal.save("common.mp3")
                    playsound("common.mp3")
                    os.remove("common.mp3")
                    print("error")
                    asksub()
            def askmail():
                global toid
                txt="ആർക്കാണ് മെസ്സേജ് അയക്കണ്ടത് , അയക്കേണ്ട ആളുടെ ജിമെയിൽ ഐഡി സോണിയയോട് പറയുക ."
                mal=gTTS(txt,lang='ml')
                mal.save("common.mp3")
                playsound("common.mp3")
                os.remove("common.mp3")
                toid=""
                import speech_recognition as sr
                listener = sr.Recognizer()
                try:
                    import speech_recognition as sr
                    with sr.Microphone() as source:
                        listener.adjust_for_ambient_noise(source)
                        voice=listener.record(source,duration=20)
                        toid=listener.recognize_google(voice) 
                        l=toid.lower() 
                        toid=l.replace(" ","")
                        print(toid) 
                        #talk(toid)
                        txt=str(toid)
                        #txt=txt+txt
                        #mal=gTTS(txt,lang='ml')
                        #mal.save("common.mp3")
                        #playsound("common.mp3")
                        #os.remove("common.mp3")
                        toid=convert_special_char(txt)
                        #for k in txt:
                        #   talk(k)
                        spell_string(toid)
                        txt="സോണിയ പറഞ്ഞത് ശരിയാണെങ്കിൽ ശരി എന്ന്  പറയുക , ശരിയല്ലെങ്കിൽ ശരിയല്ല എന്ന് പറയുക . "
                        mal=gTTS(txt,lang='ml')
                        mal.save("common.mp3")
                        playsound("common.mp3")
                        os.remove("common.mp3")
                        listener.adjust_for_ambient_noise(source)
                        voice=listener.record(source,duration=3)
                        info=listener.recognize_google(voice,language="ml-IN")
                        print(info)
                        if 'ശരി' in info:
                            print("success")
                            asksub()
                        
                        else:
                            askmail()
                except:
                    txt="സോണിയയോട് ക്ഷമിക്കണം,"
                    mal=gTTS(txt,lang='ml')
                    mal.save("common.mp3")
                    playsound("common.mp3")
                    os.remove("common.mp3")
                    print("error")
                    askmail()
            import smtplib
            import speech_recognition as sr
            from email.message import EmailMessage
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            askmail()
            #toid='nibinrajroct2001@gmail.com'
            try:
                #talk("speak")
                #server.login('nibinrajroct2001@gmail.com', 'nuaqvpdhpoogkklo')
                userlist=Userinfo.objects.all()
                for i in userlist:
                    if i.emailid==request.user.email:
                        break
                server.login(i.emailid,i.password)
                email = EmailMessage()
                #email['From'] = 'soniaablind@gmail.com'
                email['To'] = toid
                email['Subject'] = sub
                email.set_content(msg)
                server.send_message(email)
                txt="താങ്കളുടെ മെസ്സേജ് വിജയകരമായി സോണിയ അയച്ചിരിക്കുന്നു ."
                mal=gTTS(txt,lang='ml')
                mal.save("common.mp3")
                playsound("common.mp3")
                os.remove("common.mp3")
                toid=""
                msg=""
                sub=""
                return JsonResponse({'result':'compose'})
            except:
                txt="സോണിയയോട് ക്ഷമിക്കണം മെസ്സേജ് അയക്കാൻ കഴിഞ്ഞില്ല "
                mal=gTTS(txt,lang='ml')
                mal.save("common.mp3")
                playsound("common.mp3")
                os.remove("common.mp3")
                return JsonResponse({'result':'compose'})
    return render(request,'compose.html',{'toid':toid,'msg':msg,'sub':sub})
def readmail(request):
    import imaplib
    import email
    from datetime import datetime
    import pyttsx3
    import os
    # Connect to IMAP server
    imap_server = imaplib.IMAP4_SSL('imap.gmail.com')
    userlist=Userinfo.objects.all()
    for i in userlist:
        if i.emailid==request.user.email:
            break
    imap_server.login(i.emailid,i.password)
    imap_server.select('inbox')
    #server.login('soniaablind@gmail.com', 'gcmhtimwcxqhuupa')
    # Search for unread emails
    from gtts import gTTS
    from playsound import playsound
    _, message_numbers_raw = imap_server.search(None, 'UNSEEN')
    message_numbers = message_numbers_raw[0].split()
    count=len(message_numbers)
    txt1="താങ്കളുടെ ഇൻബോക്സിൽ ,"
    txt2="വായിക്കാത്ത മെസ്സേജ് ഉണ്ട്"
    if count==0:
        txt="താങ്കളുടെ ഇൻബോക്സിൽ , വായിക്കാത്ത മെസ്സേജ് ഇല്ലാ .എല്ലാ മെസ്സേജും വായിച്ചതാണ്  "
    else:
        if count==1:
            txt="താങ്കളുടെ ഇൻബോക്സിൽ , വായിക്കാത്ത ഒരു മെസ്സേജ് ഉണ്ട്"
        else:
            txt=txt1+str(count)+txt2
    print(txt)
    mal=gTTS(txt,lang='ml')
    mal.save("home.mp3")
    playsound("home.mp3")
    os.remove("home.mp3")
    print(count )
    def talk(text):
        engine =pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    flag=0
    d1={}
    d={}
    u=[]
    s=[]
    # Print sender and subject of each unread email
    for num in message_numbers:
        text=""
        flag=flag+1
        _, message_data = imap_server.fetch(num, '(RFC822)')
        message = email.message_from_bytes(message_data[0][1])
        sender = message['From']
        sender_name=email.utils.parseaddr(message['From'])[0]
        sender_email=message['From'].split()[-1]
        subject = message['Subject']
        date = datetime.fromtimestamp(email.utils.mktime_tz(email.utils.parsedate_tz(message['Date'])))
        #print(f'From: {sender} \nSubject: {subject} \nDate: {date}')


        #exist
        """
        if message.is_multipart():
            # If the message is a multipart (i.e., contains both plain text and HTML versions), get the plain text version
            for part in message.get_payload():
                if part.get_content_type() == 'text/plain':
                    text = part.get_payload(decode=True).decode('utf-8')
        else:
            # If the message is not a multipart, get the message body as is
            text = message.get_payload(decode=True).decode('utf-8')

        # Print the sender, subject, and text of the message"""
        #exist
        #new
        

        # Print message body
        if message.is_multipart():
            for part in message.get_payload():
                if part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode=True).decode()
                    #print('Message:', body)
                    text=body
        else:
            body = message.get_payload(decode=True).decode()
            text=body
            #print('Message:', body)
        #new
        print('Sender:', sender)
        print('sender email',sender_email)
        print('sender name',sender_name)
        print('Subject:', subject)
        #talk(subject)
        #print('Text:', text)
        #talk(text)
        print('Date:',date)
        #talk(date)
        d1={sender_name:subject}
        d.update(d1)
        print(d)
        u.append(sender_name)
        s.append(subject)
        print('-----------------------------------------')  
        txt1="മത്തെ  മെസ്സേജയച്ചിരിക്കുന്നത് ,"
        txt2=" ആണ്  . "
        txt3="എന്ന ജിമെയിലിൽ നിന്ന് ,"
        txt4=".എന്ന സമയത്താണ് മെസ്സേജയച്ചിരിക്കുന്നത് ."
        txt5="അയച്ച മെസ്സേജിന്റെ വിഷയം ."
        txt6=" ,എന്നതാണ് .മെസ്സേജിൽ പറയുന്നത് ഇനി പറയുന്നതാണ്  ,"
        txt=str(flag)+txt1+str(sender_name)+txt2+str(sender_email)+txt3+str(date)+txt4+txt5+str(subject)+txt6+str(text)
        mal=gTTS(txt,lang='ml')
        mal.save("home.mp3")
        playsound("home.mp3")
        os.remove("home.mp3")

        #new
        fname=""
        ftype=""
        for part in message.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            filename = part.get_filename()
            filetype=part.get_content_type()
            if filename:
                print(f'Attachment: {filename}, Type: {filetype}')
                fname=str(filename)
                ftype=str(filetype)
                txt=fname+"എന്ന പേരിലുള്ള "+ftype+"അറ്റാച്ച്മെന്റ് ഉണ്ട് "
                mal=gTTS(txt,lang='ml')
                mal.save("home.mp3")
                playsound("home.mp3")
                os.remove("home.mp3")

        
        
    print(d)   
    return render(request,'inbox.html',{'d':d,'u':u,'s':s})
global l 
l=""
def book(request):
    bookadv=Book.objects.filter(category='Adventure')
    bookrom=Book.objects.filter(category='Romance')
    bookfic=Book.objects.filter(category='Fiction')
    bookcrime=Book.objects.filter(category='Horror')
    if request.method=="POST":
        txt="ഹോം പേജിൽ പോകുന്നതിനായി നിർത്തുക എന്ന് പറയുക , അല്ലെങ്കിൽ സോണിയ യാത്ര തുടരും "
        mal=gTTS(txt,lang='ml')
        mal.save("common.mp3")
        playsound("common.mp3")
        os.remove("common.mp3")
        #talk("speak")
        listener = sr.Recognizer()
        info1=""
        try:
            with sr.Microphone() as source:
                listener.adjust_for_ambient_noise(source)
                voice=listener.record(source,duration=3)
                info1=listener.recognize_google(voice,language="ml-IN")   
        except:
                pass

        if 'നിർത്തുക' in info1:
            return JsonResponse({'result':'home'})
        else:
            def askcategory():
                txt="ഏതു ക്യാറ്റഗറിയിൽ ഉള്ള ബുക്ക് ആണ് വേണ്ടത് . അഡ്വഞ്ചർ ബുക്കിനായി അഡ്വഞ്ചർ എന്ന് പറയുക . റൊമാൻസ് ബുക്കിനായി റൊമാൻസ് എന്ന് പറയുക .ഫിക്ഷൻ ബുക്കിനായി ഫിക്ഷൻ എന്ന് പറയുക .ഹൊറർ ബുക്കിനായി ഹൊറർ എന്ന് പറയുക .."
                mal=gTTS(txt,lang='ml')
                mal.save("common.mp3")
                playsound("common.mp3")
                os.remove("common.mp3")
                try:
                    with sr.Microphone() as source:
                        listener.adjust_for_ambient_noise(source)
                        voice=listener.record(source,duration=3)
                        msg=listener.recognize_google(voice,language="ml-IN")
                        print(msg)
                        x="Adventure"
                        Y="Romance"
                        Z="Fiction"
                        P="Horror"
                        global l
                        if "അഡ്വഞ്ചർ" in msg:
                            l=x
                            return x
                        elif "റൊമാൻസ്" in msg:
                            l=Y
                            return Y
                        elif "ഫിക്ഷൻ" in msg:
                            l=Z
                            return Z
                        elif "ഹൊറർ" in msg:
                            l=P
                            return P
                        else:
                            txt="സോണിയയോട് ക്ഷമിക്കണം,"
                            mal=gTTS(txt,lang='ml')
                            mal.save("common.mp3")
                            playsound("common.mp3")
                            os.remove("common.mp3")
                            print("error")
                            askcategory()
                        
                except:
                    txt="സോണിയയോട് ക്ഷമിക്കണം,"
                    mal=gTTS(txt,lang='ml')
                    mal.save("common.mp3")
                    playsound("common.mp3")
                    os.remove("common.mp3")
                    print("error")
                    askcategory()
            def askbook():
                txt="ബുക്കുകളുടെ പേര് ഇനി പറയുന്നതാണ് "
                mal=gTTS(txt,lang='ml')
                mal.save("common.mp3")
                playsound("common.mp3")
                os.remove("common.mp3")
                print(l)
                bookall=Book.objects.filter(category=l)
                for i in bookall:
                    txt=str(i.name)+".എഴുതിയത് "+str(i.author)
                    mal=gTTS(txt,lang='ml')
                    mal.save("common.mp3")
                    playsound("common.mp3")
                    os.remove("common.mp3")
                txt="ഏത് ബുക്ക് ആണ് വേണ്ടത് ബുക്കിന്റെ പേര് പറയുക .ഹോം പേജിൽ പോകുന്നതിനായി നിർത്തുക എന്ന് പറയുക "
                mal=gTTS(txt,lang='ml')
                mal.save("common.mp3")
                playsound("common.mp3")
                os.remove("common.mp3")
                global flag
                try:
                    with sr.Microphone() as source:
                        listener.adjust_for_ambient_noise(source)
                        voice=listener.record(source,duration=8)
                        msg=listener.recognize_google(voice,language="ml-IN")
                        msg=str(msg)
                    print(msg)
                    if 'നിർത്തുക' in msg:
                        return render(request,'home.html')
                    flag=0
                    for i in bookall:
                        global bookid
                        bookid=i
                        txt=i.name
                        #print(txt)
                        if txt==msg:
                            print("book success")
                            flag=1
                            break
                    if flag==0:
                        txt="സോണിയയോട് ക്ഷമിക്കണം,"
                        mal=gTTS(txt,lang='ml')
                        mal.save("common.mp3")
                        playsound("common.mp3")
                        os.remove("common.mp3")
                        askbook()
                except:
                    txt="സോണിയയോട് ക്ഷമിക്കണം,"
                    mal=gTTS(txt,lang='ml')
                    mal.save("common.mp3")
                    playsound("common.mp3")
                    os.remove("common.mp3")
                    print("error")
                    askbook()
            askcategory()
            askbook()       
        if flag==1:
            return JsonResponse({'result':'bookplay'})
    return render(request,'book.html',{'bookadv':bookadv,'bookrom':bookrom,'bookfic':bookfic,'bookcrime':bookcrime})
def bookplay(request):
    #txt="സ്‌ക്രീനിൽ സ്പർശിച്ചു കൊണ്ട് , ബുക്ക് വായിക്കുന്നത് തുടങ്ങാനും , താത്കാലികമായി നിർത്തിവെക്കാനും സാധിക്കും  . തിരിച്ചു ഹോം പേജിലോട്ട് പോകാനായി ,പോസ് ചെയ്തശേഷം നിർത്തുക എന്ന് പറയുക ."
    #mal=gTTS(txt,lang='ml')
    #mal.save("pase.mp3")
    #playsound("pase.mp3")
    #os.remove("home1.mp3")
    print(bookid)
    return render(request,'bookplay.html',{'bookid':bookid})    
result=0
def calculator(request):
    if request.method=="POST":
        global result
        result=0
        txt="ഹോം പേജിൽ പോകുന്നതിനായി നിർത്തുക എന്ന് പറയുക , അല്ലെങ്കിൽ സോണിയ യാത്ര തുടരും "
        mal=gTTS(txt,lang='ml')
        mal.save("common.mp3")
        playsound("common.mp3")
        os.remove("common.mp3")
        #talk("speak")
        import speech_recognition as sr
        listener = sr.Recognizer()
        info1=""
        try:
            import speech_recognition as sr
            with sr.Microphone() as source:
                listener.adjust_for_ambient_noise(source)
                voice=listener.record(source,duration=3)
                info1=listener.recognize_google(voice,language="ml-IN")   
        except:
                pass

        if 'നിർത്തുക' in info1:
            return JsonResponse({'result' : 'home'})
        else:
            txt="കാൽക്കുലേറ്റർ ഇൻസ്ട്രഷൻ വേണമെങ്കിൽ വേണം എന്ന് പറയുക വേണ്ടെങ്കിൽ വേണ്ട എന്ന് പറയുക "
            mal=gTTS(txt,lang='ml')
            mal.save("home23.mp3")
            playsound("home23.mp3")
            os.remove("home23.mp3")
            infos=""
            def instruction():
                #talk("hello send message")
                txt="ഗണിത ക്രമത്തിൽ കൂട്ടുന്നതിനായി കൂട്ടണം എന്ന് പറയുക , കുറക്കാൻ കുറക്കുക എന്ന് പറയുക ,ഗുണിക്കാൻ ഗുണിക്കുക എന്ന് പറയുക ,ഹരിക്കാൻ ഹരിക്കുക എന്ന് പറയുക "
                mal=gTTS(txt,lang='ml')
                mal.save("homepo.mp3")
                playsound("homepo.mp3")
                os.remove("homepo.mp3")
            try:
                with sr.Microphone() as source:
                    listener.adjust_for_ambient_noise(source)
                    voice=listener.record(source,duration=3)
                    infos=listener.recognize_google(voice,language="ml-IN")   
            except:
                    pass
            if 'വേണ്ട' in infos:
                pass
            else:
                instruction()
            #txt="ഹോം പേജിൽ പോകുന്നതിനായി നിർത്തുക എന്ന് പറയുക , അല്ലെങ്കിൽ സോണിയ യാത്ര തുടരും "
            #mal=gTTS(txt,lang='ml')
            #mal.save("dream.mp3")
            #playsound("dream.mp3")
            #os.remove("dream.mp3")       
            #talk("talk")
            def para():
                    try:
                            with sr.Microphone() as source:        
                                    voice=listener.record(source,duration=6)
                                    info=listener.recognize_google(voice,language="ml-IN") 
                                    print(info)
                                    return info
                                    
                    except:
                            pass

                    
            def number():
                    txt="നമ്പർ പറയുക "
                    mal=gTTS(txt,lang='ml')
                    mal.save("dream.mp3")
                    playsound("dream.mp3")
                    os.remove("dream.mp3")
                    global a
                    a=para()
                    c=a
                    txt="താങ്കൾ പറഞ്ഞ നമ്പർ "+str(c)+ "ആണെങ്കിൽ ശരി എന്ന് പറയുക ശെരിയല്ലെങ്കിൽ ശരിയല്ല എന്ന്  പറയുക "
                    mal=gTTS(txt,lang='ml')
                    mal.save("dream.mp3")
                    playsound("dream.mp3")
                    os.remove("dream.mp3")
                    try:
                            with sr.Microphone() as source:        
                                    voice=listener.record(source,duration=3)
                                    info=listener.recognize_google(voice,language="ml-IN") 
                                    print(info)
                                    a=eval(a) 
                                    a=int(a)
                                    if "ശരി" not in info:
                                            number()
                                
                    except:
                            number()
                    
                    

            def nxtnumber():
                    txt="അടുത്ത നമ്പർ പറയുക "
                    mal=gTTS(txt,lang='ml')
                    mal.save("dream.mp3")
                    playsound("dream.mp3")
                    os.remove("dream.mp3")
                    global b
                    b=para()
                    c=b
                    txt="താങ്കൾ പറഞ്ഞ നമ്പർ "+str(c)+ "ആണെങ്കിൽ ശരി എന്ന് പറയുക ശെരിയല്ലെങ്കിൽ ശരിയല്ല എന്ന്  പറയുക "
                    mal=gTTS(txt,lang='ml')
                    mal.save("dream.mp3")
                    playsound("dream.mp3")
                    os.remove("dream.mp3")
                    try:
                            with sr.Microphone() as source:        
                                    voice=listener.record(source,duration=3)
                                    info=listener.recognize_google(voice,language="ml-IN") 
                                    print(info)
                                    b=eval(b) 
                                    b=int(b)
                                    if "ശരി" not in info:
                                            print("ok")
                                            nxtnumber()
                                    
                                    
                            
                    except:
                            nxtnumber()

            def operator():     
                    txt="ഗണിതക്രമം പറയുക "
                    mal=gTTS(txt,lang='ml')
                    mal.save("dream.mp3")
                    playsound("dream.mp3")
                    os.remove("dream.mp3")
                    try:
                            with sr.Microphone() as source:        
                                    voice=listener.record(source,duration=3)
                                    info=listener.recognize_google(voice,language="ml-IN") 
                                    global result
                                    if "കൂട്ടണം" in info:
                                            result=a+b       
                                    elif "കുറയ്ക്കുക" in info:
                                            result=a-b
                                    elif "ഹരിക്കുക" in info:
                                            result=a/b
                                    elif "ഗുണിക്കുക" in info:
                                            result=a*b
                                            
                                    else :
                                            operator()
                    except Exception as e:
                            print(e)
                            operator()
            def res():
                    nxtnumber()
                    operator()
                    print(result)
                    d=result
                    if d>0 :
                        txt="ഉത്തരം"+str(d)+" ആണ് .ഉത്തരം"+str(d)+" ആണ് .ഈ നമ്പറിന്റെ കൂടെ ഇനീം എന്തേലും ആഡ് ചെയ്യണോ ചെയ്യണമെങ്കിൽ വേണം എന്ന് പറയുക അല്ലെങ്കിൽ വേണ്ട എന്ന് പറയുക  "
                    else:
                        txt="ഉത്തരം മൈനസ്"+str(d)+" ആണ് . ഉത്തരം മൈനസ്"+str(d)+" ആണ് .ഈ നമ്പറിന്റെ കൂടെ ഇനീം എന്തേലും ആഡ് ചെയ്യണോ ചെയ്യണമെങ്കിൽ വേണം എന്ന് പറയുക അല്ലെങ്കിൽ വേണ്ട എന്ന് പറയുക  "

                    mal=gTTS(txt,lang='ml')
                    mal.save("dream.mp3")
                    playsound("dream.mp3")
                    os.remove("dream.mp3")
                    try:
                            with sr.Microphone() as source:        
                                    voice=listener.record(source,duration=3)
                                    info=listener.recognize_google(voice,language="ml-IN") 
                                    print(info)
                                    if "വേണം" in info:
                                            global a
                                            a=result
                                            res()
                                    else:
                                         txt=" തുടരുന്നതിനായി സ്ക്രീനിൽ സ്പർശിക്കുക."
                                         mal=gTTS(txt,lang='ml')
                                         mal.save("dream.mp3")
                                         playsound("dream.mp3")
                                         os.remove("dream.mp3")
                                         return JsonResponse({'result':'calculator'})
                    except:
                            txt=" തുടരുന്നതിനായി സ്ക്രീനിൽ സ്പർശിക്കുക."
                            mal=gTTS(txt,lang='ml')
                            mal.save("dream.mp3")
                            playsound("dream.mp3")
                            os.remove("dream.mp3")
                            return JsonResponse({'result':'calculator'})
            number()
            res()
    return render(request,'calculator.html',{'result':result})
