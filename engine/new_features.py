"""
New Features Extension - Single file to add features without modifying dual_ai.py
"""

import subprocess
import os
import datetime
import threading
import time
import socket

class NewFeatures:
    def __init__(self):
        self.features = {
            # Utility Tools
            'weather_forecast': self.weather_forecast,
            'qr_code_generator': self.qr_code_generator,
            'password_generator': self.password_generator,
            'color_picker': self.color_picker,
            'text_to_speech_file': self.text_to_speech_file,
            'image_converter': self.image_converter,
            'empty_trash': self.empty_trash,
            
            # Productivity Tools
            'pomodoro_timer': self.pomodoro_timer,
            'pomodoro_test': self.pomodoro_test,
            'break_reminder': self.break_reminder,
            'word_count': self.word_count,
            'text_cleaner': self.text_cleaner,
            'url_shortener': self.url_shortener,
            
            # File Management
            'duplicate_finder': self.duplicate_finder,
            'file_organizer': self.file_organizer,
            'batch_rename': self.batch_rename,
            'folder_size': self.folder_size,
            'recent_files': self.recent_files,
            'compress_files': self.compress_files,
            'extract_archive': self.extract_archive,
            
            # PDF Operations
            'merge_pdf': self.merge_pdf,
            'split_pdf': self.split_pdf,
            'pdf_to_text': self.pdf_to_text,
            'pdf_to_images': self.pdf_to_images,
            'pdf_encrypt': self.pdf_encrypt,
            'pdf_decrypt': self.pdf_decrypt,
            'pdf_compress': self.pdf_compress,
            'pdf_rotate': self.pdf_rotate,
            'pdf_watermark': self.pdf_watermark,
            
            # Document Conversion
            'images_to_pdf': self.images_to_pdf,
            'word_to_pdf': self.word_to_pdf,
            'excel_to_pdf': self.excel_to_pdf,
            'powerpoint_to_pdf': self.powerpoint_to_pdf,
            'html_to_pdf': self.html_to_pdf,
            'text_to_pdf': self.text_to_pdf,
            
            # Advanced Productivity
            'email_templates': self.email_templates,
            'meeting_scheduler': self.meeting_scheduler,
            'task_reminder': self.task_reminder,
            'list_reminders': self.list_reminders,
            
            # Media Tools
            'image_editor': self.image_editor,
            'audio_converter': self.audio_converter,
            'video_downloader': self.video_downloader,
            
            # Recording Tools
            'voice_recorder': self.voice_recorder,
            'screen_recorder': self.screen_recorder,
            
            # Health & Wellness
            'water_reminder': self.water_reminder,
            'exercise_timer': self.exercise_timer,
            'calorie_calculator': self.calorie_calculator,
            'sleep_tracker': self.sleep_tracker,
            'stress_meter': self.stress_meter,
            'mood_tracker': self.mood_tracker,
            'heart_rate_monitor': self.heart_rate_monitor,
            'medication_reminder': self.medication_reminder,
            'bmi_calculator': self.bmi_calculator,
            'system_monitor': self.system_monitor,
            'network_monitor': self.network_monitor,
            
            # Learning & Education
            'language_translator': self.language_translator,
            'dictionary_lookup': self.dictionary_lookup,
            'wikipedia_search': self.wikipedia_search,
            'calculator_advanced': self.calculator_advanced,
            'unit_converter': self.unit_converter,
            'flashcard_system': self.flashcard_system,
            'quiz_generator': self.quiz_generator,
            
            # Creative Tools
            'meme_generator': self.meme_generator,
            'logo_generator': self.logo_generator,
            'color_palette_generator': self.color_palette_generator,
            'font_viewer': self.font_viewer,
            'ascii_art_generator': self.ascii_art_generator,
            'barcode_generator': self.barcode_generator,
            'mind_map_creator': self.mind_map_creator,
            
            # Security & Development Tools
            'password_manager': self.password_manager,
            'startup_manager': self.startup_manager,
            'git_helper': self.git_helper,
            'port_scanner': self.port_scanner,
            'email_sender': self.email_sender,
        }
        
        self.natural_mappings = {
            # Utility Tools
            'weather': 'weather_forecast', 'weather forecast': 'weather_forecast',
            'qr code': 'qr_code_generator', 'generate qr': 'qr_code_generator',
            'password': 'password_generator', 'generate password': 'password_generator',
            'color picker': 'color_picker', 'pick color': 'color_picker',
            'text to speech': 'text_to_speech_file', 'convert to audio': 'text_to_speech_file',
            'convert image': 'image_converter', 'image format': 'image_converter',
            'empty trash': 'empty_trash', 'clear trash': 'empty_trash',
            
            # Productivity Tools
            'pomodoro': 'pomodoro_timer', 'work timer': 'pomodoro_timer',
            'pomodoro test': 'pomodoro_test', 'test timer': 'pomodoro_test',
            'break reminder': 'break_reminder', 'remind break': 'break_reminder',
            'word count': 'word_count', 'count words': 'word_count',
            'clean text': 'text_cleaner', 'format text': 'text_cleaner',
            'shorten url': 'url_shortener', 'short link': 'url_shortener',
            
            # File Management
            'find duplicates': 'duplicate_finder', 'duplicate files': 'duplicate_finder',
            'organize files': 'file_organizer', 'organize downloads': 'file_organizer',
            'rename files': 'batch_rename', 'batch rename': 'batch_rename',
            'folder size': 'folder_size', 'calculate size': 'folder_size',
            'recent files': 'recent_files', 'show recent': 'recent_files',
            'compress files': 'compress_files', 'create zip': 'compress_files',
            'extract archive': 'extract_archive', 'extract zip': 'extract_archive',
            
            # PDF Operations
            'merge pdf': 'merge_pdf', 'combine pdf': 'merge_pdf',
            'split pdf': 'split_pdf', 'divide pdf': 'split_pdf',
            'pdf to text': 'pdf_to_text', 'extract text': 'pdf_to_text',
            'pdf to images': 'pdf_to_images', 'convert pdf': 'pdf_to_images',
            'encrypt pdf': 'pdf_encrypt', 'protect pdf': 'pdf_encrypt', 'pdf encrypt': 'pdf_encrypt',
            'decrypt pdf': 'pdf_decrypt', 'unlock pdf': 'pdf_decrypt', 'pdf decrypt': 'pdf_decrypt',
            'compress pdf': 'pdf_compress', 'reduce pdf': 'pdf_compress',
            'rotate pdf': 'pdf_rotate', 'turn pdf': 'pdf_rotate',
            'watermark pdf': 'pdf_watermark', 'add watermark': 'pdf_watermark',
            
            # Document Conversion
            'images to pdf': 'images_to_pdf', 'create pdf': 'images_to_pdf',
            'word to pdf': 'word_to_pdf', 'docx to pdf': 'word_to_pdf',
            'excel to pdf': 'excel_to_pdf', 'xlsx to pdf': 'excel_to_pdf',
            'powerpoint to pdf': 'powerpoint_to_pdf', 'pptx to pdf': 'powerpoint_to_pdf',
            'html to pdf': 'html_to_pdf', 'webpage to pdf': 'html_to_pdf',
            'text to pdf': 'text_to_pdf', 'txt to pdf': 'text_to_pdf',
            
            # Advanced Productivity
            'email templates': 'email_templates', 'email template': 'email_templates',
            'meeting scheduler': 'meeting_scheduler', 'schedule meeting': 'meeting_scheduler',
            'task reminder': 'task_reminder', 'set reminder': 'task_reminder',
            'list reminders': 'list_reminders', 'show reminders': 'list_reminders',
            
            # Media Tools
            'image editor': 'image_editor', 'edit image': 'image_editor',
            'audio converter': 'audio_converter', 'convert audio': 'audio_converter',
            'video downloader': 'video_downloader', 'download video': 'video_downloader',
            
            # Recording Tools
            'voice recorder': 'voice_recorder', 'record voice': 'voice_recorder',
            'screen recorder': 'screen_recorder', 'record screen': 'screen_recorder',
            
            # Health & Wellness
            'water reminder': 'water_reminder', 'hydration tracker': 'water_reminder',
            'exercise timer': 'exercise_timer', 'workout timer': 'exercise_timer',
            'calorie calculator': 'calorie_calculator', 'food tracker': 'calorie_calculator',
            'sleep tracker': 'sleep_tracker', 'bedtime reminder': 'sleep_tracker',
            'stress meter': 'stress_meter', 'wellness check': 'stress_meter',
            'mood tracker': 'mood_tracker', 'mood check': 'mood_tracker',
            'heart rate': 'heart_rate_monitor', 'pulse check': 'heart_rate_monitor',
            'medication reminder': 'medication_reminder', 'pill reminder': 'medication_reminder',
            'bmi calculator': 'bmi_calculator', 'body mass index': 'bmi_calculator',
            'system monitor': 'system_monitor', 'system status': 'system_monitor',
            'network monitor': 'network_monitor', 'network status': 'network_monitor',
            
            # Learning & Education
            'translate': 'language_translator', 'translation': 'language_translator',
            'dictionary': 'dictionary_lookup', 'define': 'dictionary_lookup',
            'wikipedia': 'wikipedia_search', 'wiki': 'wikipedia_search',
            'calculator': 'calculator_advanced', 'calculate': 'calculator_advanced',
            'convert': 'unit_converter', 'unit conversion': 'unit_converter',
            'flashcard': 'flashcard_system', 'study cards': 'flashcard_system',
            'quiz': 'quiz_generator', 'test me': 'quiz_generator',
            
            # Creative Tools
            'meme': 'meme_generator', 'create meme': 'meme_generator',
            'logo': 'logo_generator', 'create logo': 'logo_generator',
            'color palette': 'color_palette_generator', 'colors': 'color_palette_generator',
            'font': 'font_viewer', 'fonts': 'font_viewer',
            'ascii art': 'ascii_art_generator', 'ascii': 'ascii_art_generator',
            'barcode': 'barcode_generator', 'qr code': 'qr_code_generator',
            'mind map': 'mind_map_creator', 'mindmap': 'mind_map_creator',
            
            # Security & Development Tools
            'password manager': 'password_manager', 'show password': 'password_manager',
            'startup manager': 'startup_manager', 'startup apps': 'startup_manager',
            'git helper': 'git_helper', 'git commit': 'git_helper', 'git push': 'git_helper',
            'port scanner': 'port_scanner', 'scan ports': 'port_scanner',
            'email sender': 'email_sender', 'send email': 'email_sender',
        }
    
    def execute(self, query):
        try:
            # Handle dynamic PDF operations with file paths
            import re
            
            # PDF encrypt with file path
            if 'encrypt pdf' in query.lower() or 'pdf encrypt' in query.lower():
                pattern = r'(?:encrypt pdf|pdf encrypt)\s+(.+)'
                file_match = re.search(pattern, query.lower())
                if file_match:
                    pdf_file = file_match.group(1).strip()
                    result = self.pdf_encrypt(pdf_file)
                    print(result)
                    return result
                result = self.pdf_encrypt()
                print(result)
                return result
            
            # PDF decrypt with file path
            if 'decrypt pdf' in query.lower() or 'pdf decrypt' in query.lower():
                pattern = r'(?:decrypt pdf|pdf decrypt)\s+(.+)'
                file_match = re.search(pattern, query.lower())
                if file_match:
                    pdf_file = file_match.group(1).strip()
                    result = self.pdf_decrypt(pdf_file)
                    print(result)
                    return result
                result = self.pdf_decrypt()
                print(result)
                return result
            
            # Split PDF with file path
            if 'split pdf' in query.lower():
                file_match = re.search(r'split pdf\s+([^\s]+)(?:\s+pages?\s+([\d,-]+))?', query.lower())
                if file_match:
                    pdf_file = file_match.group(1).strip()
                    page_range = file_match.group(2).strip() if file_match.group(2) else None
                    result = self.split_pdf(pdf_file, page_range)
                    print(result)
                    return result
                result = self.split_pdf()
                print(result)
                return result
            
            # Other PDF operations with file paths
            pdf_ops = {
                'merge pdf': (r'merge pdf\s+(.+)', self.merge_pdf),
                'pdf to text': (r'pdf to text\s+(.+)', self.pdf_to_text),
                'pdf to images': (r'pdf to images\s+(.+)', self.pdf_to_images),
                'compress pdf': (r'compress pdf\s+(.+)', self.pdf_compress),
                'rotate pdf': (r'rotate pdf\s+(.+)', self.pdf_rotate),
                'watermark pdf': (r'watermark pdf\s+(.+)', self.pdf_watermark)
            }
            
            for cmd, (pattern, func) in pdf_ops.items():
                if cmd in query.lower():
                    file_match = re.search(pattern, query.lower())
                    if file_match:
                        if cmd == 'merge pdf':
                            files = file_match.group(1).strip().split()
                            result = func(files)
                            print(result)
                            return result
                        else:
                            pdf_file = file_match.group(1).strip()
                            result = func(pdf_file)
                            print(result)
                            return result
                    result = func()
                    print(result)
                    return result
            
            # Check for food tracking (only 'add food' keyword)
            if 'add food' in query.lower():
                return self.calorie_calculator(query)
            
            # Check for password manager first (highest priority for password commands)
            if any(phrase in query.lower() for phrase in ['add', 'store', 'show', 'get']) and 'password' in query.lower():
                return self.password_manager(query)
            if 'password manager' in query.lower():
                return self.password_manager(query)
            
            # Check for creative tools first (highest priority)
            if any(word in query.lower() for word in ['meme', 'create meme']):
                return self.meme_generator(query)
            if any(word in query.lower() for word in ['logo', 'create logo']):
                return self.logo_generator(query)
            if any(word in query.lower() for word in ['color palette', 'colors']) and 'calorie' not in query.lower():
                return self.color_palette_generator(query)
            if any(word in query.lower() for word in ['ascii art', 'ascii']):
                return self.ascii_art_generator(query)
            if 'barcode' in query.lower():
                return self.barcode_generator(query)
            if any(word in query.lower() for word in ['mind map', 'mindmap']):
                return self.mind_map_creator(query)
            
            # Check for learning features (high priority)
            if any(word in query.lower() for word in ['translate', 'translation']):
                return self.language_translator(query)
            if any(word in query.lower() for word in ['define', 'dictionary']):
                return self.dictionary_lookup(query)
            if any(word in query.lower() for word in ['wikipedia', 'wiki']):
                return self.wikipedia_search(query)
            if any(word in query.lower() for word in ['calculate', 'calculator']) and not any(word in query.lower() for word in ['calorie', 'food']):
                return self.calculator_advanced(query)
            if 'convert' in query.lower() and any(word in query.lower() for word in ['meters', 'feet', 'kg', 'pounds', 'celsius', 'fahrenheit']):
                return self.unit_converter(query)
            if any(word in query.lower() for word in ['flashcard', 'study']):
                return self.flashcard_system(query)
            if 'quiz' in query.lower():
                return self.quiz_generator(query)
            
            # Check for email writing
            if 'write email' in query.lower() or 'compose email' in query.lower():
                return self.email_templates(query)
            
            # Check for exact matches first
            query_lower = query.lower().strip()
            if query_lower in self.features:
                func_name = query_lower
            else:
                # Try natural language understanding first
                func_name = self.understand_natural_speech(query)
                
                if not func_name:
                    # Final fallback to AI model for function selection
                    try:
                        from engine.dual_ai import dual_ai
                        prompt = f'User said: "{query}"\nAvailable functions: {list(self.features.keys())}\nRespond with ONLY the function name or "none":'
                        
                        if dual_ai.ai_provider == 'groq':
                            response = dual_ai.groq_client.chat.completions.create(
                                messages=[{"role": "user", "content": prompt}],
                                model="llama-3.1-8b-instant"
                            )
                            func_name = response.choices[0].message.content.strip()
                        else:
                            response = dual_ai.gemini_model.generate_content(prompt)
                            func_name = response.text.strip()
                    except:
                        func_name = None

            if func_name in self.features:
                # Pass query to advanced productivity functions
                if func_name in ['weather_forecast', 'email_templates', 'meeting_scheduler', 'task_reminder', 'list_reminders', 'image_editor', 'audio_converter', 'video_downloader', 'voice_recorder', 'screen_recorder', 'water_reminder', 'exercise_timer', 'calorie_calculator', 'sleep_tracker', 'stress_meter', 'mood_tracker', 'heart_rate_monitor', 'medication_reminder', 'bmi_calculator', 'system_monitor', 'network_monitor', 'language_translator', 'dictionary_lookup', 'wikipedia_search', 'calculator_advanced', 'unit_converter', 'flashcard_system', 'quiz_generator', 'meme_generator', 'logo_generator', 'color_palette_generator', 'font_viewer', 'ascii_art_generator', 'barcode_generator', 'mind_map_creator', 'password_manager', 'startup_manager', 'git_helper', 'port_scanner', 'email_sender']:
                    result = self.features[func_name](query)
                    if func_name in ['voice_recorder', 'screen_recorder', 'water_reminder', 'exercise_timer', 'calorie_calculator', 'sleep_tracker', 'stress_meter', 'mood_tracker', 'heart_rate_monitor', 'medication_reminder', 'bmi_calculator', 'system_monitor', 'network_monitor', 'language_translator', 'dictionary_lookup', 'wikipedia_search', 'calculator_advanced', 'unit_converter', 'flashcard_system', 'quiz_generator', 'meme_generator', 'logo_generator', 'color_palette_generator', 'font_viewer', 'ascii_art_generator', 'barcode_generator', 'mind_map_creator', 'password_manager', 'startup_manager', 'git_helper', 'port_scanner', 'email_sender']:
                        print(result)
                else:
                    result = self.features[func_name]()
                    print(result if result else f"{func_name} completed")
                return result if result else f"{func_name} completed"
            else:
                return None
                
        except Exception as e:
            return f"Error: {str(e)}"
    
    def understand_natural_speech(self, query):
        """Natural language processing for new features functions"""
        query = query.lower().strip()
        
        mappings = {
            # Utility Tools
            'weather_forecast': ['weather', 'weather forecast', 'how is weather'],
            'qr_code_generator': ['qr code', 'generate qr', 'create qr', 'qr generator'],
            'password_generator': ['password', 'generate password', 'create password'],
            'color_picker': ['color picker', 'pick color', 'get color'],
            'text_to_speech_file': ['text to speech', 'convert to audio', 'make audio'],
            'image_converter': ['convert image', 'image format', 'change image'],
            'empty_trash': ['empty trash', 'clear trash', 'clean recycle bin'],
            
            # Productivity Tools
            'pomodoro_timer': ['pomodoro', 'work timer', 'focus timer'],
            'pomodoro_test': ['pomodoro test', 'test timer'],
            'break_reminder': ['break reminder', 'remind break', 'set break'],
            'word_count': ['word count', 'count words'],
            'text_cleaner': ['clean text', 'format text'],
            'url_shortener': ['shorten url', 'short link', 'url shortener'],
            
            # File Management
            'duplicate_finder': ['find duplicates', 'duplicate files'],
            'file_organizer': ['organize files', 'organize downloads'],
            'batch_rename': ['rename files', 'batch rename'],
            'folder_size': ['folder size', 'calculate size'],
            'recent_files': ['recent files', 'show recent'],
            'compress_files': ['compress files', 'create zip', 'make archive'],
            'extract_archive': ['extract archive', 'extract zip', 'unzip'],
            
            # PDF Operations
            'merge_pdf': ['merge pdf', 'combine pdf', 'join pdf'],
            'split_pdf': ['split pdf', 'divide pdf', 'separate pdf'],
            'pdf_to_text': ['pdf to text', 'extract text'],
            'pdf_to_images': ['pdf to images', 'convert pdf'],
            'pdf_encrypt': ['encrypt pdf', 'protect pdf', 'secure pdf'],
            'pdf_decrypt': ['decrypt pdf', 'unlock pdf'],
            'pdf_compress': ['compress pdf', 'reduce pdf size'],
            'pdf_rotate': ['rotate pdf', 'turn pdf'],
            'pdf_watermark': ['watermark pdf', 'add watermark'],
            
            # Document Conversion
            'images_to_pdf': ['images to pdf', 'create pdf'],
            'word_to_pdf': ['word to pdf', 'doc to pdf', 'docx to pdf'],
            'excel_to_pdf': ['excel to pdf', 'xls to pdf', 'xlsx to pdf'],
            'powerpoint_to_pdf': ['powerpoint to pdf', 'ppt to pdf', 'pptx to pdf'],
            'html_to_pdf': ['html to pdf', 'web to pdf'],
            'text_to_pdf': ['text to pdf', 'txt to pdf'],
            
            # Advanced Productivity
            'email_templates': ['email templates', 'email template', 'create email', 'email draft'],
            'meeting_scheduler': ['meeting scheduler', 'schedule meeting', 'book meeting', 'calendar meeting'],
            'task_reminder': ['task reminder', 'set reminder', 'remind me', 'task alert'],
            'list_reminders': ['list reminders', 'show reminders', 'what are reminders', 'my reminders'],
            
            # Media Tools
            'image_editor': ['image editor', 'edit image', 'photo editor', 'image filter'],
            'audio_converter': ['audio converter', 'convert audio', 'audio format', 'mp3 converter'],
            'video_downloader': ['video downloader', 'download video', 'youtube download', 'video download'],
            
            # Recording Tools
            'voice_recorder': ['voice recorder', 'record voice', 'audio recorder', 'voice memo', 'record audio'],
            'screen_recorder': ['screen recorder', 'record screen', 'screen capture', 'record desktop', 'capture screen'],
            
            # Health & Wellness
            'water_reminder': ['water reminder', 'hydration tracker', 'drink water', 'water intake', 'hydration alert'],
            'exercise_timer': ['exercise timer', 'workout timer', 'hiit timer', 'fitness timer', 'interval timer'],
            'calorie_calculator': ['calorie calculator', 'food tracker', 'calorie counter', 'nutrition tracker', 'diet tracker', 'ate', 'add food', 'food'],
            'sleep_tracker': ['sleep tracker', 'bedtime reminder', 'sleep schedule', 'sleep timer', 'bedtime alert', 'bedtime', 'set bedtime', 'wake time', 'set wake'],
            'stress_meter': ['stress meter', 'wellness check', 'stress level', 'mental health', 'stress assessment'],
            'mood_tracker': ['mood tracker', 'mood check', 'how feeling', 'emotional state', 'mood log'],
            'heart_rate_monitor': ['heart rate', 'pulse check', 'heart monitor', 'bpm check', 'pulse rate'],
            'medication_reminder': ['medication reminder', 'pill reminder', 'medicine alert', 'drug reminder', 'take pills'],
            'bmi_calculator': ['bmi calculator', 'body mass index', 'weight check', 'health index', 'body weight'],
            
            # Learning & Education
            'language_translator': ['translate', 'translation', 'translate to', 'convert language'],
            'dictionary_lookup': ['define', 'dictionary', 'definition', 'meaning of', 'what is'],
            'wikipedia_search': ['wikipedia', 'wiki', 'search wiki', 'wiki search'],
            'calculator_advanced': ['calculate', 'calculator', 'math', 'solve', 'compute'],
            'unit_converter': ['convert', 'conversion', 'unit convert', 'change unit'],
            'flashcard_system': ['flashcard', 'study cards', 'flash cards', 'study', 'review cards'],
            'quiz_generator': ['quiz', 'test me', 'generate quiz', 'create quiz', 'quiz on'],
            
            # Creative Tools
            'meme_generator': ['meme', 'create meme', 'generate meme', 'meme generator', 'funny meme'],
            'logo_generator': ['logo', 'create logo', 'design logo', 'logo generator', 'company logo'],
            'color_palette_generator': ['color palette', 'colors', 'color scheme', 'palette', 'color generator'],
            'font_viewer': ['font', 'fonts', 'font viewer', 'preview fonts', 'system fonts'],
            'ascii_art_generator': ['ascii art', 'ascii', 'text art', 'ascii generator', 'character art'],
            'barcode_generator': ['barcode', 'generate barcode', 'create barcode', 'barcode generator'],
            'mind_map_creator': ['mind map', 'mindmap', 'create mind map', 'mind mapping', 'brainstorm'],
            
            # Security & Development Tools
            'password_manager': ['password manager', 'show password', 'get password', 'gmail password', 'password for'],
            'startup_manager': ['startup manager', 'startup apps', 'add startup', 'remove startup', 'manage startup'],
            'git_helper': ['git helper', 'git commit', 'git push', 'git status', 'git add', 'git pull'],
            'port_scanner': ['port scanner', 'scan ports', 'security scan', 'network scan', 'check ports'],
            'email_sender': ['email sender', 'send email', 'send message', 'email to', 'compose and send']
        }
        
        # Check for exact phrase matches first
        for func_name, phrases in mappings.items():
            for phrase in phrases:
                if phrase in query:
                    return func_name
        
        # Special handling for weather with location
        if any(word in query.lower() for word in ['weather']):
            return 'weather_forecast'
        
        # Special handling for bedtime/sleep commands
        if any(word in query for word in ['bedtime', 'wake']):
            return 'sleep_tracker'
        
        # AI-powered food detection for calorie calculator
        if any(word in query.lower() for word in ['ate', 'add', 'food', 'calorie', 'eat', 'drink']):
            return 'calorie_calculator'
        
        # Use AI to detect if query contains food items
        try:
            from engine.dual_ai import dual_ai
            food_check_prompt = f'Does this text mention any food, drink, or meal? Answer only YES or NO: "{query}"'
            
            if dual_ai.ai_provider == 'groq':
                response = dual_ai.groq_client.chat.completions.create(
                    messages=[{"role": "user", "content": food_check_prompt}],
                    model="llama-3.1-8b-instant"
                )
                ai_response = response.choices[0].message.content.strip().upper()
            else:
                response = dual_ai.gemini_model.generate_content(food_check_prompt)
                ai_response = response.text.strip().upper()
            
            if 'YES' in ai_response:
                return 'calorie_calculator'
        except:
            pass
        
        return None
    
    def weather_forecast(self, query=""):
        try:
            import requests
            import re
            
            # Extract location from query
            location = "current location"
            if query:
                # Remove common weather words to get location
                location_match = re.search(r'weather\s+(?:in\s+|for\s+|at\s+)?(.+)', query.lower())
                if location_match:
                    location = location_match.group(1).strip()
            
            # Use free weather API (wttr.in)
            if location == "current location":
                # Try to get location from IP
                try:
                    ip_response = requests.get('https://ipapi.co/json/', timeout=5)
                    if ip_response.status_code == 200:
                        ip_data = ip_response.json()
                        location = f"{ip_data.get('city', 'Unknown')}, {ip_data.get('country_name', 'Unknown')}"
                except:
                    location = "auto"
            
            # Get weather data from wttr.in (free, no API key needed)
            weather_url = f"https://wttr.in/{location}?format=j1"
            response = requests.get(weather_url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                # Current weather
                current = data['current_condition'][0]
                location_info = data['nearest_area'][0]
                
                temp_c = current['temp_C']
                temp_f = current['temp_F']
                humidity = current['humidity']
                description = current['weatherDesc'][0]['value']
                wind_speed = current['windspeedKmph']
                wind_dir = current['winddir16Point']
                feels_like = current['FeelsLikeC']
                visibility = current['visibility']
                pressure = current['pressure']
                
                # Location details
                area_name = location_info['areaName'][0]['value']
                country = location_info['country'][0]['value']
                
                # Today's forecast
                today_forecast = data['weather'][0]
                max_temp = today_forecast['maxtempC']
                min_temp = today_forecast['mintempC']
                
                # Format weather report
                weather_report = f"Weather for {area_name}, {country}:\n"
                weather_report += f"Current: {temp_c}°C ({temp_f}°F) - {description}\n"
                weather_report += f"Feels like: {feels_like}°C\n"
                weather_report += f"Today: {min_temp}°C to {max_temp}°C\n"
                weather_report += f"Humidity: {humidity}%\n"
                weather_report += f"Wind: {wind_speed} km/h {wind_dir}\n"
                weather_report += f"Pressure: {pressure} mb\n"
                weather_report += f"Visibility: {visibility} km"
                
                return weather_report
            else:
                return f"Weather data not available for '{location}'"
                
        except ImportError:
            return "Weather feature requires: pip install requests"
        except requests.exceptions.RequestException:
            return "Weather service unavailable (check internet connection)"
        except Exception as e:
            return f"Weather forecast failed: {e}"
    
    def password_generator(self, length=12):
        import random, string
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ''.join(random.choice(chars) for _ in range(length))
        return f"Generated password: {password}"
    
    def color_picker(self):
        try:
            import pyautogui
            x, y = pyautogui.position()
            screenshot = pyautogui.screenshot()
            color = screenshot.getpixel((x, y))
            hex_color = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
            return f"Color at cursor: RGB{color} | HEX: {hex_color}"
        except Exception as e:
            return f"Color picker failed: {e}"
    
    def text_to_speech_file(self, text="Hello from Jarvis"):
        try:
            import pyttsx3
            engine = pyttsx3.init()
            
            voices = engine.getProperty('voices')
            if voices:
                engine.setProperty('voice', voices[0].id)
            engine.setProperty('rate', 150)
            engine.setProperty('volume', 0.9)
            
            filename = f"speech_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
            engine.save_to_file(text, filename)
            engine.runAndWait()
            
            return f"🔊 Audio file created: '{filename}' | Text: '{text[:50]}...'" if len(text) > 50 else f"🔊 Audio file created: '{filename}' | Text: '{text}'"
        except Exception as e:
            return f"Text-to-speech failed: {e}"
    
    def image_converter(self, input_file="image.jpg", output_format="png"):
        try:
            from PIL import Image
            if not os.path.exists(input_file):
                return f"Image file '{input_file}' not found"
            
            output_format = output_format.replace('.', '').lower()
            
            img = Image.open(input_file)
            output_file = f"{os.path.splitext(input_file)[0]}.{output_format}"
            
            if output_format in ['jpg', 'jpeg']:
                img = img.convert('RGB')
            
            img.save(output_file)
            return f"✅ Converted '{input_file}' to '{output_file}'"
        except Exception as e:
            return f"Image conversion failed: {e}"
    
    def empty_trash(self):
        try:
            subprocess.run('powershell -c "Clear-RecycleBin -Force"', shell=True)
            return "Recycle bin emptied successfully"
        except Exception as e:
            return f"Empty trash failed: {e}"
    
    def pomodoro_timer(self):
        self._show_notification("🍅 Pomodoro Started", "Working for 25 minutes...")
        
        def timer():
            time.sleep(1500)
            self._show_notification("🍅 Pomodoro Complete!", "Take a 5-minute break. Great work!")
        
        threading.Thread(target=timer, daemon=True).start()
        return "🍅 25-minute Pomodoro timer started - Check your notification!"
    
    def break_reminder(self, minutes=30):
        if minutes <= 0 or minutes > 480:
            minutes = 30
        
        self._show_notification("⏰ Break Reminder Set", f"Will remind you in {minutes} minutes")
        
        def reminder():
            time.sleep(minutes * 60)
            self._show_notification("⏰ Break Time!", f"You've been working for {minutes} minutes. Time for a break!")
        
        threading.Thread(target=reminder, daemon=True).start()
        return f"⏰ Break reminder set for {minutes} minutes - Check your notification!"

    def pomodoro_test(self):
        self._show_notification("🍅 TEST: Pomodoro Started", "Will complete in 10 seconds...")
        
        def test_timer():
            time.sleep(10)
            self._show_notification("🍅 TEST: Pomodoro Complete!", "This was a 10-second test.")
        
        threading.Thread(target=test_timer, daemon=True).start()
        return "🍅 TEST: 10-second Pomodoro timer started - Check notifications!"
    
    def _show_notification(self, title, message):
        try:
            import tkinter as tk
            from tkinter import messagebox
            
            root = tk.Tk()
            root.withdraw()
            root.attributes('-topmost', True)
            
            messagebox.showinfo(title, message)
            root.destroy()
        except Exception as e:
            print(f"NOTIFICATION: {title} - {message}")
    
    def word_count(self):
        try:
            import pyperclip
            text = pyperclip.paste()
            words = len(text.split())
            chars = len(text)
            return f"Word count: {words} words, {chars} characters"
        except Exception as e:
            return f"Word count failed: {e}"
    
    def text_cleaner(self):
        try:
            import pyperclip, re
            text = pyperclip.paste()
            cleaned = re.sub(r'\s+', ' ', text).strip()
            pyperclip.copy(cleaned)
            return "Text cleaned and copied to clipboard"
        except Exception as e:
            return f"Text cleaner failed: {e}"
    
    def url_shortener(self, url="https://example.com"):
        try:
            import urllib.parse, urllib.request
            
            parsed = urllib.parse.urlparse(url)
            if not parsed.scheme:
                url = 'https://' + url
            
            api_url = f"http://tinyurl.com/api-create.php?url={urllib.parse.quote(url)}"
            response = urllib.request.urlopen(api_url)
            short_url = response.read().decode('utf-8')
            
            try:
                import pyperclip
                pyperclip.copy(short_url)
                clipboard_msg = " (copied to clipboard)"
            except:
                clipboard_msg = ""
            
            return f"🔗 Short URL: {short_url}{clipboard_msg}"
        except Exception as e:
            return f"URL shortener failed: {e}"
    
    def duplicate_finder(self, folder=None):
        try:
            if folder is None:
                folder = "."
            import hashlib
            files = {}
            duplicates = []
            for root, dirs, filenames in os.walk(folder):
                for filename in filenames:
                    filepath = os.path.join(root, filename)
                    try:
                        with open(filepath, 'rb') as f:
                            file_hash = hashlib.md5(f.read()).hexdigest()
                        if file_hash in files:
                            duplicates.append((filepath, files[file_hash]))
                        else:
                            files[file_hash] = filepath
                    except:
                        continue
            return f"Found {len(duplicates)} duplicate file pairs in {folder}"
        except Exception as e:
            return f"Duplicate finder failed: {e}"
    
    def file_organizer(self, folder=None):
        try:
            if folder is None:
                folder = os.path.join(os.path.expanduser("~"), "Downloads")
            extensions = {
                'images': ['.jpg', '.png', '.gif', '.bmp'],
                'documents': ['.pdf', '.doc', '.txt', '.docx'],
                'videos': ['.mp4', '.avi', '.mkv', '.mov'],
                'music': ['.mp3', '.wav', '.flac']
            }
            organized = 0
            for filename in os.listdir(folder):
                filepath = os.path.join(folder, filename)
                if os.path.isfile(filepath):
                    ext = os.path.splitext(filename)[1].lower()
                    for folder_name, exts in extensions.items():
                        if ext in exts:
                            folder_path = os.path.join(folder, folder_name)
                            os.makedirs(folder_path, exist_ok=True)
                            new_path = os.path.join(folder_path, filename)
                            if not os.path.exists(new_path):
                                os.rename(filepath, new_path)
                                organized += 1
                            break
            return f"Organized {organized} files in {folder}"
        except Exception as e:
            return f"File organizer failed: {e}"
    
    def batch_rename(self, folder=None, prefix="file_"):
        try:
            if folder is None:
                folder = "."
            count = 0
            for i, filename in enumerate(os.listdir(folder)):
                if os.path.isfile(os.path.join(folder, filename)):
                    ext = os.path.splitext(filename)[1]
                    new_name = f"{prefix}{i+1:03d}{ext}"
                    old_path = os.path.join(folder, filename)
                    new_path = os.path.join(folder, new_name)
                    if not os.path.exists(new_path):
                        os.rename(old_path, new_path)
                        count += 1
            return f"Renamed {count} files with prefix '{prefix}' in {folder}"
        except Exception as e:
            return f"Batch rename failed: {e}"
    
    def folder_size(self, folder=None):
        try:
            if folder is None:
                folder = "."
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(folder):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    try:
                        total_size += os.path.getsize(filepath)
                    except:
                        continue
            size_mb = total_size / (1024 * 1024)
            return f"Folder size: {size_mb:.2f} MB ({total_size:,} bytes) in {folder}"
        except Exception as e:
            return f"Folder size calculation failed: {e}"
    
    def recent_files(self, count=10, folder=None):
        try:
            if folder is None:
                folder = "."
            recent = []
            for root, dirs, files in os.walk(folder):
                for file in files:
                    filepath = os.path.join(root, file)
                    try:
                        mtime = os.path.getmtime(filepath)
                        recent.append((filepath, mtime))
                    except:
                        continue
            recent.sort(key=lambda x: x[1], reverse=True)
            result = f"Recent {count} files in {folder}:\n"
            for filepath, mtime in recent[:count]:
                result += f"- {os.path.basename(filepath)}\n"
            return result
        except Exception as e:
            return f"Recent files failed: {e}"
    
    def qr_code_generator(self, text="Hello World"):
        try:
            import qrcode
            from PIL import Image
            
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color="#0078FF", back_color="white").convert('RGB')
            
            filename = f"jarvis_qr_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            img.save(filename)
            return f"✅ QR Code generated for '{text}': {filename}"
            
        except ImportError:
            return "QR code library not installed. Run: pip install qrcode[pil] pillow"
        except Exception as e:
            return f"QR code generation failed: {str(e)}"
    
    def compress_files(self, folder=None, output_name=None):
        try:
            import zipfile
            if folder is None:
                folder = "."
            if output_name is None:
                output_name = f"archive_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
            
            with zipfile.ZipFile(output_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(folder):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, folder)
                        zipf.write(file_path, arcname)
            
            return f"📦 Compressed {folder} to {output_name}"
        except Exception as e:
            return f"Compression failed: {e}"
    
    def extract_archive(self, archive_path=None, extract_to=None):
        try:
            if archive_path is None:
                return "Please specify archive path"
            if extract_to is None:
                extract_to = os.path.splitext(archive_path)[0]
            
            os.makedirs(extract_to, exist_ok=True)
            
            if archive_path.lower().endswith('.zip'):
                import zipfile
                with zipfile.ZipFile(archive_path, 'r') as zipf:
                    zipf.extractall(extract_to)
                return f"📂 Extracted ZIP to {extract_to}"
            elif archive_path.lower().endswith('.rar'):
                try:
                    import rarfile
                    with rarfile.RarFile(archive_path, 'r') as rarf:
                        rarf.extractall(extract_to)
                    return f"📂 Extracted RAR to {extract_to}"
                except ImportError:
                    return "RAR support not installed. Run: pip install rarfile"
            else:
                return "Unsupported archive format. Supports ZIP and RAR only."
        except Exception as e:
            return f"Extraction failed: {e}"
    
    def merge_pdf(self, pdf_files=None):
        try:
            from PyPDF2 import PdfMerger
            if not pdf_files:
                return "Please specify PDF files to merge"
            
            merger = PdfMerger()
            for pdf in pdf_files:
                if os.path.exists(pdf):
                    merger.append(pdf)
            
            output_name = f"merged_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            merger.write(output_name)
            merger.close()
            return f"📄 Merged {len(pdf_files)} PDFs into {output_name}"
        except ImportError:
            return "PDF library not installed. Run: pip install PyPDF2"
        except Exception as e:
            return f"PDF merge failed: {e}"
    
    def split_pdf(self, pdf_file=None, page_range=None):
        try:
            from PyPDF2 import PdfReader, PdfWriter
            if not pdf_file or not os.path.exists(pdf_file):
                return "Please specify valid PDF file"
            
            reader = PdfReader(pdf_file)
            base_name = os.path.splitext(pdf_file)[0]
            
            if page_range:
                # Parse page range (e.g., "1-3", "2,4,6", "5")
                pages_to_split = []
                if '-' in page_range:
                    start, end = map(int, page_range.split('-'))
                    pages_to_split = list(range(start-1, min(end, len(reader.pages))))
                elif ',' in page_range:
                    pages_to_split = [int(p.strip())-1 for p in page_range.split(',') if int(p.strip())-1 < len(reader.pages)]
                else:
                    page_num = int(page_range) - 1
                    if 0 <= page_num < len(reader.pages):
                        pages_to_split = [page_num]
                
                for i in pages_to_split:
                    writer = PdfWriter()
                    writer.add_page(reader.pages[i])
                    output_name = f"{base_name}_page_{i+1}.pdf"
                    with open(output_name, 'wb') as output_file:
                        writer.write(output_file)
                
                return f"📄 Split {len(pages_to_split)} pages from PDF"
            else:
                # Split all pages
                for i, page in enumerate(reader.pages):
                    writer = PdfWriter()
                    writer.add_page(page)
                    output_name = f"{base_name}_page_{i+1}.pdf"
                    with open(output_name, 'wb') as output_file:
                        writer.write(output_file)
                
                return f"📄 Split PDF into {len(reader.pages)} pages"
        except ImportError:
            return "PDF library not installed. Run: pip install PyPDF2"
        except Exception as e:
            return f"PDF split failed: {e}"
    
    def pdf_to_text(self, pdf_file=None):
        try:
            from PyPDF2 import PdfReader
            if not pdf_file or not os.path.exists(pdf_file):
                return "Please specify valid PDF file"
            
            reader = PdfReader(pdf_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            
            output_name = f"{os.path.splitext(pdf_file)[0]}.txt"
            with open(output_name, 'w', encoding='utf-8') as f:
                f.write(text)
            
            return f"📝 Extracted text to {output_name}"
        except ImportError:
            return "PDF library not installed. Run: pip install PyPDF2"
        except Exception as e:
            return f"PDF to text failed: {e}"
    
    def pdf_to_images(self, pdf_file=None):
        try:
            try:
                import fitz  # PyMuPDF
            except ImportError:
                return "PDF library not installed. Run: pip install PyMuPDF"
            
            if not pdf_file or not os.path.exists(pdf_file):
                return "Please specify valid PDF file"
            
            doc = fitz.open(pdf_file)
            base_name = os.path.splitext(pdf_file)[0]
            
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                pix = page.get_pixmap()
                output_name = f"{base_name}_page_{page_num+1}.png"
                pix.save(output_name)
            
            doc.close()
            return f"🖼️ Converted PDF to {len(doc)} images"
        except Exception as e:
            return f"PDF to images failed: {e}"
    
    def images_to_pdf(self, image_folder=None):
        try:
            from PIL import Image
            if not image_folder:
                image_folder = "."
            
            images = []
            for file in os.listdir(image_folder):
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                    img_path = os.path.join(image_folder, file)
                    img = Image.open(img_path).convert('RGB')
                    images.append(img)
            
            if images:
                output_name = f"images_to_pdf_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
                images[0].save(output_name, save_all=True, append_images=images[1:])
                return f"📄 Created PDF from {len(images)} images: {output_name}"
            else:
                return "No images found in folder"
        except ImportError:
            return "PIL library not installed. Run: pip install Pillow"
        except Exception as e:
            return f"Images to PDF failed: {e}"
    
    def word_to_pdf(self, doc_file=None):
        try:
            import win32com.client
            if not doc_file or not os.path.exists(doc_file):
                return "Please specify valid Word document"
            
            word = win32com.client.Dispatch("Word.Application")
            word.Visible = False
            doc = word.Documents.Open(os.path.abspath(doc_file))
            output_name = f"{os.path.splitext(doc_file)[0]}.pdf"
            doc.SaveAs(os.path.abspath(output_name), FileFormat=17)
            doc.Close()
            word.Quit()
            
            return f"📄 Converted Word to PDF: {output_name}"
        except ImportError:
            return "Word automation not available. Install: pip install pywin32"
        except Exception as e:
            return f"Word to PDF failed: {e}"
    
    def excel_to_pdf(self, excel_file=None):
        try:
            import win32com.client
            if not excel_file or not os.path.exists(excel_file):
                return "Please specify valid Excel file"
            
            excel = win32com.client.Dispatch("Excel.Application")
            excel.Visible = False
            wb = excel.Workbooks.Open(os.path.abspath(excel_file))
            output_name = f"{os.path.splitext(excel_file)[0]}.pdf"
            wb.ExportAsFixedFormat(0, os.path.abspath(output_name))
            wb.Close()
            excel.Quit()
            
            return f"📄 Converted Excel to PDF: {output_name}"
        except ImportError:
            return "Excel automation not available. Install: pip install pywin32"
        except Exception as e:
            return f"Excel to PDF failed: {e}"
    
    def powerpoint_to_pdf(self, ppt_file=None):
        try:
            import win32com.client
            if not ppt_file or not os.path.exists(ppt_file):
                return "Please specify valid PowerPoint file"
            
            ppt = win32com.client.Dispatch("PowerPoint.Application")
            ppt.Visible = 1
            presentation = ppt.Presentations.Open(os.path.abspath(ppt_file))
            output_name = f"{os.path.splitext(ppt_file)[0]}.pdf"
            presentation.SaveAs(os.path.abspath(output_name), 32)
            presentation.Close()
            ppt.Quit()
            
            return f"📄 Converted PowerPoint to PDF: {output_name}"
        except ImportError:
            return "PowerPoint automation not available. Install: pip install pywin32"
        except Exception as e:
            return f"PowerPoint to PDF failed: {e}"
    
    def html_to_pdf(self, html_file=None):
        try:
            import pdfkit
            if not html_file or not os.path.exists(html_file):
                return "Please specify valid HTML file"
            
            output_name = f"{os.path.splitext(html_file)[0]}.pdf"
            pdfkit.from_file(html_file, output_name)
            
            return f"📄 Converted HTML to PDF: {output_name}"
        except ImportError:
            return "HTML to PDF library not installed. Run: pip install pdfkit"
        except Exception as e:
            return f"HTML to PDF failed: {e}"
    
    def text_to_pdf(self, text_file=None):
        try:
            from reportlab.pdfgen import canvas
            from reportlab.lib.pagesizes import letter
            
            if not text_file or not os.path.exists(text_file):
                return "Please specify valid text file"
            
            with open(text_file, 'r', encoding='utf-8') as f:
                text = f.read()
            
            output_name = f"{os.path.splitext(text_file)[0]}.pdf"
            c = canvas.Canvas(output_name, pagesize=letter)
            
            lines = text.split('\n')
            y = 750
            for line in lines:
                if y < 50:
                    c.showPage()
                    y = 750
                c.drawString(50, y, line[:80])
                y -= 15
            
            c.save()
            return f"📄 Converted text to PDF: {output_name}"
        except ImportError:
            return "PDF library not installed. Run: pip install reportlab"
        except Exception as e:
            return f"Text to PDF failed: {e}"
    
    def pdf_encrypt(self, pdf_file=None, password="jarvis123"):
        try:
            from PyPDF2 import PdfReader, PdfWriter
            if not pdf_file or not os.path.exists(pdf_file):
                return "Please specify valid PDF file"
            
            reader = PdfReader(pdf_file)
            writer = PdfWriter()
            
            for page in reader.pages:
                writer.add_page(page)
            
            writer.encrypt(password)
            output_name = f"{os.path.splitext(pdf_file)[0]}_encrypted.pdf"
            
            with open(output_name, 'wb') as output_file:
                writer.write(output_file)
            
            return f"🔒 Encrypted PDF: {output_name} (password: {password})"
        except ImportError:
            return "PDF library not installed. Run: pip install PyPDF2"
        except Exception as e:
            return f"PDF encryption failed: {e}"
    
    def pdf_decrypt(self, pdf_file=None, password="jarvis123"):
        try:
            from PyPDF2 import PdfReader, PdfWriter
            if not pdf_file or not os.path.exists(pdf_file):
                return "Please specify valid PDF file"
            
            reader = PdfReader(pdf_file)
            if reader.is_encrypted:
                reader.decrypt(password)
            
            writer = PdfWriter()
            for page in reader.pages:
                writer.add_page(page)
            
            output_name = f"{os.path.splitext(pdf_file)[0]}_decrypted.pdf"
            with open(output_name, 'wb') as output_file:
                writer.write(output_file)
            
            return f"🔓 Decrypted PDF: {output_name}"
        except ImportError:
            return "PDF library not installed. Run: pip install PyPDF2"
        except Exception as e:
            return f"PDF decryption failed: {e}"
    
    def pdf_compress(self, pdf_file=None):
        try:
            from PyPDF2 import PdfReader, PdfWriter
            if not pdf_file or not os.path.exists(pdf_file):
                return "Please specify valid PDF file"
            
            reader = PdfReader(pdf_file)
            writer = PdfWriter()
            
            for page in reader.pages:
                page.compress_content_streams()
                writer.add_page(page)
            
            output_name = f"{os.path.splitext(pdf_file)[0]}_compressed.pdf"
            with open(output_name, 'wb') as output_file:
                writer.write(output_file)
            
            original_size = os.path.getsize(pdf_file)
            compressed_size = os.path.getsize(output_name)
            reduction = ((original_size - compressed_size) / original_size) * 100
            
            return f"🗜️ Compressed PDF: {output_name} ({reduction:.1f}% reduction)"
        except ImportError:
            return "PDF library not installed. Run: pip install PyPDF2"
        except Exception as e:
            return f"PDF compression failed: {e}"
    
    def pdf_rotate(self, pdf_file=None, angle=90):
        try:
            from PyPDF2 import PdfReader, PdfWriter
            if not pdf_file or not os.path.exists(pdf_file):
                return "Please specify valid PDF file"
            
            reader = PdfReader(pdf_file)
            writer = PdfWriter()
            
            for page in reader.pages:
                page.rotate(angle)
                writer.add_page(page)
            
            output_name = f"{os.path.splitext(pdf_file)[0]}_rotated.pdf"
            with open(output_name, 'wb') as output_file:
                writer.write(output_file)
            
            return f"🔄 Rotated PDF {angle}°: {output_name}"
        except ImportError:
            return "PDF library not installed. Run: pip install PyPDF2"
        except Exception as e:
            return f"PDF rotation failed: {e}"
    
    def pdf_watermark(self, pdf_file=None, watermark_text="JARVIS"):
        try:
            from reportlab.pdfgen import canvas
            from reportlab.lib.pagesizes import letter
            from PyPDF2 import PdfReader, PdfWriter
            import io
            
            if not pdf_file or not os.path.exists(pdf_file):
                return "Please specify valid PDF file"
            
            # Create watermark
            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=letter)
            can.setFont("Helvetica", 50)
            can.setFillAlpha(0.3)
            can.rotate(45)
            can.drawString(200, 200, watermark_text)
            can.save()
            
            packet.seek(0)
            watermark_pdf = PdfReader(packet)
            
            # Apply watermark
            reader = PdfReader(pdf_file)
            writer = PdfWriter()
            
            for page in reader.pages:
                page.merge_page(watermark_pdf.pages[0])
                writer.add_page(page)
            
            output_name = f"{os.path.splitext(pdf_file)[0]}_watermarked.pdf"
            with open(output_name, 'wb') as output_file:
                writer.write(output_file)
            
            return f"💧 Added watermark to PDF: {output_name}"
        except ImportError:
            return "PDF libraries not installed. Run: pip install PyPDF2 reportlab"
        except Exception as e:
            return f"PDF watermark failed: {e}"
    
    def email_templates(self, query=""):
        try:
            # Check if user wants AI-generated email
            if 'write email' in query.lower() or 'compose email' in query.lower():
                return self._generate_ai_email(query)
            
            # Use predefined templates
            templates = {
                'meeting': "Subject: Meeting Request\n\nHi [Name],\n\nI'd like to schedule a meeting to discuss [Topic]. Are you available [Date/Time]?\n\nBest regards,\n[Your Name]",
                'followup': "Subject: Follow-up on [Topic]\n\nHi [Name],\n\nI wanted to follow up on our previous discussion about [Topic]. Please let me know if you need any additional information.\n\nBest regards,\n[Your Name]",
                'thankyou': "Subject: Thank You\n\nHi [Name],\n\nThank you for [Reason]. I really appreciate your time and assistance.\n\nBest regards,\n[Your Name]",
                'apology': "Subject: Apology\n\nHi [Name],\n\nI apologize for [Issue]. I will ensure this doesn't happen again in the future.\n\nBest regards,\n[Your Name]",
                'outofoffice': "Subject: Out of Office\n\nI am currently out of the office from [Start Date] to [End Date]. I will respond to your email when I return.\n\nFor urgent matters, please contact [Contact Person] at [Email/Phone]."
            }
            
            # Extract template type from query
            template_type = "meeting"  # default
            query_lower = query.lower()
            
            if 'apology' in query_lower or 'sorry' in query_lower:
                template_type = 'apology'
            elif 'followup' in query_lower or 'follow up' in query_lower:
                template_type = 'followup'
            elif 'thank' in query_lower:
                template_type = 'thankyou'
            elif 'out of office' in query_lower or 'vacation' in query_lower:
                template_type = 'outofoffice'
            elif 'meeting' in query_lower:
                template_type = 'meeting'
            
            template = templates.get(template_type, templates['meeting'])
            
            try:
                import pyperclip
                pyperclip.copy(template)
                return f"📧 Email template '{template_type}' copied to clipboard\n\n{template}"
            except ImportError:
                return f"📧 Email template '{template_type}':\n\n{template}"
        except Exception as e:
            return f"Email template failed: {e}"
    
    def _generate_ai_email(self, query):
        try:
            import re
            
            # Extract recipient name
            recipient = "there"
            name_patterns = [
                r'write email (?:to |with )?([a-zA-Z]+)',
                r'email (?:to |with )?([a-zA-Z]+)',
                r'compose email (?:to |with )?([a-zA-Z]+)'
            ]
            
            for pattern in name_patterns:
                match = re.search(pattern, query.lower())
                if match:
                    recipient = match.group(1).capitalize()
                    break
            
            # Use AI to generate email content
            try:
                from engine.dual_ai import dual_ai
                
                prompt = f"Write a professional email. User request: '{query}'. Recipient name: '{recipient}'. Include subject line and proper email format. Keep it concise and professional."
                
                if dual_ai.ai_provider == 'groq':
                    response = dual_ai.groq_client.chat.completions.create(
                        messages=[{"role": "user", "content": prompt}],
                        model="llama-3.1-8b-instant"
                    )
                    email_content = response.choices[0].message.content.strip()
                else:
                    response = dual_ai.gemini_model.generate_content(prompt)
                    email_content = response.text.strip()
                
                # Copy to clipboard
                try:
                    import pyperclip
                    pyperclip.copy(email_content)
                    return f"📧 AI-generated email copied to clipboard\n\n{email_content}"
                except ImportError:
                    return f"📧 AI-generated email:\n\n{email_content}"
                    
            except Exception as ai_error:
                # Fallback to simple template
                fallback_email = f"Subject: Message for {recipient}\n\nHi {recipient},\n\nI hope this email finds you well. I wanted to reach out regarding our recent discussion.\n\nPlease let me know if you have any questions or if there's anything I can help you with.\n\nBest regards,\n[Your Name]"
                
                try:
                    import pyperclip
                    pyperclip.copy(fallback_email)
                    return f"📧 Email generated (AI unavailable) copied to clipboard\n\n{fallback_email}"
                except ImportError:
                    return f"📧 Email generated (AI unavailable):\n\n{fallback_email}"
                    
        except Exception as e:
            return f"AI email generation failed: {e}"
    
    def meeting_scheduler(self, query=""):
        try:
            import webbrowser, re
            from datetime import datetime, timedelta
            
            # Extract duration from query
            duration = "1 hour"  # default
            duration_match = re.search(r'(\d+)\s*(hour|hours|minute|minutes)', query.lower())
            if duration_match:
                duration = f"{duration_match.group(1)} {duration_match.group(2)}"
            
            # Extract participants from query
            participants = "team"  # default
            if 'with' in query.lower():
                parts = query.lower().split('with')
                if len(parts) > 1:
                    participants = parts[1].strip()
            
            # Generate meeting details
            now = datetime.now()
            suggested_time = now + timedelta(days=1)
            meeting_link = "https://meet.google.com/new"
            
            meeting_details = f"""Meeting Scheduler
            
Suggested Time: {suggested_time.strftime('%Y-%m-%d %H:%M')}
Duration: {duration}
Participants: {participants}
Meeting Link: {meeting_link}
            
Calendar Integration:
- Google Calendar: https://calendar.google.com
- Outlook: https://outlook.live.com/calendar
            
Meeting opened in browser for scheduling."""
            
            # Open Google Meet in browser
            webbrowser.open(meeting_link)
            
            return meeting_details
        except Exception as e:
            return f"Meeting scheduler failed: {e}"
    
    def task_reminder(self, query=""):
        try:
            import re, json, os
            from datetime import datetime, timedelta
            
            # Create reminders file in current directory
            reminders_file = "reminders.json"
            
            # Extract task from query
            task = "Take a break"  # default
            if 'remind me to' in query.lower():
                task_match = re.search(r'remind me to (.+?)(?:\s+in|$)', query.lower())
                if task_match:
                    task = task_match.group(1).strip()
            elif 'reminder' in query.lower() and len(query.split()) > 2:
                words = query.split()
                if 'reminder' in [w.lower() for w in words]:
                    idx = [w.lower() for w in words].index('reminder')
                    if idx + 1 < len(words):
                        task = ' '.join(words[idx+1:]).strip()
            
            # Extract minutes from query
            minutes = 30  # default
            time_match = re.search(r'(\d+)\s*(minute|minutes|hour|hours)', query.lower())
            if time_match:
                num = int(time_match.group(1))
                unit = time_match.group(2)
                if 'hour' in unit:
                    minutes = num * 60
                else:
                    minutes = num
            
            if minutes <= 0 or minutes > 1440:
                minutes = 30
            
            # Calculate reminder time
            reminder_time = datetime.now() + timedelta(minutes=minutes)
            
            # Save reminder to JSON
            reminder_data = {
                "task": task,
                "reminder_time": reminder_time.isoformat(),
                "created_at": datetime.now().isoformat(),
                "minutes": minutes
            }
            
            # Load existing reminders
            reminders = []
            if os.path.exists(reminders_file):
                try:
                    with open(reminders_file, 'r') as f:
                        reminders = json.load(f)
                except:
                    reminders = []
            
            reminders.append(reminder_data)
            
            # Save updated reminders
            with open(reminders_file, 'w') as f:
                json.dump(reminders, f, indent=2)
            
            self._show_notification("Task Reminder Set", f"Will remind you to '{task}' in {minutes} minutes")
            
            def reminder():
                time.sleep(minutes * 60)
                self._show_notification("Task Reminder!", f"Time to: {task}")
                
                # Remove completed reminder
                try:
                    if os.path.exists(reminders_file):
                        with open(reminders_file, 'r') as f:
                            current_reminders = json.load(f)
                        updated_reminders = [r for r in current_reminders if r != reminder_data]
                        with open(reminders_file, 'w') as f:
                            json.dump(updated_reminders, f, indent=2)
                except:
                    pass
            
            threading.Thread(target=reminder, daemon=True).start()
            
            return f"Task reminder set: '{task}' at {reminder_time.strftime('%H:%M')} ({minutes} minutes)"
        except Exception as e:
            return f"Task reminder failed: {e}"
    
    def list_reminders(self, query=""):
        try:
            import json, os
            from datetime import datetime
            
            reminders_file = "reminders.json"
            
            if not os.path.exists(reminders_file):
                return "No reminders found. Create your first reminder!"
            
            with open(reminders_file, 'r') as f:
                reminders = json.load(f)
            
            if not reminders:
                return "No active reminders found."
            
            result = "Active Reminders:\n" + "="*30 + "\n"
            
            for i, reminder in enumerate(reminders, 1):
                task = reminder.get('task', 'Unknown task')
                reminder_time = datetime.fromisoformat(reminder.get('reminder_time', ''))
                created_at = datetime.fromisoformat(reminder.get('created_at', ''))
                
                now = datetime.now()
                if reminder_time > now:
                    time_left = reminder_time - now
                    minutes_left = int(time_left.total_seconds() / 60)
                    if minutes_left > 60:
                        hours = minutes_left // 60
                        mins = minutes_left % 60
                        time_str = f"{hours}h {mins}m remaining"
                    else:
                        time_str = f"{minutes_left}m remaining"
                    status = "ACTIVE"
                else:
                    time_str = "OVERDUE"
                    status = "OVERDUE"
                
                result += f"{i}. [{status}] {task}\n"
                result += f"   {time_str}\n"
                result += f"   Due: {reminder_time.strftime('%H:%M')}\n\n"
            
            result += f"Total: {len(reminders)} reminders"
            return result
        except Exception as e:
            return f"Failed to list reminders: {e}"
    
    def image_editor(self, query=""):
        try:
            try:
                from PIL import Image, ImageFilter, ImageEnhance
            except ImportError:
                return "Image library not installed. Run: pip install Pillow"
            
            import re
            
            # Extract file path from query
            file_match = re.search(r'(?:edit|image)\s+(.+?)(?:\s+(?:blur|sharp|bright|contrast|gray|resize)|$)', query.lower())
            if file_match:
                file_path = file_match.group(1).strip()
            else:
                return "Please specify image file: 'image editor filename.jpg blur'"
            
            if not os.path.exists(file_path):
                return f"Image file not found: {file_path}"
            
            img = Image.open(file_path)
            base_name = os.path.splitext(file_path)[0]
            
            # Apply filters based on query
            if 'blur' in query.lower():
                img = img.filter(ImageFilter.BLUR)
                output = f"{base_name}_blur.jpg"
            elif 'sharpen' in query.lower():
                img = img.filter(ImageFilter.SHARPEN)
                output = f"{base_name}_sharp.jpg"
            elif 'bright' in query.lower():
                enhancer = ImageEnhance.Brightness(img)
                img = enhancer.enhance(1.5)
                output = f"{base_name}_bright.jpg"
            elif 'contrast' in query.lower():
                enhancer = ImageEnhance.Contrast(img)
                img = enhancer.enhance(1.5)
                output = f"{base_name}_contrast.jpg"
            elif 'grayscale' in query.lower() or 'gray' in query.lower():
                img = img.convert('L')
                output = f"{base_name}_gray.jpg"
            elif 'resize' in query.lower():
                img = img.resize((800, 600))
                output = f"{base_name}_resized.jpg"
            else:
                # Default: apply multiple filters
                img = img.filter(ImageFilter.ENHANCE)
                output = f"{base_name}_enhanced.jpg"
            
            img.save(output)
            return f"🖼️ Image edited: {output}"
        except Exception as e:
            return f"Image editor failed: {e}"
    
    def audio_converter(self, query=""):
        try:
            try:
                from pydub import AudioSegment
            except ImportError:
                return "Audio library not installed. Run: pip install pydub"
            
            import re
            
            # Extract file path from query
            file_match = re.search(r'(?:convert|audio)\s+(.+?)(?:\s+(?:to|mp3|wav|flac|aac|ogg)|$)', query.lower())
            if file_match:
                file_path = file_match.group(1).strip()
            else:
                return "Please specify audio file: 'audio converter song.mp3 to wav'"
            
            if not os.path.exists(file_path):
                return f"Audio file not found: {file_path}"
            
            # Detect input format
            input_ext = os.path.splitext(file_path)[1].lower()
            base_name = os.path.splitext(file_path)[0]
            
            # Determine output format from query
            if 'mp3' in query.lower():
                output_format = 'mp3'
            elif 'wav' in query.lower():
                output_format = 'wav'
            elif 'flac' in query.lower():
                output_format = 'flac'
            elif 'aac' in query.lower():
                output_format = 'aac'
            elif 'ogg' in query.lower():
                output_format = 'ogg'
            else:
                output_format = 'mp3'  # default
            
            # Load and convert audio
            audio = AudioSegment.from_file(file_path)
            output_path = f"{base_name}.{output_format}"
            
            # Export with format-specific settings
            if output_format == 'mp3':
                audio.export(output_path, format="mp3", bitrate="192k")
            elif output_format == 'wav':
                audio.export(output_path, format="wav")
            elif output_format == 'flac':
                audio.export(output_path, format="flac")
            else:
                audio.export(output_path, format=output_format)
            
            return f"🎵 Audio converted to {output_format.upper()}: {output_path}"
        except Exception as e:
            return f"Audio converter failed: {e}"
    
    def video_downloader(self, query=""):
        try:
            try:
                import yt_dlp
            except ImportError:
                return "Video downloader not installed. Run: pip install yt-dlp"
            
            import re
            
            # Extract URL from query
            url_pattern = r'https?://[^\s]+'
            url_match = re.search(url_pattern, query)
            
            if not url_match:
                return "Please provide video URL: 'video downloader https://youtube.com/watch?v=...'"
            
            url = url_match.group()
            
            # Configure download options
            ydl_opts = {
                'format': 'best[height<=720]',  # Max 720p for faster download
                'outtmpl': '%(title)s.%(ext)s',
                'noplaylist': True,
            }
            
            # Determine quality from query
            if 'audio' in query.lower() or 'mp3' in query.lower():
                ydl_opts['format'] = 'bestaudio/best'
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            elif '1080' in query.lower():
                ydl_opts['format'] = 'best[height<=1080]'
            elif '480' in query.lower():
                ydl_opts['format'] = 'best[height<=480]'
            
            # Download video
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                title = info.get('title', 'Unknown')
                
                ydl.download([url])
                
            return f"📹 Downloaded: {title[:50]}..."
        except Exception as e:
            return f"Video download failed: {e}"
    
    def voice_recorder(self, query=""):
        try:
            import pyaudio
            import wave
            import threading
            import time
            from datetime import datetime
            
            # Extract duration from query (default 30 seconds)
            duration = 30
            import re
            duration_match = re.search(r'(\d+)\s*(second|seconds|minute|minutes)', query.lower())
            if duration_match:
                num = int(duration_match.group(1))
                unit = duration_match.group(2)
                if 'minute' in unit:
                    duration = num * 60
                else:
                    duration = num
            
            # Generate filename
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"voice_memo_{timestamp}.wav"
            
            # Immediate response with voice feedback
            response_msg = f"Starting voice recording for {duration} seconds"
            
            def record_audio():
                try:
                    print(f"🎤 Recording audio for {duration} seconds...")
                    
                    # Audio settings
                    CHUNK = 1024
                    FORMAT = pyaudio.paInt16
                    CHANNELS = 1
                    RATE = 44100
                    
                    # Initialize PyAudio
                    p = pyaudio.PyAudio()
                    
                    # Start recording
                    stream = p.open(format=FORMAT,
                                  channels=CHANNELS,
                                  rate=RATE,
                                  input=True,
                                  frames_per_buffer=CHUNK)
                    
                    frames = []
                    
                    # Record audio
                    for i in range(0, int(RATE / CHUNK * duration)):
                        data = stream.read(CHUNK)
                        frames.append(data)
                    
                    # Stop recording
                    stream.stop_stream()
                    stream.close()
                    p.terminate()
                    
                    # Save audio file
                    wf = wave.open(filename, 'wb')
                    wf.setnchannels(CHANNELS)
                    wf.setsampwidth(p.get_sample_size(FORMAT))
                    wf.setframerate(RATE)
                    wf.writeframes(b''.join(frames))
                    wf.close()
                    
                    print(f"🎤 Voice recording saved: {filename}")
                    
                    # Optional: Convert to text using speech recognition
                    if 'text' in query.lower() or 'transcribe' in query.lower():
                        try:
                            print("📝 Converting speech to text...")
                            import speech_recognition as sr
                            r = sr.Recognizer()
                            with sr.AudioFile(filename) as source:
                                audio = r.record(source)
                            text = r.recognize_google(audio)
                            
                            # Save transcription
                            text_filename = f"transcription_{timestamp}.txt"
                            with open(text_filename, 'w', encoding='utf-8') as f:
                                f.write(text)
                            
                            print(f"📝 Transcription saved: {text_filename}")
                            print(f"Text: {text[:100]}..." if len(text) > 100 else f"Text: {text}")
                        except Exception as e:
                            print(f"📝 Transcription failed: {e}")
                        
                except Exception as e:
                    print(f"🎤 Recording failed: {e}")
            
            # Start recording in background thread
            threading.Thread(target=record_audio, daemon=True).start()
            
            return response_msg
            
        except ImportError:
            return "Audio library not installed. Run: pip install pyaudio wave"
        except Exception as e:
            return f"Voice recording failed: {e}"
    
    def screen_recorder(self, query=""):
        try:
            import cv2
            import numpy as np
            import pyautogui
            import threading
            import time
            from datetime import datetime
            
            # Extract duration from query (default 30 seconds)
            duration = 30
            import re
            duration_match = re.search(r'(\d+)\s*(second|seconds|minute|minutes)', query.lower())
            if duration_match:
                num = int(duration_match.group(1))
                unit = duration_match.group(2)
                if 'minute' in unit:
                    duration = num * 60
                else:
                    duration = num
            
            # Generate filename
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"screen_recording_{timestamp}.mp4"
            
            # Immediate response with voice feedback
            response_msg = f"Starting screen recording for {duration} seconds"
            
            def record_screen():
                try:
                    print(f"📹 Recording screen for {duration} seconds...")
                    
                    # Get screen dimensions
                    screen_size = pyautogui.size()
                    
                    # Define codec and create VideoWriter
                    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
                    fps = 20.0
                    out = cv2.VideoWriter(filename, fourcc, fps, screen_size)
                    
                    # Record screen
                    start_time = datetime.now()
                    frames_recorded = 0
                    
                    while (datetime.now() - start_time).seconds < duration:
                        # Capture screenshot
                        img = pyautogui.screenshot()
                        
                        # Convert PIL image to OpenCV format
                        frame = np.array(img)
                        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                        
                        # Write frame to video
                        out.write(frame)
                        frames_recorded += 1
                        
                        # Control frame rate
                        time.sleep(1/fps)
                    
                    # Release everything
                    out.release()
                    cv2.destroyAllWindows()
                    
                    print(f"📹 Screen recording saved: {filename} ({frames_recorded} frames)")
                    
                except Exception as e:
                    print(f"📹 Recording failed: {e}")
            
            # Start recording in background thread
            threading.Thread(target=record_screen, daemon=True).start()
            
            return response_msg
            
        except ImportError:
            return "Screen recording libraries not installed. Run: pip install opencv-python pyautogui"
        except Exception as e:
            return f"Screen recording failed: {e}"
    
    def _load_health_data(self):
        """Load health data from JSON file"""
        default_data = {
            'water_intake': {'daily_goal': 8, 'today': 0, 'last_reminder': None, 'history': []},
            'exercise': {'sessions': [], 'weekly_goal': 5, 'current_week': 0},
            'calories': {'daily_goal': 2000, 'today': 0, 'foods': [], 'history': []},
            'sleep': {'bedtime': '22:00', 'wake_time': '06:00', 'reminders': True, 'history': []},
            'stress': {'levels': [], 'last_check': None, 'weekly_average': 0},
            'mood': {'entries': [], 'weekly_average': 0, 'last_check': None},
            'heart_rate': {'readings': [], 'resting_hr': 70, 'last_check': None},
            'medications': {'pills': [], 'reminders': []},
            'bmi': {'height': 170, 'weight': 70, 'history': []}
        }
        
        try:
            import json
            if os.path.exists('health_data.json'):
                with open('health_data.json', 'r') as f:
                    loaded_data = json.load(f)
                    # Merge with defaults to ensure all keys exist
                    for key, value in default_data.items():
                        if key not in loaded_data:
                            loaded_data[key] = value
                    return loaded_data
        except:
            pass
        
        return default_data
    
    def _save_health_data(self, data):
        """Save health data to JSON file"""
        try:
            import json
            with open('health_data.json', 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Failed to save health data: {e}")
    
    def water_reminder(self, query=""):
        try:
            import json, re
            from datetime import datetime, timedelta
            
            data = self._load_health_data()
            water_data = data['water_intake']
            
            # Check if user wants to log water intake
            if any(word in query.lower() for word in ['drink', 'drank', 'add', 'had']):
                try:
                    # Use AI to extract water amount and type
                    from engine.dual_ai import dual_ai
                    
                    ai_prompt = f'''Extract water/drink information from: "{query}"
                    
Respond ONLY in this format:
Drink: [drink type]
Amount: [number in ml]
                    
Examples:
Drink: water
Amount: 500

Drink: coffee
Amount: 250

Drink: juice
Amount: 300
                    
Convert glasses/cups to ml (1 glass = 250ml, 1 cup = 240ml, 1 liter = 1000ml).'''
                    
                    if dual_ai.ai_provider == 'groq':
                        response = dual_ai.groq_client.chat.completions.create(
                            messages=[{"role": "user", "content": ai_prompt}],
                            model="llama-3.1-8b-instant"
                        )
                        ai_response = response.choices[0].message.content.strip()
                    else:
                        response = dual_ai.gemini_model.generate_content(ai_prompt)
                        ai_response = response.text.strip()
                    
                    # Parse AI response
                    drink_match = re.search(r'Drink:\s*(.+)', ai_response, re.IGNORECASE)
                    amount_match = re.search(r'Amount:\s*(\d+)', ai_response, re.IGNORECASE)
                    
                    if drink_match and amount_match:
                        drink_type = drink_match.group(1).strip().lower()
                        amount = int(amount_match.group(1))
                        
                        # AI hydration analysis
                        hydration_value = amount if drink_type in ['water', 'herbal tea'] else amount * 0.7
                        
                        water_data['today'] += hydration_value
                        water_data['history'].append({
                            'timestamp': datetime.now().isoformat(),
                            'amount': hydration_value,
                            'drink_type': drink_type,
                            'original_amount': amount
                        })
                        
                        glasses_today = water_data['today'] / 250
                        remaining = max(0, water_data['daily_goal'] - glasses_today)
                        
                        self._save_health_data(data)
                        
                        # AI health tip
                        if drink_type not in ['water', 'herbal tea']:
                            tip = f" (Note: {drink_type} provides less hydration than pure water)"
                        else:
                            tip = " (Excellent hydration choice!)"
                        
                        self._show_notification("💧 Hydration Logged", f"{drink_type.title()}: {amount}ml. Hydration: {hydration_value:.0f}ml")
                        
                        return f"💧 Added {amount}ml {drink_type} (hydration value: {hydration_value:.0f}ml). Today: {glasses_today:.1f}/{water_data['daily_goal']} glasses. Remaining: {remaining:.1f}{tip}"
                    
                except Exception:
                    # Fallback to basic parsing
                    amount_match = re.search(r'(\d+)\s*(ml|glass|glasses|cup|cups|liter|liters)', query.lower())
                    if amount_match:
                        amount = int(amount_match.group(1))
                        unit = amount_match.group(2)
                        if 'glass' in unit or 'cup' in unit:
                            amount *= 250
                        elif 'liter' in unit:
                            amount *= 1000
                    else:
                        amount = 250
                    
                    water_data['today'] += amount
                    water_data['history'].append({
                        'timestamp': datetime.now().isoformat(),
                        'amount': amount
                    })
                    
                    glasses_today = water_data['today'] / 250
                    remaining = max(0, water_data['daily_goal'] - glasses_today)
                    
                    self._save_health_data(data)
                    self._show_notification("💧 Water Logged", f"Added {amount}ml. Today: {glasses_today:.1f}/{water_data['daily_goal']} glasses")
                    
                    return f"💧 Water logged: {amount}ml. Today: {glasses_today:.1f}/{water_data['daily_goal']} glasses. Remaining: {remaining:.1f} glasses"
            
            # Set up hourly reminders
            elif 'start' in query.lower() or 'enable' in query.lower():
                def hourly_reminder():
                    while True:
                        time.sleep(3600)  # 1 hour
                        current_data = self._load_health_data()
                        glasses_today = current_data['water_intake']['today'] / 250
                        goal = current_data['water_intake']['daily_goal']
                        
                        if glasses_today < goal:
                            remaining = goal - glasses_today
                            self._show_notification("💧 Hydration Reminder", f"Time to drink water! {remaining:.1f} glasses remaining today")
                
                threading.Thread(target=hourly_reminder, daemon=True).start()
                return "💧 Hourly water reminders started. Stay hydrated!"
            
            # Show current status
            else:
                glasses_today = water_data['today'] / 250
                remaining = max(0, water_data['daily_goal'] - glasses_today)
                
                status = f"💧 Water Intake Today: {glasses_today:.1f}/{water_data['daily_goal']} glasses\n"
                status += f"Remaining: {remaining:.1f} glasses ({remaining * 250:.0f}ml)\n"
                
                if water_data['history']:
                    last_drink = water_data['history'][-1]
                    last_time = datetime.fromisoformat(last_drink['timestamp'])
                    time_ago = datetime.now() - last_time
                    hours_ago = time_ago.total_seconds() / 3600
                    status += f"Last drink: {hours_ago:.1f} hours ago"
                
                return status
                
        except Exception as e:
            return f"Water reminder failed: {e}"
    
    def exercise_timer(self, query=""):
        try:
            import re
            from datetime import datetime, timedelta
            
            data = self._load_health_data()
            exercise_data = data['exercise']
            
            try:
                # Use AI to create personalized workout
                from engine.dual_ai import dual_ai
                
                ai_prompt = f'''Create a workout plan from: "{query}"
                
Respond ONLY in this format:
Workout: [workout type]
Rounds: [number]
Work: [seconds]
Rest: [seconds]
Intensity: [Low/Medium/High]
                
Examples:
Workout: HIIT
Rounds: 5
Work: 30
Rest: 10
Intensity: High

Workout: Cardio
Rounds: 3
Work: 60
Rest: 30
Intensity: Medium
                
Adjust based on user request or use defaults for HIIT.'''
                
                if dual_ai.ai_provider == 'groq':
                    response = dual_ai.groq_client.chat.completions.create(
                        messages=[{"role": "user", "content": ai_prompt}],
                        model="llama-3.1-8b-instant"
                    )
                    ai_response = response.choices[0].message.content.strip()
                else:
                    response = dual_ai.gemini_model.generate_content(ai_prompt)
                    ai_response = response.text.strip()
                
                # Parse AI response
                workout_match = re.search(r'Workout:\s*(.+)', ai_response, re.IGNORECASE)
                rounds_match = re.search(r'Rounds:\s*(\d+)', ai_response, re.IGNORECASE)
                work_match = re.search(r'Work:\s*(\d+)', ai_response, re.IGNORECASE)
                rest_match = re.search(r'Rest:\s*(\d+)', ai_response, re.IGNORECASE)
                intensity_match = re.search(r'Intensity:\s*(.+)', ai_response, re.IGNORECASE)
                
                if all([workout_match, rounds_match, work_match, rest_match]):
                    workout_type = workout_match.group(1).strip()
                    rounds = int(rounds_match.group(1))
                    work_time = int(work_match.group(1))
                    rest_time = int(rest_match.group(1))
                    intensity = intensity_match.group(1).strip() if intensity_match else "Medium"
                else:
                    raise Exception("AI parsing failed")
                    
            except Exception:
                # Fallback to basic parsing
                work_time = 30
                rest_time = 10
                rounds = 5
                workout_type = "HIIT"
                intensity = "Medium"
                
                work_match = re.search(r'work\s+(\d+)\s*(second|seconds|minute|minutes)', query.lower())
                if work_match:
                    work_time = int(work_match.group(1))
                    if 'minute' in work_match.group(2):
                        work_time *= 60
                
                rest_match = re.search(r'rest\s+(\d+)\s*(second|seconds|minute|minutes)', query.lower())
                if rest_match:
                    rest_time = int(rest_match.group(1))
                    if 'minute' in rest_match.group(2):
                        rest_time *= 60
                
                rounds_match = re.search(r'(\d+)\s*rounds?', query.lower())
                if rounds_match:
                    rounds = int(rounds_match.group(1))
            
            # AI-enhanced workout response
            response_msg = f"Starting {workout_type}: {rounds} rounds, {work_time}s work, {rest_time}s rest ({intensity} intensity)"
            
            def hiit_timer():
                try:
                    print(f"🏃 Starting HIIT workout: {rounds} rounds")
                    
                    for round_num in range(1, rounds + 1):
                        # Work phase
                        self._show_notification(f"🏃 Round {round_num}/{rounds}", f"WORK! {work_time} seconds")
                        print(f"🏃 Round {round_num}/{rounds} - WORK! {work_time}s")
                        time.sleep(work_time)
                        
                        # Rest phase (except last round)
                        if round_num < rounds:
                            self._show_notification(f"😴 Rest Time", f"Rest for {rest_time} seconds")
                            print(f"😴 Rest for {rest_time}s")
                            time.sleep(rest_time)
                    
                    # Workout complete
                    total_time = rounds * work_time + (rounds - 1) * rest_time
                    
                    # Log workout
                    exercise_data['sessions'].append({
                        'timestamp': datetime.now().isoformat(),
                        'type': 'HIIT',
                        'duration': total_time,
                        'rounds': rounds,
                        'work_time': work_time,
                        'rest_time': rest_time
                    })
                    exercise_data['current_week'] += 1
                    
                    self._save_health_data(data)
                    
                    self._show_notification("🎉 Workout Complete!", f"Great job! {total_time//60}min {total_time%60}s workout finished")
                    print(f"🎉 Workout complete! Total time: {total_time//60}min {total_time%60}s")
                    
                except Exception as e:
                    print(f"🏃 Exercise timer failed: {e}")
            
            threading.Thread(target=hiit_timer, daemon=True).start()
            return response_msg
            
        except Exception as e:
            return f"Exercise timer failed: {e}"
    
    def calorie_calculator(self, query=""):
        try:
            import re
            from datetime import datetime
            
            data = self._load_health_data()
            calorie_data = data['calories']
            
            # Add food using AI
            if any(word in query.lower() for word in ['add', 'ate', 'eat', 'drink', 'had']):
                try:
                    # Use AI to extract food and estimate calories
                    from engine.dual_ai import dual_ai
                    
                    ai_prompt = f'''Extract food information from: "{query}"
                    
Respond ONLY in this exact format (no extra text):
Food: [food name]
Quantity: [number]
Calories: [estimated calories per serving]
                    
Examples:
Food: banana
Quantity: 2
Calories: 105

Food: sushi roll
Quantity: 1
Calories: 200

Food: chocolate cookie
Quantity: 3
Calories: 120
                    
Estimate realistic calories per serving. Always include all three lines.'''
                    
                    if dual_ai.ai_provider == 'groq':
                        response = dual_ai.groq_client.chat.completions.create(
                            messages=[{"role": "user", "content": ai_prompt}],
                            model="llama-3.1-8b-instant"
                        )
                        ai_response = response.choices[0].message.content.strip()
                    else:
                        response = dual_ai.gemini_model.generate_content(ai_prompt)
                        ai_response = response.text.strip()
                    
                    # Parse AI response
                    food_match = re.search(r'Food:\s*(.+)', ai_response, re.IGNORECASE)
                    qty_match = re.search(r'Quantity:\s*(\d+)', ai_response, re.IGNORECASE)
                    cal_match = re.search(r'Calories:\s*(\d+)', ai_response, re.IGNORECASE)
                    
                    if food_match and cal_match:
                        food_name = food_match.group(1).strip().lower()
                        quantity = int(qty_match.group(1)) if qty_match else 1
                        calories_per_serving = int(cal_match.group(1))
                        
                        total_calories = calories_per_serving * quantity
                        calorie_data['today'] += total_calories
                        
                        calorie_data['foods'].append({
                            'timestamp': datetime.now().isoformat(),
                            'food': food_name,
                            'quantity': quantity,
                            'calories': total_calories
                        })
                        
                        remaining = max(0, calorie_data['daily_goal'] - calorie_data['today'])
                        
                        self._save_health_data(data)
                        self._show_notification("🍎 Food Logged", f"{food_name.title()}: {total_calories} cal. Today: {calorie_data['today']}/{calorie_data['daily_goal']}")
                        
                        return f"🍎 Added {quantity}x {food_name}: {total_calories} calories. Today: {calorie_data['today']}/{calorie_data['daily_goal']}. Remaining: {remaining}"
                    else:
                        return "🍎 Could not identify food from your message. Try: 'ate 2 apples' or 'add pizza'"
                        
                except Exception as ai_error:
                    # Fallback to basic food database
                    food_db = {
                        'apple': 95, 'banana': 105, 'orange': 62, 'bread': 80, 'rice': 130,
                        'chicken': 165, 'beef': 250, 'fish': 140, 'egg': 70, 'milk': 150,
                        'pizza': 285, 'burger': 540, 'pasta': 220, 'salad': 50, 'yogurt': 100,
                        'coffee': 5, 'tea': 2, 'soda': 140, 'water': 0, 'juice': 110
                    }
                    
                    for food, calories_per_serving in food_db.items():
                        if food in query.lower():
                            qty_match = re.search(f'(\d+)\s*{food}', query.lower())
                            quantity = int(qty_match.group(1)) if qty_match else 1
                            
                            total_calories = calories_per_serving * quantity
                            calorie_data['today'] += total_calories
                            
                            calorie_data['foods'].append({
                                'timestamp': datetime.now().isoformat(),
                                'food': food,
                                'quantity': quantity,
                                'calories': total_calories
                            })
                            
                            remaining = max(0, calorie_data['daily_goal'] - calorie_data['today'])
                            
                            self._save_health_data(data)
                            self._show_notification("🍎 Food Logged", f"{food.title()}: {total_calories} cal. Today: {calorie_data['today']}/{calorie_data['daily_goal']}")
                            
                            return f"🍎 Added {quantity}x {food}: {total_calories} calories. Today: {calorie_data['today']}/{calorie_data['daily_goal']}. Remaining: {remaining}"
                    
                    return "🍎 Food not recognized. Try: 'ate sandwich' or 'add 2 cookies'"
            
            # Show status
            else:
                remaining = max(0, calorie_data['daily_goal'] - calorie_data['today'])
                over = max(0, calorie_data['today'] - calorie_data['daily_goal'])
                
                status = f"🍎 Calories Today: {calorie_data['today']}/{calorie_data['daily_goal']}\n"
                
                if over > 0:
                    status += f"Over goal by: {over} calories\n"
                else:
                    status += f"Remaining: {remaining} calories\n"
                
                if calorie_data['foods']:
                    status += "\nToday's meals:\n"
                    for food in calorie_data['foods'][-5:]:  # Last 5 items
                        time_str = datetime.fromisoformat(food['timestamp']).strftime('%H:%M')
                        status += f"- {time_str}: {food['quantity']}x {food['food']} ({food['calories']} cal)\n"
                
                return status
                
        except Exception as e:
            return f"Calorie calculator failed: {e}"
    
    def sleep_tracker(self, query=""):
        try:
            import re
            from datetime import datetime, timedelta, time
            
            data = self._load_health_data()
            sleep_data = data['sleep']
            
            # AI-powered sleep optimization
            if 'bedtime' in query.lower() or 'set' in query.lower():
                try:
                    # Use AI to optimize sleep schedule
                    from engine.dual_ai import dual_ai
                    
                    ai_prompt = f'''Optimize sleep schedule from: "{query}"
                    
Respond ONLY in this format:
Bedtime: [HH:MM in 24h format]
Wake: [HH:MM in 24h format]
Optimal: [Yes/No]
Advice: [sleep optimization tip]
                    
Examples:
Bedtime: 22:30
Wake: 06:30
Optimal: Yes
Advice: Perfect 8-hour sleep cycle

Bedtime: 01:00
Wake: 07:00
Optimal: No
Advice: Try sleeping earlier for better recovery
                    
Recommend 7-9 hours of sleep for optimal health.'''
                    
                    if dual_ai.ai_provider == 'groq':
                        response = dual_ai.groq_client.chat.completions.create(
                            messages=[{"role": "user", "content": ai_prompt}],
                            model="llama-3.1-8b-instant"
                        )
                        ai_response = response.choices[0].message.content.strip()
                    else:
                        response = dual_ai.gemini_model.generate_content(ai_response)
                        ai_response = response.text.strip()
                    
                    # Parse AI response
                    bedtime_match = re.search(r'Bedtime:\s*(\d{1,2}:\d{2})', ai_response, re.IGNORECASE)
                    wake_match = re.search(r'Wake:\s*(\d{1,2}:\d{2})', ai_response, re.IGNORECASE)
                    optimal_match = re.search(r'Optimal:\s*(Yes|No)', ai_response, re.IGNORECASE)
                    advice_match = re.search(r'Advice:\s*(.+)', ai_response, re.IGNORECASE)
                    
                    if bedtime_match:
                        sleep_data['bedtime'] = bedtime_match.group(1)
                        if wake_match:
                            sleep_data['wake_time'] = wake_match.group(1)
                        
                        optimal = optimal_match.group(1) if optimal_match else "Unknown"
                        advice = advice_match.group(1) if advice_match else "Maintain consistent sleep schedule"
                        
                        sleep_data['ai_advice'] = advice
                        self._save_health_data(data)
                        
                        return f"😴 AI-optimized schedule set\nBedtime: {sleep_data['bedtime']}\nWake: {sleep_data['wake_time']}\nOptimal: {optimal}\nAI Advice: {advice}"
                        
                except Exception:
                    # Fallback to basic parsing
                    time_match = re.search(r'(\d{1,2}):?(\d{2})?\s*(pm|am)?', query.lower())
                    if time_match:
                        hour = int(time_match.group(1))
                        minute = int(time_match.group(2)) if time_match.group(2) else 0
                        period = time_match.group(3)
                        
                        if period == 'pm' and hour != 12:
                            hour += 12
                        elif period == 'am' and hour == 12:
                            hour = 0
                        
                        sleep_data['bedtime'] = f"{hour:02d}:{minute:02d}"
                        self._save_health_data(data)
                        
                        return f"😴 Bedtime set to {sleep_data['bedtime']}. Sleep reminders enabled."
            
            # Set wake time
            elif 'wake' in query.lower():
                time_match = re.search(r'(\d{1,2}):?(\d{2})?\s*(pm|am)?', query.lower())
                if time_match:
                    hour = int(time_match.group(1))
                    minute = int(time_match.group(2)) if time_match.group(2) else 0
                    period = time_match.group(3)
                    
                    if period == 'pm' and hour != 12:
                        hour += 12
                    elif period == 'am' and hour == 12:
                        hour = 0
                    
                    sleep_data['wake_time'] = f"{hour:02d}:{minute:02d}"
                    self._save_health_data(data)
                    
                    return f"⏰ Wake time set to {sleep_data['wake_time']}"
            
            # Start sleep reminders
            elif 'start' in query.lower() or 'enable' in query.lower():
                def sleep_reminder():
                    while True:
                        try:
                            current_data = self._load_health_data()
                            bedtime_str = current_data['sleep']['bedtime']
                            bedtime_hour, bedtime_min = map(int, bedtime_str.split(':'))
                            
                            now = datetime.now()
                            bedtime_today = now.replace(hour=bedtime_hour, minute=bedtime_min, second=0, microsecond=0)
                            
                            # If bedtime has passed today, set for tomorrow
                            if now > bedtime_today:
                                bedtime_today += timedelta(days=1)
                            
                            # Calculate time until bedtime
                            time_until = bedtime_today - now
                            
                            # Remind 30 minutes before bedtime
                            if time_until.total_seconds() <= 1800:  # 30 minutes
                                self._show_notification("😴 Bedtime Soon", f"Bedtime in {int(time_until.total_seconds()//60)} minutes. Start winding down!")
                                time.sleep(1800)  # Wait 30 minutes before next check
                            else:
                                time.sleep(900)  # Check every 15 minutes
                                
                        except Exception as e:
                            time.sleep(3600)  # Wait 1 hour on error
                
                threading.Thread(target=sleep_reminder, daemon=True).start()
                return f"😴 Sleep reminders started. Bedtime: {sleep_data['bedtime']}, Wake: {sleep_data['wake_time']}"
            
            # Show sleep schedule
            else:
                bedtime_hour, bedtime_min = map(int, sleep_data['bedtime'].split(':'))
                wake_hour, wake_min = map(int, sleep_data['wake_time'].split(':'))
                
                # Calculate sleep duration
                bedtime_minutes = bedtime_hour * 60 + bedtime_min
                wake_minutes = wake_hour * 60 + wake_min
                
                if wake_minutes < bedtime_minutes:
                    wake_minutes += 24 * 60  # Next day
                
                sleep_duration = (wake_minutes - bedtime_minutes) / 60
                
                status = f"😴 Sleep Schedule:\n"
                status += f"Bedtime: {sleep_data['bedtime']}\n"
                status += f"Wake time: {sleep_data['wake_time']}\n"
                status += f"Sleep duration: {sleep_duration:.1f} hours\n"
                
                if sleep_duration < 7:
                    status += "⚠️ Consider getting more sleep (7-9 hours recommended)"
                elif sleep_duration > 9:
                    status += "⚠️ You might be sleeping too much (7-9 hours recommended)"
                else:
                    status += "✅ Good sleep duration!"
                
                return status
                
        except Exception as e:
            return f"Sleep tracker failed: {e}"
    
    def stress_meter(self, query=""):
        try:
            import re
            from datetime import datetime, timedelta
            
            data = self._load_health_data()
            stress_data = data['stress']
            
            # AI-powered stress analysis
            if any(word in query.lower() for word in ['level', 'feel', 'stressed', 'rate', 'anxious', 'overwhelmed']):
                try:
                    # Use AI to analyze stress from description
                    from engine.dual_ai import dual_ai
                    
                    ai_prompt = f'''Analyze stress level from: "{query}"
                    
Respond ONLY in this format:
Stress: [1-10]
Cause: [main stress cause]
Recommendation: [specific advice]
                    
Examples:
Stress: 7
Cause: work pressure
Recommendation: Take 5-minute breathing break

Stress: 3
Cause: mild fatigue
Recommendation: Stay hydrated and rest
                    
Rate 1-10 where 1=very calm, 10=extremely stressed.'''
                    
                    if dual_ai.ai_provider == 'groq':
                        response = dual_ai.groq_client.chat.completions.create(
                            messages=[{"role": "user", "content": ai_prompt}],
                            model="llama-3.1-8b-instant"
                        )
                        ai_response = response.choices[0].message.content.strip()
                    else:
                        response = dual_ai.gemini_model.generate_content(ai_prompt)
                        ai_response = response.text.strip()
                    
                    # Parse AI response
                    stress_match = re.search(r'Stress:\s*(\d+)', ai_response, re.IGNORECASE)
                    cause_match = re.search(r'Cause:\s*(.+)', ai_response, re.IGNORECASE)
                    rec_match = re.search(r'Recommendation:\s*(.+)', ai_response, re.IGNORECASE)
                    
                    if stress_match:
                        stress_level = int(stress_match.group(1))
                        cause = cause_match.group(1).strip() if cause_match else "general stress"
                        ai_recommendation = rec_match.group(1).strip() if rec_match else "Take deep breaths"
                    else:
                        raise Exception("AI parsing failed")
                        
                except Exception:
                    # Fallback to manual input
                    level_match = re.search(r'(\d+)', query)
                    if level_match:
                        stress_level = int(level_match.group(1))
                        cause = "user reported"
                        ai_recommendation = "Basic stress management"
                    else:
                        return "🧘 Please describe your stress or rate it 1-10. Example: 'stress level 5' or 'feeling overwhelmed'"
                
                if 1 <= stress_level <= 10:
                    stress_data['levels'].append({
                        'timestamp': datetime.now().isoformat(),
                        'level': stress_level,
                        'cause': cause,
                        'ai_recommendation': ai_recommendation
                    })
                    
                    # AI-enhanced weekly analysis
                    week_ago = datetime.now() - timedelta(days=7)
                    recent_levels = [
                        entry['level'] for entry in stress_data['levels']
                        if datetime.fromisoformat(entry['timestamp']) > week_ago
                    ]
                    
                    if recent_levels:
                        stress_data['weekly_average'] = sum(recent_levels) / len(recent_levels)
                        
                        # AI trend analysis
                        if len(recent_levels) >= 3:
                            trend = "increasing" if recent_levels[-1] > recent_levels[-3] else "decreasing" if recent_levels[-1] < recent_levels[-3] else "stable"
                            trend_msg = f" (Trend: {trend})"
                        else:
                            trend_msg = ""
                    else:
                        trend_msg = ""
                    
                    stress_data['last_check'] = datetime.now().isoformat()
                    self._save_health_data(data)
                    
                    # AI-enhanced recommendations
                    if stress_level >= 8:
                        self._show_notification("🧘 High Stress Alert", f"Cause: {cause}. {ai_recommendation}")
                    elif stress_level >= 6:
                        self._show_notification("🧘 Stress Notice", f"Moderate stress from {cause}")
                    
                    return f"🧘 Stress logged: {stress_level}/10\nCause: {cause}\nWeekly average: {stress_data['weekly_average']:.1f}{trend_msg}\nAI Advice: {ai_recommendation}"
                else:
                    return "🧘 Please rate stress level 1-10 (1=very calm, 10=very stressed)"
            
            # Quick stress assessment
            elif 'check' in query.lower() or 'assess' in query.lower():
                questions = [
                    "Rate your current stress (1-10):",
                    "1 = Very calm and relaxed",
                    "5 = Moderate stress",
                    "10 = Extremely stressed"
                ]
                
                assessment = "🧘 Quick Stress Assessment:\n" + "\n".join(questions)
                assessment += "\n\nBreathing Exercise: Inhale 4 counts → Hold 4 → Exhale 4 → Repeat 5 times"
                
                return assessment
            
            # Show stress history
            else:
                if not stress_data['levels']:
                    return "🧘 No stress data yet. Try: 'stress level 5' to log your current stress."
                
                # Recent stress levels
                recent = stress_data['levels'][-7:]  # Last 7 entries
                
                status = f"🧘 Stress Overview:\n"
                status += f"Weekly average: {stress_data['weekly_average']:.1f}/10\n"
                
                if stress_data['last_check']:
                    last_time = datetime.fromisoformat(stress_data['last_check'])
                    hours_ago = (datetime.now() - last_time).total_seconds() / 3600
                    status += f"Last check: {hours_ago:.1f} hours ago\n"
                
                status += "\nRecent levels:\n"
                for entry in recent:
                    time_str = datetime.fromisoformat(entry['timestamp']).strftime('%m/%d %H:%M')
                    level = entry['level']
                    status += f"- {time_str}: {level}/10\n"
                
                # Stress management tips
                if stress_data['weekly_average'] >= 7:
                    status += "\n⚠️ High stress detected. Consider: meditation, exercise, or talking to someone."
                elif stress_data['weekly_average'] >= 5:
                    status += "\n💡 Moderate stress. Try: regular breaks, deep breathing, or light exercise."
                else:
                    status += "\n✅ Good stress management! Keep it up."
                
                return status
                
        except Exception as e:
            return f"Stress meter failed: {e}"
    
    def mood_tracker(self, query=""):
        try:
            import re
            from datetime import datetime, timedelta
            
            data = self._load_health_data()
            mood_data = data['mood']
            
            # AI-powered mood analysis
            if any(word in query.lower() for word in ['feel', 'mood', 'happy', 'sad', 'angry', 'anxious', 'excited', 'tired']):
                try:
                    from engine.dual_ai import dual_ai
                    
                    ai_prompt = f'''Analyze mood from: "{query}"
                    
Respond ONLY in this format:
Mood: [1-10]
Emotion: [primary emotion]
Trigger: [what caused this mood]
Suggestion: [mood improvement tip]
                    
Examples:
Mood: 8
Emotion: happy
Trigger: good news
Suggestion: Share your joy with others

Mood: 4
Emotion: stressed
Trigger: work pressure
Suggestion: Take a short walk
                    
Rate 1-10 where 1=very negative, 10=very positive.'''
                    
                    if dual_ai.ai_provider == 'groq':
                        response = dual_ai.groq_client.chat.completions.create(
                            messages=[{"role": "user", "content": ai_prompt}],
                            model="llama-3.1-8b-instant"
                        )
                        ai_response = response.choices[0].message.content.strip()
                    else:
                        response = dual_ai.gemini_model.generate_content(ai_prompt)
                        ai_response = response.text.strip()
                    
                    # Parse AI response
                    mood_match = re.search(r'Mood:\s*(\d+)', ai_response, re.IGNORECASE)
                    emotion_match = re.search(r'Emotion:\s*(.+)', ai_response, re.IGNORECASE)
                    trigger_match = re.search(r'Trigger:\s*(.+)', ai_response, re.IGNORECASE)
                    suggestion_match = re.search(r'Suggestion:\s*(.+)', ai_response, re.IGNORECASE)
                    
                    if mood_match:
                        mood_score = int(mood_match.group(1))
                        emotion = emotion_match.group(1).strip() if emotion_match else "neutral"
                        trigger = trigger_match.group(1).strip() if trigger_match else "general"
                        suggestion = suggestion_match.group(1).strip() if suggestion_match else "Stay positive"
                    else:
                        raise Exception("AI parsing failed")
                        
                except Exception:
                    # Fallback mood detection
                    positive_words = ['happy', 'great', 'good', 'excited', 'amazing', 'wonderful']
                    negative_words = ['sad', 'bad', 'angry', 'tired', 'stressed', 'awful']
                    
                    mood_score = 5  # neutral
                    emotion = "neutral"
                    
                    for word in positive_words:
                        if word in query.lower():
                            mood_score = 8
                            emotion = word
                            break
                    
                    for word in negative_words:
                        if word in query.lower():
                            mood_score = 3
                            emotion = word
                            break
                    
                    trigger = "user reported"
                    suggestion = "Practice mindfulness"
                
                if 1 <= mood_score <= 10:
                    mood_data['entries'].append({
                        'timestamp': datetime.now().isoformat(),
                        'score': mood_score,
                        'emotion': emotion,
                        'trigger': trigger,
                        'suggestion': suggestion
                    })
                    
                    # Calculate weekly average
                    week_ago = datetime.now() - timedelta(days=7)
                    recent_moods = [
                        entry['score'] for entry in mood_data['entries']
                        if datetime.fromisoformat(entry['timestamp']) > week_ago
                    ]
                    
                    if recent_moods:
                        mood_data['weekly_average'] = sum(recent_moods) / len(recent_moods)
                    
                    mood_data['last_check'] = datetime.now().isoformat()
                    self._save_health_data(data)
                    
                    # Mood-based notifications
                    if mood_score <= 3:
                        self._show_notification("Mood Alert", f"Low mood detected. {suggestion}")
                    elif mood_score >= 8:
                        self._show_notification("Great Mood!", f"You're feeling {emotion}! Keep it up!")
                    
                    return f"Mood logged: {mood_score}/10 ({emotion})\nTrigger: {trigger}\nWeekly average: {mood_data['weekly_average']:.1f}\nSuggestion: {suggestion}"
                else:
                    return "Please rate mood 1-10 or describe how you feel"
            
            # Show mood history
            else:
                if not mood_data['entries']:
                    return "No mood data yet. Try: 'feeling happy' or 'mood 7'"
                
                recent = mood_data['entries'][-7:]
                
                status = f"Mood Overview:\n"
                status += f"Weekly average: {mood_data['weekly_average']:.1f}/10\n"
                
                if mood_data['last_check']:
                    last_time = datetime.fromisoformat(mood_data['last_check'])
                    hours_ago = (datetime.now() - last_time).total_seconds() / 3600
                    status += f"Last check: {hours_ago:.1f} hours ago\n"
                
                status += "\nRecent moods:\n"
                for entry in recent:
                    time_str = datetime.fromisoformat(entry['timestamp']).strftime('%m/%d %H:%M')
                    score = entry['score']
                    emotion = entry['emotion']
                    status += f"- {time_str}: {score}/10 ({emotion})\n"
                
                return status
                
        except Exception as e:
            return f"Mood tracker failed: {e}"
    
    def heart_rate_monitor(self, query=""):
        try:
            import re
            from datetime import datetime, timedelta
            
            data = self._load_health_data()
            hr_data = data['heart_rate']
            
            # Log heart rate
            if any(word in query.lower() for word in ['bpm', 'rate', 'pulse', 'beat']):
                hr_match = re.search(r'(\d+)\s*(?:bpm|beats?)', query.lower())
                if hr_match:
                    heart_rate = int(hr_match.group(1))
                    
                    if 40 <= heart_rate <= 200:
                        hr_data['readings'].append({
                            'timestamp': datetime.now().isoformat(),
                            'bpm': heart_rate,
                            'type': 'manual'
                        })
                        
                        # Calculate resting HR average
                        recent_readings = hr_data['readings'][-10:]  # Last 10 readings
                        if len(recent_readings) >= 3:
                            avg_hr = sum(r['bpm'] for r in recent_readings) / len(recent_readings)
                            hr_data['resting_hr'] = int(avg_hr)
                        
                        hr_data['last_check'] = datetime.now().isoformat()
                        self._save_health_data(data)
                        
                        # Heart rate analysis
                        if heart_rate > 100:
                            status = "High (may indicate stress or activity)"
                            self._show_notification("High Heart Rate", f"{heart_rate} BPM detected")
                        elif heart_rate < 60:
                            status = "Low (athletic or resting)"
                        else:
                            status = "Normal range"
                        
                        return f"Heart rate logged: {heart_rate} BPM\nStatus: {status}\nResting HR: {hr_data['resting_hr']} BPM"
                    else:
                        return "Please enter valid heart rate (40-200 BPM)"
                else:
                    return "Please specify heart rate: 'heart rate 75 bpm'"
            
            # Show heart rate history
            else:
                if not hr_data['readings']:
                    return "No heart rate data yet. Try: 'heart rate 72 bpm'"
                
                recent = hr_data['readings'][-7:]
                
                status = f"Heart Rate Monitor:\n"
                status += f"Resting HR: {hr_data['resting_hr']} BPM\n"
                
                if hr_data['last_check']:
                    last_time = datetime.fromisoformat(hr_data['last_check'])
                    hours_ago = (datetime.now() - last_time).total_seconds() / 3600
                    status += f"Last reading: {hours_ago:.1f} hours ago\n"
                
                status += "\nRecent readings:\n"
                for reading in recent:
                    time_str = datetime.fromisoformat(reading['timestamp']).strftime('%m/%d %H:%M')
                    bpm = reading['bpm']
                    status += f"- {time_str}: {bpm} BPM\n"
                
                return status
                
        except Exception as e:
            return f"Heart rate monitor failed: {e}"
    
    def medication_reminder(self, query=""):
        try:
            import re, json
            from datetime import datetime, timedelta
            
            data = self._load_health_data()
            med_data = data['medications']
            
            # Add medication
            if 'add' in query.lower() or 'take' in query.lower():
                # Extract medication name and schedule
                med_match = re.search(r'(?:add|take)\s+(.+?)(?:\s+(?:every|at|daily)|$)', query.lower())
                if med_match:
                    med_name = med_match.group(1).strip()
                    
                    # Extract schedule
                    schedule = "daily"
                    time_match = re.search(r'(?:at|every)\s+(\d{1,2}):?(\d{2})?\s*(am|pm)?', query.lower())
                    if time_match:
                        hour = int(time_match.group(1))
                        minute = int(time_match.group(2)) if time_match.group(2) else 0
                        period = time_match.group(3)
                        
                        if period == 'pm' and hour != 12:
                            hour += 12
                        elif period == 'am' and hour == 12:
                            hour = 0
                        
                        schedule = f"{hour:02d}:{minute:02d}"
                    
                    medication = {
                        'name': med_name,
                        'schedule': schedule,
                        'added': datetime.now().isoformat(),
                        'last_taken': None
                    }
                    
                    med_data['pills'].append(medication)
                    self._save_health_data(data)
                    
                    # Set up reminder
                    def med_reminder():
                        while True:
                            try:
                                if schedule != "daily":
                                    # Parse time
                                    hour, minute = map(int, schedule.split(':'))
                                    now = datetime.now()
                                    reminder_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
                                    
                                    if now > reminder_time:
                                        reminder_time += timedelta(days=1)
                                    
                                    time_until = (reminder_time - now).total_seconds()
                                    time.sleep(time_until)
                                    
                                    self._show_notification("💊 Medication Reminder", f"Time to take {med_name}")
                                    time.sleep(86400)  # Wait 24 hours for next reminder
                                else:
                                    time.sleep(86400)  # Daily reminder at same time
                            except Exception:
                                time.sleep(3600)  # Wait 1 hour on error
                    
                    threading.Thread(target=med_reminder, daemon=True).start()
                    
                    return f"Medication added: {med_name}\nSchedule: {schedule}\nReminders enabled"
                else:
                    return "Please specify medication: 'add aspirin at 8am'"
            
            # Mark as taken
            elif 'taken' in query.lower() or 'took' in query.lower():
                med_match = re.search(r'(?:taken|took)\s+(.+)', query.lower())
                if med_match:
                    med_name = med_match.group(1).strip()
                    
                    for med in med_data['pills']:
                        if med_name.lower() in med['name'].lower():
                            med['last_taken'] = datetime.now().isoformat()
                            self._save_health_data(data)
                            return f"Marked {med['name']} as taken"
                    
                    return f"Medication '{med_name}' not found in your list"
                else:
                    return "Please specify which medication you took"
            
            # List medications
            else:
                if not med_data['pills']:
                    return "No medications added yet. Try: 'add vitamin D at 9am'"
                
                status = "Medication Schedule:\n" + "="*30 + "\n"
                
                for i, med in enumerate(med_data['pills'], 1):
                    status += f"{i}. {med['name']}\n"
                    status += f"   Schedule: {med['schedule']}\n"
                    
                    if med['last_taken']:
                        last_taken = datetime.fromisoformat(med['last_taken'])
                        hours_ago = (datetime.now() - last_taken).total_seconds() / 3600
                        status += f"   Last taken: {hours_ago:.1f} hours ago\n"
                    else:
                        status += f"   Last taken: Never\n"
                    
                    status += "\n"
                
                return status
                
        except Exception as e:
            return f"Medication reminder failed: {e}"
    
    def bmi_calculator(self, query=""):
        try:
            import re
            from datetime import datetime
            
            data = self._load_health_data()
            bmi_data = data['bmi']
            
            # Update weight/height
            if 'weight' in query.lower() or 'height' in query.lower():
                weight_match = re.search(r'weight\s+(\d+(?:\.\d+)?)\s*(?:kg|kilos?)?', query.lower())
                height_match = re.search(r'height\s+(\d+(?:\.\d+)?)\s*(?:cm|centimeters?)?', query.lower())
                
                if weight_match:
                    bmi_data['weight'] = float(weight_match.group(1))
                
                if height_match:
                    bmi_data['height'] = float(height_match.group(1))
                
                self._save_health_data(data)
            
            # Calculate BMI
            weight = bmi_data['weight']
            height = bmi_data['height'] / 100  # Convert cm to meters
            
            bmi = weight / (height * height)
            
            # BMI categories
            if bmi < 18.5:
                category = "Underweight"
                advice = "Consider consulting a nutritionist for healthy weight gain"
            elif bmi < 25:
                category = "Normal weight"
                advice = "Great! Maintain your current lifestyle"
            elif bmi < 30:
                category = "Overweight"
                advice = "Consider regular exercise and balanced diet"
            else:
                category = "Obese"
                advice = "Consult a healthcare provider for weight management"
            
            # Log BMI history
            bmi_data['history'].append({
                'timestamp': datetime.now().isoformat(),
                'bmi': round(bmi, 1),
                'weight': weight,
                'height': bmi_data['height'],
                'category': category
            })
            
            self._save_health_data(data)
            
            result = f"BMI Calculator:\n"
            result += f"Height: {bmi_data['height']} cm\n"
            result += f"Weight: {weight} kg\n"
            result += f"BMI: {bmi:.1f}\n"
            result += f"Category: {category}\n"
            result += f"Advice: {advice}"
            
            return result
            
        except Exception as e:
            return f"BMI calculator failed: {e}"
    
    def system_monitor(self, query=""):
        try:
            import psutil
            from datetime import datetime
            
            # CPU and Memory usage
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            # System temperatures (if available)
            try:
                temps = psutil.sensors_temperatures()
                temp_info = ""
                if temps:
                    for name, entries in temps.items():
                        for entry in entries:
                            temp_info += f"{entry.label or name}: {entry.current}°C "
            except:
                temp_info = "Temperature sensors not available"
            
            # Network activity
            net_io = psutil.net_io_counters()
            
            # Battery info (for laptops)
            try:
                battery = psutil.sensors_battery()
                battery_info = f"Battery: {battery.percent}% ({'Charging' if battery.power_plugged else 'Discharging'})" if battery else "No battery"
            except:
                battery_info = "Battery info unavailable"
            
            status = f"System Monitor:\n"
            status += f"CPU Usage: {cpu_percent}%\n"
            status += f"Memory: {memory.percent}% ({memory.used//1024//1024}MB/{memory.total//1024//1024}MB)\n"
            status += f"Disk: {disk.percent}% ({disk.used//1024//1024//1024}GB/{disk.total//1024//1024//1024}GB)\n"
            status += f"Network: {net_io.bytes_sent//1024//1024}MB sent, {net_io.bytes_recv//1024//1024}MB received\n"
            status += f"{battery_info}\n"
            status += f"Temperature: {temp_info}"
            
            # Alerts for high usage
            if cpu_percent > 80:
                self._show_notification("High CPU Usage", f"CPU at {cpu_percent}%")
            if memory.percent > 85:
                self._show_notification("High Memory Usage", f"RAM at {memory.percent}%")
            
            return status
            
        except ImportError:
            return "System monitoring requires: pip install psutil"
        except Exception as e:
            return f"System monitor failed: {e}"
    
    def network_monitor(self, query=""):
        try:
            import socket
            import subprocess
            import re
            
            # Get local IP
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            
            # Check internet connectivity
            try:
                socket.create_connection(("8.8.8.8", 53), timeout=3)
                internet_status = "Connected"
            except:
                internet_status = "Disconnected"
            
            # Get WiFi info (Windows)
            try:
                wifi_result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], 
                                           capture_output=True, text=True, timeout=10)
                wifi_profiles = len(re.findall(r'All User Profile\s*:\s*(.+)', wifi_result.stdout))
                
                # Current WiFi connection
                current_wifi = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], 
                                            capture_output=True, text=True, timeout=10)
                ssid_match = re.search(r'SSID\s*:\s*(.+)', current_wifi.stdout)
                current_ssid = ssid_match.group(1).strip() if ssid_match else "Not connected"
                
                signal_match = re.search(r'Signal\s*:\s*(\d+)%', current_wifi.stdout)
                signal_strength = signal_match.group(1) + "%" if signal_match else "Unknown"
                
            except:
                wifi_profiles = "Unknown"
                current_ssid = "Unknown"
                signal_strength = "Unknown"
            
            # Network speed test (simple ping)
            try:
                ping_result = subprocess.run(['ping', '-n', '4', '8.8.8.8'], 
                                           capture_output=True, text=True, timeout=15)
                avg_match = re.search(r'Average = (\d+)ms', ping_result.stdout)
                ping_time = avg_match.group(1) + "ms" if avg_match else "Failed"
            except:
                ping_time = "Failed"
            
            status = f"Network Monitor:\n"
            status += f"Local IP: {local_ip}\n"
            status += f"Internet: {internet_status}\n"
            status += f"Current WiFi: {current_ssid}\n"
            status += f"Signal Strength: {signal_strength}\n"
            status += f"Ping to Google: {ping_time}\n"
            status += f"Saved WiFi Networks: {wifi_profiles}"
            
            # Alert for connection issues
            if internet_status == "Disconnected":
                self._show_notification("Network Alert", "Internet connection lost")
            
            return status
            
        except Exception as e:
            return f"Network monitor failed: {e}"
    
    def language_translator(self, query=""):
        try:
            import re
            
            # Extract text and target language
            if 'translate' in query.lower():
                # Parse: "translate hello to spanish" or "translate 'bonjour' from french to english"
                translate_match = re.search(r'translate\s+["\']?(.+?)["\']?\s+(?:to|into)\s+(\w+)', query.lower())
                if translate_match:
                    text = translate_match.group(1).strip()
                    target_lang = translate_match.group(2).strip()
                else:
                    return "Usage: 'translate hello to spanish' or 'translate bonjour to english'"
            else:
                return "Please specify translation: 'translate [text] to [language]'"
            
            # Use AI for translation
            try:
                from engine.dual_ai import dual_ai
                
                ai_prompt = f'''Translate this text to {target_lang}: "{text}"
                
Respond ONLY in this format:
Original: [original text]
Language: [target language]
Translation: [translated text]
Pronunciation: [how to pronounce if applicable]
                
Example:
Original: hello
Language: spanish
Translation: hola
Pronunciation: OH-lah'''
                
                if dual_ai.ai_provider == 'groq':
                    response = dual_ai.groq_client.chat.completions.create(
                        messages=[{"role": "user", "content": ai_prompt}],
                        model="llama-3.1-8b-instant"
                    )
                    ai_response = response.choices[0].message.content.strip()
                else:
                    response = dual_ai.gemini_model.generate_content(ai_prompt)
                    ai_response = response.text.strip()
                
                # Parse AI response
                translation_match = re.search(r'Translation:\s*(.+)', ai_response, re.IGNORECASE)
                pronunciation_match = re.search(r'Pronunciation:\s*(.+)', ai_response, re.IGNORECASE)
                
                if translation_match:
                    translation = translation_match.group(1).strip()
                    pronunciation = pronunciation_match.group(1).strip() if pronunciation_match else ""
                    
                    result = f"Translation:\n"
                    result += f"'{text}' -> '{translation}' ({target_lang})"
                    if pronunciation:
                        result += f"\nPronunciation: {pronunciation}"
                    
                    return result
                else:
                    return f"Could not translate '{text}' to {target_lang}"
                    
            except Exception:
                # Fallback to basic translation service
                try:
                    import requests
                    
                    # Use Google Translate API (free tier)
                    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl={target_lang}&dt=t&q={text}"
                    response = requests.get(url, timeout=5)
                    
                    if response.status_code == 200:
                        result_data = response.json()
                        translation = result_data[0][0][0]
                        return f"Translation: '{text}' -> '{translation}' ({target_lang})"
                    else:
                        return "Translation service unavailable"
                        
                except Exception:
                    return f"Translation failed for '{text}' to {target_lang}"
                    
        except Exception as e:
            return f"Language translator failed: {e}"
    
    def dictionary_lookup(self, query=""):
        try:
            import re
            
            # Extract word to define
            if 'define' in query.lower():
                word_match = re.search(r'define\s+(\w+)', query.lower())
                if word_match:
                    word = word_match.group(1).strip()
                else:
                    return "Usage: 'define [word]' - Example: 'define computer'"
            elif 'dictionary' in query.lower():
                word_match = re.search(r'dictionary\s+(\w+)', query.lower())
                if word_match:
                    word = word_match.group(1).strip()
                else:
                    return "Usage: 'dictionary [word]' - Example: 'dictionary science'"
            else:
                # Extract any word from query
                words = re.findall(r'\b[a-zA-Z]{3,}\b', query)
                if words:
                    word = words[-1]  # Take last significant word
                else:
                    return "Please specify a word to define"
            
            # Use AI for comprehensive definition
            try:
                from engine.dual_ai import dual_ai
                
                ai_prompt = f'''Provide a comprehensive definition for the word: "{word}"
                
Respond ONLY in this format:
Word: [word]
Pronunciation: [phonetic pronunciation]
Part of Speech: [noun/verb/adjective/etc.]
Definition: [clear definition]
Example: [example sentence]
Synonyms: [similar words]
Etymology: [word origin if known]
                
Example:
Word: computer
Pronunciation: kuhm-PYOO-ter
Part of Speech: noun
Definition: An electronic device that processes data and performs calculations
Example: I use my computer for work and entertainment
Synonyms: PC, machine, device
Etymology: From Latin "computare" meaning to calculate'''
                
                if dual_ai.ai_provider == 'groq':
                    response = dual_ai.groq_client.chat.completions.create(
                        messages=[{"role": "user", "content": ai_prompt}],
                        model="llama-3.1-8b-instant"
                    )
                    ai_response = response.choices[0].message.content.strip()
                else:
                    response = dual_ai.gemini_model.generate_content(ai_prompt)
                    ai_response = response.text.strip()
                
                # Format the response nicely
                lines = ai_response.split('\n')
                formatted_def = f"Dictionary Lookup: {word.upper()}\n" + "="*40 + "\n"
                
                for line in lines:
                    if ':' in line:
                        formatted_def += line + "\n"
                
                return formatted_def
                
            except Exception:
                # Fallback to simple definition
                return f"Definition of '{word}': A word requiring dictionary lookup. Please check online dictionary for detailed definition."
                
        except Exception as e:
            return f"Dictionary lookup failed: {e}"
    
    def wikipedia_search(self, query=""):
        try:
            import re
            import requests
            
            # Extract search term
            if 'wikipedia' in query.lower() or 'wiki' in query.lower():
                search_match = re.search(r'(?:wikipedia|wiki)\s+(.+)', query.lower())
                if search_match:
                    search_term = search_match.group(1).strip()
                else:
                    return "Usage: 'wikipedia [topic]' - Example: 'wikipedia artificial intelligence'"
            else:
                search_term = query.strip()
            
            if not search_term:
                return "Please specify a topic to search"
            
            # Search Wikipedia API
            try:
                # Get page summary
                wiki_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{search_term.replace(' ', '_')}"
                response = requests.get(wiki_url, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    title = data.get('title', search_term)
                    extract = data.get('extract', 'No summary available')
                    page_url = data.get('content_urls', {}).get('desktop', {}).get('page', '')
                    
                    # Limit extract length
                    if len(extract) > 500:
                        extract = extract[:500] + "..."
                    
                    result = f"Wikipedia: {title}\n" + "="*50 + "\n"
                    result += f"{extract}\n\n"
                    result += f"Full article: {page_url}"
                    
                    return result
                else:
                    # Try search if direct lookup fails
                    search_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={search_term}&format=json&srlimit=1"
                    search_response = requests.get(search_url, timeout=10)
                    
                    if search_response.status_code == 200:
                        search_data = search_response.json()
                        if search_data['query']['search']:
                            page_title = search_data['query']['search'][0]['title']
                            return f"Found: {page_title}. Try: 'wikipedia {page_title}'"
                    
                    return f"No Wikipedia article found for '{search_term}'"
                    
            except Exception:
                return f"Wikipedia search failed for '{search_term}'"
                
        except Exception as e:
            return f"Wikipedia search failed: {e}"
    
    def calculator_advanced(self, query=""):
        try:
            import re
            import math
            
            # Extract mathematical expression
            if 'calculate' in query.lower():
                calc_match = re.search(r'calculate\s+(.+)', query.lower())
                if calc_match:
                    expression = calc_match.group(1).strip()
                else:
                    return "Usage: 'calculate [expression]' - Example: 'calculate sin(45) + log(10)'"
            else:
                expression = query.strip()
            
            if not expression:
                return "Please provide a mathematical expression"
            
            # Use AI for complex calculations
            try:
                from engine.dual_ai import dual_ai
                
                ai_prompt = f'''Solve this mathematical expression: "{expression}"
                
Respond ONLY in this format:
Expression: [original expression]
Result: [numerical result]
Steps: [calculation steps if complex]
Explanation: [brief explanation]
                
Support: basic arithmetic (+,-,*,/), powers (^,**), roots (sqrt), trigonometry (sin,cos,tan), logarithms (log,ln), constants (pi,e)
                
Example:
Expression: sin(45) + log(10)
Result: 0.707 + 1.000 = 1.707
Steps: sin(45°) = 0.707, log₁₀(10) = 1.000
Explanation: Sine of 45 degrees plus logarithm base 10 of 10'''
                
                if dual_ai.ai_provider == 'groq':
                    response = dual_ai.groq_client.chat.completions.create(
                        messages=[{"role": "user", "content": ai_prompt}],
                        model="llama-3.1-8b-instant"
                    )
                    ai_response = response.choices[0].message.content.strip()
                else:
                    response = dual_ai.gemini_model.generate_content(ai_prompt)
                    ai_response = response.text.strip()
                
                return f"Advanced Calculator:\n{ai_response}"
                
            except Exception:
                # Fallback to basic Python evaluation
                try:
                    # Replace common math functions
                    safe_expr = expression.lower()
                    safe_expr = safe_expr.replace('^', '**')
                    safe_expr = safe_expr.replace('sin', 'math.sin')
                    safe_expr = safe_expr.replace('cos', 'math.cos')
                    safe_expr = safe_expr.replace('tan', 'math.tan')
                    safe_expr = safe_expr.replace('log', 'math.log10')
                    safe_expr = safe_expr.replace('ln', 'math.log')
                    safe_expr = safe_expr.replace('sqrt', 'math.sqrt')
                    safe_expr = safe_expr.replace('pi', 'math.pi')
                    safe_expr = safe_expr.replace('e', 'math.e')
                    
                    # Evaluate safely
                    result = eval(safe_expr, {"__builtins__": {}, "math": math})
                    return f"Calculator: {expression} = {result}"
                    
                except Exception:
                    return f"Invalid mathematical expression: '{expression}'"
                    
        except Exception as e:
            return f"Calculator failed: {e}"
    
    def unit_converter(self, query=""):
        try:
            import re
            
            # Extract conversion request
            convert_match = re.search(r'convert\s+(\d+(?:\.\d+)?)\s*(\w+)\s+(?:to|into)\s+(\w+)', query.lower())
            if convert_match:
                value = float(convert_match.group(1))
                from_unit = convert_match.group(2).strip()
                to_unit = convert_match.group(3).strip()
            else:
                return "Usage: 'convert 100 meters to feet' or 'convert 32 fahrenheit to celsius'"
            
            # Use AI for intelligent unit conversion
            try:
                from engine.dual_ai import dual_ai
                
                ai_prompt = f'''Convert {value} {from_unit} to {to_unit}
                
Respond ONLY in this format:
Original: [value] [from_unit]
Converted: [result] [to_unit]
Formula: [conversion formula]
Category: [length/weight/temperature/etc.]
                
Support common units: meters/feet/inches, kg/pounds/ounces, celsius/fahrenheit/kelvin, liters/gallons/cups, etc.
                
Example:
Original: 100 meters
Converted: 328.08 feet
Formula: meters × 3.28084 = feet
Category: length'''
                
                if dual_ai.ai_provider == 'groq':
                    response = dual_ai.groq_client.chat.completions.create(
                        messages=[{"role": "user", "content": ai_prompt}],
                        model="llama-3.1-8b-instant"
                    )
                    ai_response = response.choices[0].message.content.strip()
                else:
                    response = dual_ai.gemini_model.generate_content(ai_prompt)
                    ai_response = response.text.strip()
                
                return f"Unit Converter:\n{ai_response}"
                
            except Exception:
                # Fallback to basic conversions
                conversions = {
                    ('meters', 'feet'): 3.28084,
                    ('feet', 'meters'): 0.3048,
                    ('kg', 'pounds'): 2.20462,
                    ('pounds', 'kg'): 0.453592,
                    ('celsius', 'fahrenheit'): lambda c: c * 9/5 + 32,
                    ('fahrenheit', 'celsius'): lambda f: (f - 32) * 5/9,
                }
                
                key = (from_unit.lower(), to_unit.lower())
                if key in conversions:
                    factor = conversions[key]
                    if callable(factor):
                        result = factor(value)
                    else:
                        result = value * factor
                    
                    return f"Unit Conversion: {value} {from_unit} = {result:.4f} {to_unit}"
                else:
                    return f"Conversion from {from_unit} to {to_unit} not supported"
                    
        except Exception as e:
            return f"Unit converter failed: {e}"
    
    def flashcard_system(self, query=""):
        try:
            import json
            import random
            import re
            
            flashcards_file = "flashcards.json"
            
            # Load existing flashcards
            try:
                with open(flashcards_file, 'r') as f:
                    flashcards = json.load(f)
            except:
                flashcards = {'decks': {}}
            
            # Add new flashcard
            if 'add' in query.lower() and 'flashcard' in query.lower():
                # Parse: "add flashcard python: programming language"
                add_match = re.search(r'add flashcard\s+(.+?):\s*(.+)', query.lower())
                if add_match:
                    question = add_match.group(1).strip()
                    answer = add_match.group(2).strip()
                    
                    deck_name = "general"
                    if 'deck' in query.lower():
                        deck_match = re.search(r'deck\s+(\w+)', query.lower())
                        if deck_match:
                            deck_name = deck_match.group(1)
                    
                    if deck_name not in flashcards['decks']:
                        flashcards['decks'][deck_name] = []
                    
                    from datetime import datetime
                    flashcards['decks'][deck_name].append({
                        'question': question,
                        'answer': answer,
                        'created': datetime.now().isoformat()
                    })
                    
                    with open(flashcards_file, 'w') as f:
                        json.dump(flashcards, f, indent=2)
                    
                    return f"Flashcard added to '{deck_name}' deck: {question} -> {answer}"
                else:
                    return "Usage: 'add flashcard [question]: [answer]' - Example: 'add flashcard capital of france: paris'"
            
            # Study flashcards
            elif 'study' in query.lower() or 'flashcard' in query.lower():
                if not flashcards['decks']:
                    return "No flashcards available. Add some first: 'add flashcard [question]: [answer]'"
                
                # Select deck
                deck_name = "general"
                if 'deck' in query.lower():
                    deck_match = re.search(r'deck\s+(\w+)', query.lower())
                    if deck_match:
                        deck_name = deck_match.group(1)
                
                if deck_name not in flashcards['decks'] or not flashcards['decks'][deck_name]:
                    available_decks = list(flashcards['decks'].keys())
                    return f"Deck '{deck_name}' not found. Available decks: {', '.join(available_decks)}"
                
                # Get random flashcard
                cards = flashcards['decks'][deck_name]
                card = random.choice(cards)
                
                return f"Flashcard Study - {deck_name.title()} Deck:\nQuestion: {card['question']}\n\n(Say 'answer' to reveal the answer)"
            
            # Show answer
            elif 'answer' in query.lower():
                return "Feature: Show last flashcard answer (implement session tracking)"
            
            # List decks
            else:
                if not flashcards['decks']:
                    return "No flashcard decks available. Create your first: 'add flashcard [question]: [answer]'"
                
                result = "Flashcard Decks:\n" + "="*30 + "\n"
                for deck_name, cards in flashcards['decks'].items():
                    result += f"{deck_name.title()}: {len(cards)} cards\n"
                
                result += "\nUsage: 'study flashcard deck [name]' or 'add flashcard [question]: [answer]'"
                return result
                
        except Exception as e:
            return f"Flashcard system failed: {e}"
    
    def quiz_generator(self, query=""):
        try:
            import re
            
            # Extract quiz topic
            if 'quiz' in query.lower():
                topic_match = re.search(r'quiz\s+(?:on\s+|about\s+)?(.+)', query.lower())
                if topic_match:
                    topic = topic_match.group(1).strip()
                else:
                    topic = "general knowledge"
            else:
                topic = query.strip() or "general knowledge"
            
            # Use AI to generate quiz questions
            try:
                from engine.dual_ai import dual_ai
                
                ai_prompt = f'''Generate a quiz about: "{topic}"
                
Create 5 multiple choice questions. Respond ONLY in this format:

QUIZ: {topic.upper()}

Q1: [question]
A) [option A]
B) [option B] 
C) [option C]
D) [option D]
Correct: [A/B/C/D]

Q2: [question]
A) [option A]
B) [option B]
C) [option C] 
D) [option D]
Correct: [A/B/C/D]

[Continue for Q3, Q4, Q5]

Make questions educational and appropriate difficulty level.'''
                
                if dual_ai.ai_provider == 'groq':
                    response = dual_ai.groq_client.chat.completions.create(
                        messages=[{"role": "user", "content": ai_prompt}],
                        model="llama-3.1-8b-instant"
                    )
                    ai_response = response.choices[0].message.content.strip()
                else:
                    response = dual_ai.gemini_model.generate_content(ai_prompt)
                    ai_response = response.text.strip()
                
                return f"Quiz Generator:\n{ai_response}\n\nSay 'quiz answers' to see the correct answers!"
                
            except Exception:
                # Fallback to simple quiz
                sample_questions = {
                    "general": [
                        "What is the capital of France? A) London B) Berlin C) Paris D) Madrid",
                        "What is 2+2? A) 3 B) 4 C) 5 D) 6",
                        "Which planet is closest to the Sun? A) Venus B) Mercury C) Earth D) Mars"
                    ],
                    "science": [
                        "What is H2O? A) Hydrogen B) Oxygen C) Water D) Carbon",
                        "Speed of light? A) 300,000 km/s B) 150,000 km/s C) 450,000 km/s D) 600,000 km/s"
                    ]
                }
                
                questions = sample_questions.get("general", sample_questions["general"])
                
                result = f"Quiz: {topic.title()}\n" + "="*30 + "\n"
                for i, q in enumerate(questions[:3], 1):
                    result += f"Q{i}: {q}\n\n"
                
                return result
                
        except Exception as e:
            return f"Quiz generator failed: {e}"
    
    def meme_generator(self, query=""):
        try:
            import re
            
            # Extract meme request
            if 'meme' in query.lower():
                meme_match = re.search(r'meme\s+(.+)', query.lower())
                if meme_match:
                    meme_request = meme_match.group(1).strip()
                else:
                    meme_request = "funny programming joke"
            else:
                meme_request = query.strip() or "random funny meme"
            
            # Use AI to generate meme concept
            try:
                from engine.dual_ai import dual_ai
                
                ai_prompt = f'''Create a meme concept for: "{meme_request}"
                
Respond ONLY in this format:
Template: [meme template name]
Top Text: [text for top]
Bottom Text: [text for bottom]
Style: [humor style]
Description: [visual description]
                
Examples:
Template: Drake Pointing
Top Text: Using print() for debugging
Bottom Text: Using proper debugger
Style: Programming humor
Description: Drake disapproving of print, approving debugger
                
Make it funny and relatable!'''
                
                if dual_ai.ai_provider == 'groq':
                    response = dual_ai.groq_client.chat.completions.create(
                        messages=[{"role": "user", "content": ai_prompt}],
                        model="llama-3.1-8b-instant"
                    )
                    ai_response = response.choices[0].message.content.strip()
                else:
                    response = dual_ai.gemini_model.generate_content(ai_prompt)
                    ai_response = response.text.strip()
                
                return f"Meme Generator:\n{ai_response}\n\nNote: Use online meme generators like imgflip.com to create the actual image!"
                
            except Exception:
                # Fallback meme concepts
                templates = {
                    "programming": "Template: Distracted Boyfriend\nTop: Me\nGirlfriend: Current project\nOther woman: New framework",
                    "work": "Template: This is Fine\nTop: Everything is under control\nBottom: (while everything burns)",
                    "study": "Template: Drake Pointing\nTop: Studying early\nBottom: Cramming last minute"
                }
                
                concept_type = "programming" if any(word in meme_request for word in ['code', 'programming', 'developer']) else "work"
                concept = templates.get(concept_type, templates["work"])
                
                return f"Meme Generator:\n{concept}\n\nUse imgflip.com or similar to create the image!"
                
        except Exception as e:
            return f"Meme generator failed: {e}"
    
    def logo_generator(self, query=""):
        try:
            import re
            
            # Extract logo requirements
            company_match = re.search(r'logo\s+(?:for\s+)?(.+?)(?:\s+(?:blue|red|green|black|white|color))?', query.lower())
            if company_match:
                company_name = company_match.group(1).strip()
            else:
                company_name = "MyCompany"
            
            # Extract colors
            colors = []
            color_words = ['blue', 'red', 'green', 'black', 'white', 'yellow', 'purple', 'orange']
            for color in color_words:
                if color in query.lower():
                    colors.append(color)
            
            if not colors:
                colors = ['blue', 'white']
            
            # Use AI to generate logo concept
            try:
                from engine.dual_ai import dual_ai
                
                ai_prompt = f'''Design a logo concept for: "{company_name}" using colors: {', '.join(colors)}
                
Respond ONLY in this format:
Company: [company name]
Concept: [logo concept]
Colors: [color scheme]
Font: [font style]
Symbol: [icon/symbol idea]
Style: [modern/classic/minimalist/etc]
Description: [detailed visual description]
                
Example:
Company: TechCorp
Concept: Tech innovation and reliability
Colors: Blue (#0066CC) and White (#FFFFFF)
Font: Modern sans-serif, bold
Symbol: Stylized circuit pattern forming a "T"
Style: Modern, minimalist
Description: Clean geometric design with tech elements
                
Make it professional and memorable!'''
                
                if dual_ai.ai_provider == 'groq':
                    response = dual_ai.groq_client.chat.completions.create(
                        messages=[{"role": "user", "content": ai_prompt}],
                        model="llama-3.1-8b-instant"
                    )
                    ai_response = response.choices[0].message.content.strip()
                else:
                    response = dual_ai.gemini_model.generate_content(ai_prompt)
                    ai_response = response.text.strip()
                
                return f"Logo Generator:\n{ai_response}\n\nRecommended tools: Canva, Figma, or Adobe Illustrator"
                
            except Exception:
                # Fallback logo concept
                return f"Logo Generator:\nCompany: {company_name.title()}\nConcept: Professional and modern\nColors: {', '.join(colors)}\nFont: Clean sans-serif\nSymbol: Abstract geometric shape\nStyle: Minimalist\nDescription: Simple, scalable design with company initials"
                
        except Exception as e:
            return f"Logo generator failed: {e}"
    
    def color_palette_generator(self, query=""):
        try:
            import re
            import random
            
            # Extract theme
            theme_match = re.search(r'(?:color|palette)\s+(.+)', query.lower())
            if theme_match:
                theme = theme_match.group(1).strip()
            else:
                theme = "modern"
            
            # Use AI to generate color palette
            try:
                from engine.dual_ai import dual_ai
                
                ai_prompt = f'''Generate a color palette for theme: "{theme}"
                
Respond ONLY in this format:
Theme: [theme name]
Primary: [color name] (#HEXCODE)
Secondary: [color name] (#HEXCODE)
Accent: [color name] (#HEXCODE)
Neutral: [color name] (#HEXCODE)
Background: [color name] (#HEXCODE)
Mood: [emotional description]
Use Case: [where to use this palette]
                
Example:
Theme: Ocean Sunset
Primary: Deep Blue (#1E3A8A)
Secondary: Coral Orange (#FF7F50)
Accent: Golden Yellow (#FFD700)
Neutral: Warm Gray (#8B7355)
Background: Cream White (#FFF8DC)
Mood: Calm, warm, inspiring
Use Case: Website, branding, presentations
                
Provide harmonious, professional colors!'''
                
                if dual_ai.ai_provider == 'groq':
                    response = dual_ai.groq_client.chat.completions.create(
                        messages=[{"role": "user", "content": ai_prompt}],
                        model="llama-3.1-8b-instant"
                    )
                    ai_response = response.choices[0].message.content.strip()
                else:
                    response = dual_ai.gemini_model.generate_content(ai_prompt)
                    ai_response = response.text.strip()
                
                return f"Color Palette Generator:\n{ai_response}\n\nTip: Use tools like Coolors.co or Adobe Color for visualization"
                
            except Exception:
                # Fallback color palettes
                palettes = {
                    "modern": ["#2563EB", "#64748B", "#F59E0B", "#EF4444", "#F8FAFC"],
                    "nature": ["#16A34A", "#84CC16", "#EAB308", "#92400E", "#F7FEE7"],
                    "ocean": ["#0EA5E9", "#06B6D4", "#3B82F6", "#1E40AF", "#F0F9FF"]
                }
                
                colors = palettes.get(theme, palettes["modern"])
                result = f"Color Palette: {theme.title()}\n"
                for i, color in enumerate(colors):
                    labels = ["Primary", "Secondary", "Accent", "Neutral", "Background"]
                    result += f"{labels[i]}: {color}\n"
                
                return result
                
        except Exception as e:
            return f"Color palette generator failed: {e}"
    
    def font_viewer(self, query=""):
        try:
            import platform
            
            # Get system info
            system = platform.system()
            
            # Use AI to recommend fonts
            try:
                from engine.dual_ai import dual_ai
                
                ai_prompt = f'''Recommend fonts for: "{query or 'general use'}"
                
Respond ONLY in this format:
Purpose: [use case]
Heading Font: [font name] - [description]
Body Font: [font name] - [description]
Display Font: [font name] - [description]
Monospace: [font name] - [description]
System Fonts: [list of common system fonts]
Web Safe: [web-safe alternatives]
Google Fonts: [free alternatives]
                
Example:
Purpose: Professional presentation
Heading Font: Arial Black - Bold, impactful
Body Font: Calibri - Clean, readable
Display Font: Impact - Strong presence
Monospace: Consolas - Code and data
System Fonts: Arial, Times New Roman, Verdana
Web Safe: Helvetica, Georgia, Courier
Google Fonts: Roboto, Open Sans, Lato
                
Focus on readability and professionalism!'''
                
                if dual_ai.ai_provider == 'groq':
                    response = dual_ai.groq_client.chat.completions.create(
                        messages=[{"role": "user", "content": ai_prompt}],
                        model="llama-3.1-8b-instant"
                    )
                    ai_response = response.choices[0].message.content.strip()
                else:
                    response = dual_ai.gemini_model.generate_content(ai_prompt)
                    ai_response = response.text.strip()
                
                return f"Font Viewer ({system}):\n{ai_response}\n\nUse Character Map (Windows) or Font Book (Mac) to preview fonts"
                
            except Exception:
                # Fallback font recommendations
                common_fonts = {
                    "Windows": ["Arial", "Calibri", "Times New Roman", "Verdana", "Consolas"],
                    "Darwin": ["Helvetica", "San Francisco", "Times", "Menlo", "Monaco"],
                    "Linux": ["DejaVu Sans", "Liberation Sans", "Ubuntu", "Noto Sans"]
                }
                
                fonts = common_fonts.get(system, common_fonts["Windows"])
                result = f"Font Viewer ({system}):\n"
                result += f"Common System Fonts:\n"
                for font in fonts:
                    result += f"- {font}\n"
                
                return result
                
        except Exception as e:
            return f"Font viewer failed: {e}"
    
    def ascii_art_generator(self, query=""):
        try:
            import re
            
            # Extract text to convert
            text_match = re.search(r'ascii\s+(?:art\s+)?(.+)', query.lower())
            if text_match:
                text = text_match.group(1).strip()
            else:
                text = "HELLO"
            
            # Use AI to generate ASCII art
            try:
                from engine.dual_ai import dual_ai
                
                ai_prompt = f'''Create ASCII art for text: "{text}"
                
Respond ONLY with ASCII art using characters like: # * - = + | \\ / _ ^
                
Make it readable and artistic. Example for "HI":

#   #  ###
#   #   #
#####   #
#   #   #
#   #  ###
                
Create similar art for the given text.'''
                
                if dual_ai.ai_provider == 'groq':
                    response = dual_ai.groq_client.chat.completions.create(
                        messages=[{"role": "user", "content": ai_prompt}],
                        model="llama-3.1-8b-instant"
                    )
                    ai_response = response.choices[0].message.content.strip()
                else:
                    response = dual_ai.gemini_model.generate_content(ai_prompt)
                    ai_response = response.text.strip()
                
                return f"ASCII Art Generator:\n{ai_response}"
                
            except Exception:
                # Fallback simple ASCII
                simple_ascii = {
                    "hello": "#   # ##### #     #     #####\n#   # #     #     #     #    \n##### ##### #     #     #####\n#   # #     #     #     #    \n#   # ##### ##### ##### #####",
                    "hi": "#   #  ###\n#   #   #\n#####   #\n#   #   #\n#   #  ###"
                }
                
                art = simple_ascii.get(text.lower(), f"ASCII: {text.upper()}")
                return f"ASCII Art Generator:\n{art}"
                
        except Exception as e:
            return f"ASCII art generator failed: {e}"
    
    def barcode_generator(self, query=""):
        try:
            import re
            
            # Extract data to encode
            data_match = re.search(r'barcode\s+(.+)', query.lower())
            if data_match:
                data = data_match.group(1).strip()
            else:
                data = "123456789"
            
            # Use AI to generate barcode info
            try:
                from engine.dual_ai import dual_ai
                
                ai_prompt = f'''Generate barcode information for: "{data}"
                
Respond ONLY in this format:
Data: [input data]
Type: [barcode type - Code128/EAN/QR/etc]
Format: [numeric/alphanumeric/text]
Use Case: [where this would be used]
Pattern: [simplified visual pattern]
Tools: [recommended generators]
                
Example:
Data: 123456789
Type: Code128
Format: Numeric
Use Case: Product identification
Pattern: |||| | || ||| | |||| |
Tools: Online generators, ZXing, python-barcode
                
Choose appropriate barcode type for the data!'''
                
                if dual_ai.ai_provider == 'groq':
                    response = dual_ai.groq_client.chat.completions.create(
                        messages=[{"role": "user", "content": ai_prompt}],
                        model="llama-3.1-8b-instant"
                    )
                    ai_response = response.choices[0].message.content.strip()
                else:
                    response = dual_ai.gemini_model.generate_content(ai_prompt)
                    ai_response = response.text.strip()
                
                return f"Barcode Generator:\n{ai_response}\n\nRecommended: Use online barcode generators or python-barcode library"
                
            except Exception:
                # Fallback barcode info
                barcode_type = "QR Code" if len(data) > 20 else "Code128"
                return f"Barcode Generator:\nData: {data}\nType: {barcode_type}\nUse online generators like barcode-generator.org"
                
        except Exception as e:
            return f"Barcode generator failed: {e}"
    
    def mind_map_creator(self, query=""):
        try:
            import re
            
            # Extract topic
            topic_match = re.search(r'mind\s*map\s+(.+)', query.lower())
            if topic_match:
                topic = topic_match.group(1).strip()
            else:
                topic = "project planning"
            
            # Use AI to generate mind map structure
            try:
                from engine.dual_ai import dual_ai
                
                ai_prompt = f'''Create a mind map structure for: "{topic}"
                
Respond ONLY in this format:
Central Topic: [main topic]
Branch 1: [subtopic]
  - [detail 1]
  - [detail 2]
Branch 2: [subtopic]
  - [detail 1]
  - [detail 2]
Branch 3: [subtopic]
  - [detail 1]
  - [detail 2]
Connections: [how branches relate]
Colors: [suggested color scheme]
Tools: [recommended mind mapping tools]
                
Example:
Central Topic: Learning Python
Branch 1: Basics
  - Variables and data types
  - Control structures
Branch 2: Advanced
  - Object-oriented programming
  - Libraries and frameworks
Branch 3: Practice
  - Projects
  - Problem solving
Connections: Basics → Advanced → Practice
Colors: Blue for basics, Green for advanced, Orange for practice
Tools: XMind, MindMeister, Lucidchart
                
Make it comprehensive and logical!'''
                
                if dual_ai.ai_provider == 'groq':
                    response = dual_ai.groq_client.chat.completions.create(
                        messages=[{"role": "user", "content": ai_prompt}],
                        model="llama-3.1-8b-instant"
                    )
                    ai_response = response.choices[0].message.content.strip()
                else:
                    response = dual_ai.gemini_model.generate_content(ai_prompt)
                    ai_response = response.text.strip()
                
                return f"Mind Map Creator:\n{ai_response}\n\nRecommended tools: XMind, MindMeister, or draw.io for digital creation"
                
            except Exception:
                # Fallback mind map structure
                return f"Mind Map Creator:\nCentral Topic: {topic.title()}\nBranch 1: Planning\n  - Goals\n  - Timeline\nBranch 2: Resources\n  - Tools\n  - People\nBranch 3: Implementation\n  - Steps\n  - Milestones\n\nUse XMind or similar tools to create visual mind map"
                
        except Exception as e:
            return f"Mind map creator failed: {e}"
    
    def password_manager(self, query=""):
        try:
            import json
            import os
            import re
            
            try:
                from cryptography.fernet import Fernet  # type: ignore
            except ImportError:
                return "🔐 Password manager requires: pip install cryptography"
            
            # Password storage file
            password_file = "passwords.json"
            key_file = "password_key.key"
            
            # Generate or load encryption key
            if not os.path.exists(key_file):
                key = Fernet.generate_key()
                with open(key_file, 'wb') as f:
                    f.write(key)
            else:
                with open(key_file, 'rb') as f:
                    key = f.read()
            
            cipher = Fernet(key)
            
            # Load existing passwords
            passwords = {}
            if os.path.exists(password_file):
                try:
                    with open(password_file, 'r') as f:
                        encrypted_data = json.load(f)
                    for service, encrypted_pass in encrypted_data.items():
                        passwords[service] = cipher.decrypt(encrypted_pass.encode()).decode()
                except:
                    passwords = {}
            
            # Show password command
            if 'show' in query.lower() or 'get' in query.lower():
                service_match = re.search(r'(?:show|get)\s+(?:my\s+)?(\w+)\s+password', query.lower())
                if service_match:
                    service = service_match.group(1).lower()
                    if service in passwords:
                        return f"🔐 {service.title()} password: {passwords[service]}"
                    else:
                        return f"🔐 No password stored for {service}. Available: {', '.join(passwords.keys())}"
                else:
                    return f"🔐 Stored passwords: {', '.join(passwords.keys()) if passwords else 'None'}\nUsage: 'show gmail password'"
            
            # Add password command
            elif 'add' in query.lower() or 'store' in query.lower():
                add_match = re.search(r'(?:add|store)\s+(\w+)\s+password\s+(.+)', query.lower())
                if add_match:
                    service = add_match.group(1).lower()
                    password = add_match.group(2).strip()
                    
                    passwords[service] = password
                    
                    # Encrypt and save
                    encrypted_data = {}
                    for svc, pwd in passwords.items():
                        encrypted_data[svc] = cipher.encrypt(pwd.encode()).decode()
                    
                    with open(password_file, 'w') as f:
                        json.dump(encrypted_data, f)
                    
                    return f" Password for {service} stored securely"
                else:
                    return " Usage: 'add gmail password mypassword123'"
            
            # List passwords
            else:
                if passwords:
                    return f" Password Manager - Stored accounts: {', '.join(passwords.keys())}\nSay 'show [service] password' to retrieve"
                else:
                    return " Password Manager - No passwords stored yet\nUsage: 'add gmail password mypassword123'"
                    
        except Exception as e:
            return f" Password manager failed: {e}"
    
    def startup_manager(self, query=""):
        try:
            import subprocess
            import os
            import re
            
            # Add startup app
            if 'add' in query.lower():
                app_match = re.search(r'add\s+(?:startup\s+)?(\w+)', query.lower())
                if app_match:
                    app_name = app_match.group(1)
                    
                    # Windows startup registry
                    try:
                        import winreg
                        key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
                        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
                        
                        # For demo, we'll add notepad as example
                        app_path = "notepad.exe" if app_name.lower() == "notepad" else f"{app_name}.exe"
                        winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, app_path)
                        winreg.CloseKey(key)
                        
                        return f"Added {app_name} to startup programs"
                    except Exception as e:
                        return f"Failed to add {app_name} to startup: {e}"
                else:
                    return "Usage: 'add startup notepad' or 'add chrome to startup'"
            
            # Remove startup app
            elif 'remove' in query.lower():
                app_match = re.search(r'remove\s+(?:startup\s+)?(\w+)', query.lower())
                if app_match:
                    app_name = app_match.group(1)
                    
                    try:
                        import winreg
                        key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
                        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
                        
                        winreg.DeleteValue(key, app_name)
                        winreg.CloseKey(key)
                        
                        return f"Removed {app_name} from startup programs"
                    except FileNotFoundError:
                        return f"{app_name} not found in startup programs"
                    except Exception as e:
                        return f"Failed to remove {app_name}: {e}"
                else:
                    return "Usage: 'remove startup notepad'"
            
            # List startup apps
            else:
                try:
                    import winreg
                    key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
                    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)
                    
                    startup_apps = []
                    i = 0
                    while True:
                        try:
                            name, value, _ = winreg.EnumValue(key, i)
                            startup_apps.append(f"{name}: {value}")
                            i += 1
                        except WindowsError:
                            break
                    
                    winreg.CloseKey(key)
                    
                    if startup_apps:
                        result = "Startup Programs:\n" + "\n".join(startup_apps)
                    else:
                        result = "No custom startup programs found"
                    
                    return result
                    
                except Exception as e:
                    return f"Failed to list startup programs: {e}"
                    
        except Exception as e:
            return f"Startup manager failed: {e}"
    
    def git_helper(self, query=""):
        try:
            import subprocess
            import os
            import re
            
            # Check if in git repository
            try:
                subprocess.run(['git', 'status'], capture_output=True, check=True)
            except subprocess.CalledProcessError:
                return "Not in a git repository. Navigate to a git project first."
            
            # Git commit
            if 'commit' in query.lower():
                message_match = re.search(r'commit\s+["\']?(.+?)["\']?$', query)
                if message_match:
                    commit_message = message_match.group(1).strip()
                else:
                    commit_message = "Auto commit via Jarvis"
                
                try:
                    # Add all changes
                    subprocess.run(['git', 'add', '.'], check=True)
                    
                    # Commit with message
                    result = subprocess.run(['git', 'commit', '-m', commit_message], 
                                          capture_output=True, text=True, check=True)
                    
                    return f"Git commit successful: '{commit_message}'\n{result.stdout}"
                except subprocess.CalledProcessError as e:
                    return f"Git commit failed: {e.stderr}"
            
            # Git push
            elif 'push' in query.lower():
                try:
                    result = subprocess.run(['git', 'push'], capture_output=True, text=True, check=True)
                    return f"Git push successful\n{result.stdout}"
                except subprocess.CalledProcessError as e:
                    return f"Git push failed: {e.stderr}"
            
            # Git status
            elif 'status' in query.lower():
                try:
                    result = subprocess.run(['git', 'status', '--short'], capture_output=True, text=True, check=True)
                    if result.stdout.strip():
                        return f"Git status:\n{result.stdout}"
                    else:
                        return "Git status: Working directory clean"
                except subprocess.CalledProcessError as e:
                    return f"Git status failed: {e.stderr}"
            
            # Default: show git status
            else:
                try:
                    status_result = subprocess.run(['git', 'status', '--short'], capture_output=True, text=True)
                    branch_result = subprocess.run(['git', 'branch', '--show-current'], capture_output=True, text=True)
                    
                    current_branch = branch_result.stdout.strip()
                    status = status_result.stdout.strip()
                    
                    result = f"Git Helper - Branch: {current_branch}\n"
                    if status:
                        result += f"Changes:\n{status}\n"
                    else:
                        result += "Working directory clean\n"
                    
                    result += "\nCommands: 'git commit message', 'git push', 'git status'"
                    return result
                    
                except subprocess.CalledProcessError:
                    return "Git Helper - Repository status unavailable"
                    
        except FileNotFoundError:
            return "Git not installed. Please install Git first."
        except Exception as e:
            return f"Git helper failed: {e}"
    
    def port_scanner(self, query=""):
        try:
            import threading
            import re
            from datetime import datetime
            
            # Extract target and port range
            target = "127.0.0.1"  # localhost default
            start_port = 1
            end_port = 1000
            
            # Parse target IP/hostname
            ip_match = re.search(r'scan\s+([\d\.]+|\w+\.\w+)', query.lower())
            if ip_match:
                target = ip_match.group(1)
            
            # Parse port range
            port_match = re.search(r'port[s]?\s+(\d+)(?:-(\d+))?', query.lower())
            if port_match:
                start_port = int(port_match.group(1))
                end_port = int(port_match.group(2)) if port_match.group(2) else start_port
            
            # Limit scan range for safety
            if end_port - start_port > 1000:
                end_port = start_port + 1000
            
            open_ports = []
            
            def scan_port(host, port):
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)
                    result = sock.connect_ex((host, port))
                    if result == 0:
                        open_ports.append(port)
                    sock.close()
                except:
                    pass
            
            # Start scanning
            start_time = datetime.now()
            threads = []
            
            for port in range(start_port, end_port + 1):
                thread = threading.Thread(target=scan_port, args=(target, port))
                threads.append(thread)
                thread.start()
                
                # Limit concurrent threads
                if len(threads) >= 50:
                    for t in threads:
                        t.join()
                    threads = []
            
            # Wait for remaining threads
            for thread in threads:
                thread.join()
            
            end_time = datetime.now()
            scan_duration = (end_time - start_time).total_seconds()
            
            # Common port services
            port_services = {
                21: "FTP", 22: "SSH", 80: "HTTP", 443: "HTTPS", 3389: "RDP"
            }
            
            result = f"🔍 Port Scanner Results\n"
            result += f"Target: {target}\n"
            result += f"Scanned: {start_port}-{end_port}\n"
            result += f"Duration: {scan_duration:.2f}s\n\n"
            
            if open_ports:
                result += f"Open Ports ({len(open_ports)} found):\n"
                for port in sorted(open_ports):
                    service = port_services.get(port, "Unknown")
                    result += f"  {port}/tcp - {service}\n"
            else:
                result += "No open ports found\n"
            
            return result
            
        except Exception as e:
            return f"🔍 Port scanner failed: {e}"
    
    def email_sender(self, query=""):
        try:
            import smtplib
            import re
            from email.mime.text import MIMEText
            
            # Parse email components
            to_match = re.search(r'(?:to|send)\s+([\w\.]+@[\w\.]+)', query.lower())
            subject_match = re.search(r'subject\s+(.+?)(?:\s+message|$)', query)
            message_match = re.search(r'message\s+(.+)$', query)
            
            if not to_match:
                return "📧 Usage: 'send email to user@example.com subject Hello message How are you?'"
            
            to_email = to_match.group(1)
            subject = subject_match.group(1) if subject_match else "Message from Jarvis"
            message = message_match.group(1) if message_match else "Hello from Jarvis!"
            
            return f"📧 Email configured:\nTo: {to_email}\nSubject: {subject}\nMessage: {message}\n\nNote: Configure SMTP settings to actually send emails"
            
        except Exception as e:
            return f"📧 Email sender failed: {e}"

new_features = NewFeatures()

def get_new_feature_response(query):
    return new_features.execute(query)