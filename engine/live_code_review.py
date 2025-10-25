import threading
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class CodeReviewHandler(FileSystemEventHandler):
    def __init__(self, dual_ai_instance):
        self.dual_ai = dual_ai_instance
        self.last_check = {}
        self.corrected_files = {}
    
    def on_modified(self, event):
        if event.is_directory:
            return
        
        code_extensions = ['.py', '.js', '.java', '.cpp', '.c', '.cs', '.php', '.rb', '.go', '.rs', '.kt', '.swift', '.ts', '.jsx', '.tsx', '.vue', '.html', '.css', '.sql', '.sh', '.bat']
        if not any(event.src_path.endswith(ext) for ext in code_extensions):
            return
        
        current_time = time.time()
        if event.src_path in self.last_check:
            if current_time - self.last_check[event.src_path] < 0.5:
                return
        
        self.last_check[event.src_path] = current_time
        
        # Clear correction flag after 30 seconds
        if event.src_path in self.corrected_files:
            if current_time - self.corrected_files[event.src_path] > 30:
                del self.corrected_files[event.src_path]
        
        try:
            with open(event.src_path, 'r', encoding='utf-8') as f:
                code = f.read()
            
            if len(code.strip()) < 10:
                return
            
            lines = code.split('\n')
            numbered_code = '\n'.join([f'{i+1}: {line}' for i, line in enumerate(lines)])
            
            file_ext = os.path.splitext(event.src_path)[1]
            lang_map = {
                '.py': 'Python', '.js': 'JavaScript', '.java': 'Java', '.cpp': 'C++', '.c': 'C',
                '.cs': 'C#', '.php': 'PHP', '.rb': 'Ruby', '.go': 'Go', '.rs': 'Rust',
                '.kt': 'Kotlin', '.swift': 'Swift', '.ts': 'TypeScript', '.jsx': 'React JSX',
                '.tsx': 'React TSX', '.vue': 'Vue.js', '.html': 'HTML', '.css': 'CSS',
                '.sql': 'SQL', '.sh': 'Shell', '.bat': 'Batch'
            }
            language = lang_map.get(file_ext, 'Code')
            
            prompt = f'''Analyze this {language} code for errors:\n{numbered_code}\n\nCheck for:\n- Syntax errors\n- Undefined variables\n- Missing imports\n- Logic errors\n- Indentation issues\n\nIf you find ANY error, respond with: "Line X: [specific error description]"\nIf no errors found, respond with: "Code looks good"'''
            
            if self.dual_ai.ai_provider == 'groq':
                response = self.dual_ai.groq_client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="llama-3.1-8b-instant"
                )
                result = response.choices[0].message.content.strip()
            else:
                response = self.dual_ai.gemini_model.generate_content(prompt)
                result = response.text.strip()
            
            error_indicators = ['error', 'undefined', 'not defined', 'syntax', 'invalid', 'missing', 'unexpected', 'indentation', 'line', 'fix', 'should be', 'change', 'incorrect', 'wrong']
            has_error = any(indicator in result.lower() for indicator in error_indicators)
            
            if has_error and event.src_path not in self.corrected_files:
                self._show_error_notification(event.src_path, result)
        
        except Exception as e:
            pass
    
    def _show_error_notification(self, file_path, error_message):
        title = f"Code Error in {os.path.basename(file_path)}"
        if self._ask_for_correction(title, error_message):
            self._auto_correct_code(file_path, error_message)
        else:
            self._show_notification(title, error_message)
    
    def _ask_for_correction(self, title, message):
        try:
            import tkinter as tk
            from tkinter import messagebox
            
            root = tk.Tk()
            root.withdraw()
            result = messagebox.askyesno(
                "Auto-Correction", 
                f"{title}\n\n{message[:200]}...\n\nWould you like to auto-correct this error?",
                icon='warning'
            )
            root.destroy()
            return result
        except:
            return False
    
    def _auto_correct_code(self, file_path, error_message):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                original_code = f.read()
            
            correction_prompt = f'''Fix this code error. Return ONLY the corrected code without explanations:\n\nOriginal code:\n{original_code}\n\nError: {error_message}\n\nCorrected code:'''
            
            if self.dual_ai.ai_provider == 'groq':
                response = self.dual_ai.groq_client.chat.completions.create(
                    messages=[{"role": "user", "content": correction_prompt}],
                    model="llama-3.1-8b-instant",
                    temperature=0.1
                )
                corrected_code = response.choices[0].message.content.strip()
            else:
                response = self.dual_ai.gemini_model.generate_content(correction_prompt)
                corrected_code = response.text.strip()
            
            # Clean AI response
            if corrected_code.startswith('```'):
                lines = corrected_code.split('\n')
                corrected_code = '\n'.join(lines[1:-1])
            
            # Create backup
            import datetime
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_path = f"{file_path}.backup_{timestamp}"
            
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(original_code)
            
            # Apply correction
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(corrected_code)
            
            # Mark as corrected
            self.corrected_files[file_path] = time.time()
            
            self._show_notification("Auto-Correction Complete", f"✅ Code fixed in {os.path.basename(file_path)}\n📁 Backup: {os.path.basename(backup_path)}")
        
        except Exception as e:
            self._show_notification("Auto-Correction Failed", f"❌ Could not fix: {str(e)}")
    
    def _show_notification(self, title, message):
        try:
            import win10toast
            toaster = win10toast.ToastNotifier()
            toaster.show_toast(title, message, duration=5, threaded=True)
        except:
            try:
                import tkinter as tk
                import threading
                
                def show_toast():
                    root = tk.Tk()
                    root.overrideredirect(True)
                    root.attributes('-topmost', True)
                    root.configure(bg='#1e1e1e')
                    
                    width, height = 350, 120
                    screen_width = root.winfo_screenwidth()
                    screen_height = root.winfo_screenheight()
                    x = screen_width - width - 10
                    y = screen_height - height - 40
                    root.geometry(f'{width}x{height}+{x}+{y}')
                    
                    tk.Label(root, text=title, bg='#1e1e1e', fg='white', font=('Arial', 10, 'bold')).pack(pady=5)
                    tk.Label(root, text=message[:100], bg='#1e1e1e', fg='#cccccc', font=('Arial', 9), wraplength=320).pack(pady=5)
                    
                    root.after(4000, root.destroy)
                    root.mainloop()
                
                threading.Thread(target=show_toast, daemon=True).start()
            except:
                print(f"🚨 {title}: {message}")

def start_live_code_review(dual_ai_instance):
    try:
        observer = Observer()
        handler = CodeReviewHandler(dual_ai_instance)
        observer.schedule(handler, '.', recursive=True)
        observer.start()
        return observer, "Live code review started - monitoring all code files for errors"
    except Exception as e:
        return None, f"Live code review error: {str(e)}"