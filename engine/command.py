import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    text = str(text)
    
    # Transform text with personality manager
    try:
        from engine.personality_manager import personality_manager
        text = personality_manager.transform_response(text)
    except Exception as e:
        print(f"Personality transform error: {e}")
    
    # Get current language from multilingual support
    try:
        from engine.multilingual_support import multilingual
        current_language = multilingual.current_language
    except:
        current_language = 'english'
    
    try:
        eel.DisplayMessage(text)
    except:
        print(f"Jarvis: {text}")
    
    # Handle TTS based on language
    try:
        # For non-English languages, use gTTS
        if current_language != 'english':
            try:
                from gtts import gTTS
                import pygame
                import io
                import os
                
                # Get language code for gTTS
                lang_codes = {
                    'kannada': 'kn',
                    'hindi': 'hi',
                    'bengali': 'bn',
                    'gujarati': 'gu',
                    'malayalam': 'ml',
                    'marathi': 'mr',
                    'tamil': 'ta',
                    'telugu': 'te',
                    'urdu': 'ur'
                }
                
                lang_code = lang_codes.get(current_language, 'en')
                
                # Generate speech using gTTS
                tts = gTTS(text=text, lang=lang_code, slow=False)
                
                # Save to memory buffer
                mp3_buffer = io.BytesIO()
                tts.write_to_fp(mp3_buffer)
                mp3_buffer.seek(0)
                
                # Play using pygame
                pygame.mixer.init()
                pygame.mixer.music.load(mp3_buffer)
                pygame.mixer.music.play()
                
                # Wait for playback to complete
                while pygame.mixer.music.get_busy():
                    pygame.time.wait(100)
                
                pygame.mixer.quit()
                
            except Exception as e:
                print(f"gTTS error: {e}")
                # Fallback to voice gender control for non-English
                from engine.voice_gender_control import voice_control
                voice_control.speak_with_gender(text)
        else:
            # For English, use voice gender control
            from engine.voice_gender_control import voice_control
            success = voice_control.speak_with_gender(text)
            if not success:
                # Final fallback to basic pyttsx3
                engine = pyttsx3.init('sapi5')
                voices = engine.getProperty('voices')
                engine.setProperty('voice', voices[0].id)
                engine.setProperty('rate', 174)
                engine.say(text)
                engine.runAndWait()
                
    except Exception as e:
        print(f"TTS error: {e}")
        # Final fallback to basic pyttsx3
        try:
            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.setProperty('rate', 174)
            engine.say(text)
            engine.runAndWait()
        except:
            print(f"All TTS methods failed for: {text}")
    
    try:
        eel.receiverText(text)
    except:
        pass

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        try:
            eel.DisplayMessage('listening....')
        except:
            pass
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=3)
        except sr.WaitTimeoutError:
            print("Listening timeout - no speech detected")
            return ""

    try:
        print('recognizing')
        try:
            eel.DisplayMessage('recognizing....')
        except:
            pass
        
        # Get current language for speech recognition
        try:
            from engine.multilingual_support import multilingual
            current_language = multilingual.current_language
        except:
            current_language = 'english'
        
        # Set recognition language based on current language
        try:
            from engine.multilingual_support import multilingual
            recognition_language = multilingual.get_speech_recognition_language()
        except:
            recognition_language = 'en-IN'
        
        query = r.recognize_google(audio, language=recognition_language)
        print(f"user said: {query}")
        try:
            eel.DisplayMessage(query)
        except:
            pass
        time.sleep(1)
    except Exception as e:
        print(f"Recognition error: {e}")
        return ""
    
    return query.lower()

@eel.expose
def allCommands(message=1):
    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        try:
            eel.senderText(query)
        except:
            print(f"User: {query}")
    
    try:
        print(f"Processing query: '{query}'")
        
        # Contact-based calling and messaging
        if "send message" in query or "phone call" in query or "video call" in query or "call" in query:
            from engine.features import findContact, whatsApp, makeCall, sendMessage
            contact_no, name = findContact(query)
            if contact_no != 0:
                speak("Which mode you want to use whatsapp or mobile")
                preference = takecommand()
                print(preference)

                if "mobile" in preference:
                    if "send message" in query or "send sms" in query: 
                        speak("what message to send")
                        message = takecommand()
                        sendMessage(message, contact_no, name)
                    elif "phone call" in query or "call" in query:
                        makeCall(name, contact_no)
                    else:
                        speak("please try again")
                elif "whatsapp" in preference:
                    message = ""
                    if "send message" in query:
                        message = 'message'
                        speak("what message to send")
                        query = takecommand()
                                        
                    elif "phone call" in query or "call" in query:
                        message = 'call'
                    else:
                        message = 'video call'
                                        
                    whatsApp(contact_no, query, message, name)
            eel.ShowHood()
            return
        
        # SMS Test Commands
        elif "test sms" in query or "sms test" in query:
            from engine.features import testSMS
            testSMS()
            eel.ShowHood()
            return
        
        # Phone Commands (must have "on phone" suffix)
        elif "on phone" in query:
            from engine.phone import handle_phone_commands
            if handle_phone_commands(query):
                eel.ShowHood()
                return
        
        # Language switching commands
        elif "switch to" in query or "change language" in query:
            try:
                from engine.multilingual_support import multilingual
                response = multilingual.process_multilingual_command(query)
                speak(response)
            except Exception as e:
                print(f"Language switch error: {e}")
                speak("Language switching is not available")
            eel.ShowHood()
            return
        
        # Voice gender switching commands - handle before dual AI
        elif "voice" in query.lower() and any(word in query.lower() for word in ["male", "female", "switch", "current", "status"]):
            try:
                from engine.voice_gender_control import voice_control
                query_lower = query.lower()
                
                if "female voice" in query_lower or "switch to female" in query_lower:
                    response = voice_control.switch_to_female()
                    speak(response)
                elif "male voice" in query_lower or "switch to male" in query_lower:
                    response = voice_control.switch_to_male()
                    speak(response)
                elif "current voice" in query_lower or "voice status" in query_lower:
                    gender = voice_control.get_current_gender()
                    speak(f"Current voice is set to {gender}")
                    
            except Exception as e:
                print(f"Voice switch error: {e}")
                speak("Voice switching failed")
            eel.ShowHood()
            return
        
        # Everything else handled by Dual AI (reliable functions only)
        else:
            from engine.dual_ai import dual_ai
            # Use dual_ai.execute instead of get_simple_response for multilingual support
            response = dual_ai.execute(query)
            speak(response)
            try:
                pass
            except Exception as e:
                print(f"Simple AI Error: {e}")
                # Get error message in current language
                try:
                    from engine.multilingual_support import multilingual
                    speak(multilingual.get_response('processing'))
                except:
                    speak("I'm processing your request")
            
    except Exception as e:
        print(f"Error in allCommands: {e}")
        speak("Something went wrong")
    
    try:
        eel.ShowHood()
    except:
        pass