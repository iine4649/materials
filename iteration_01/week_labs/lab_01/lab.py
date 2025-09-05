'''

Week 01 Lab : Advanced Level
Due Date: Sunday 9/7 @ midnight

    Objective: Build an interactive program that practices input/output, conditionals, data structures, and introduces a new
               tool/library (GUI or formatted output). The program should take user information and present it in a polished, 
               engaging way.

    Requirements: GUI or Rich Input/Output. A simple GUI toolkit (tkinter/turtle, or PyQt if you already know tkinter). Or a terminal UI
               library (rich or textual) for nicely formatted text. Collect the same base data as the beginner assignment.

               
    - Create a program that asks the user for their...

        - Name
        - Age
        - Multilingual status

    - Program should accomplish the set of criteria listed below

        1. For age rules, instead of just printing messages, display a progression of privileges (driving, voting, renting a car, etc.)
          in a formatted way (e.g., a list, progress bar, or GUI checkboxes).
        2. Language handling. If multilingual, ask for all the languages. Store them in a data structure and display them nicely (for example, in a
            sorted list, or with flags/emojis if using rich).
        3. If not multilingual, ask for a desired language and display a "learning plan" (could just be a fun random tip or suggested practice hours generated in code).

    - Bonus Challenges (optional but encouraged):
        1. Write user data to a JSON file so that the program "remembers" users between runs.
        2. Translate a greeting into one of the listed languages using a library like googletrans.
        3. Use datetime to estimate what year the user can vote, rent a car, or retire.
        

'''

import tkinter as tk
from tkinter import ttk, messagebox
import json
import datetime
import random
import os
import asyncio
import time
try:
    import googletrans  # type: ignore
    from googletrans import Translator  # type: ignore
except Exception:  #
    googletrans = None  # type: ignore
    Translator = None  

class LanguageLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Learning App")
        self.root.geometry("800x700")
        self.root.configure(bg='#f0f0f0')
        
        # Data file path
        self.data_file = "user_data.json"
        
        # User data
        self.user_data = self.load_user_data()
        
        # Age privileges
        self.age_privileges = {
            16: "Drivers License",
            18: "Voting Rights",
            21: "Car Rental",
            25: "Insurance Discount",
            65: "Retirement"
        }
        
        # Language learning tips
        self.language_tips = {
            "English": ["Listen to English music", "Watch movies with English subtitles", "Take online English lessons"],
            "Spanish": ["Listen to Spanish music", "Learn with Duolingo", "Make friends in Spanish-speaking countries"],
            "French": ["Read French news", "Read French recipes", "Listen to French podcasts"],
            "German": ["Learn German grammar", "Watch German movies", "Read German literature"],
            "Chinese": ["Practice writing Chinese characters", "Sing Chinese songs", "Watch Chinese dramas"],
            "Japanese": ["Learn Hiragana and Katakana", "Watch anime with Japanese subtitles", "Sing Japanese songs"]
        }
        
        
        self.translator = Translator()
        self.lang_name_to_code = {name.title(): code for code, name in googletrans.LANGUAGES.items()}
        '''
        except Exception:
            self.translator = None
            self.lang_name_to_code = {}
        '''
        self.create_widgets()
        
        # If there is saved user, display it
        if self.user_data:
            self.display_saved_user()
    
    def load_user_data(self):
        """Load saved user data"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Data loading error: {e}")
        return {}
    
    def save_user_data(self):
        """Save user data to JSON file"""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.user_data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Data saving error: {e}")
    
    def create_widgets(self):
        """Create widgets"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="🌍 Language Learning App", 
                               font=('Arial', 24, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Name input
        ttk.Label(main_frame, text="Name:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.name_entry = ttk.Entry(main_frame, width=30)
        self.name_entry.grid(row=1, column=1, sticky=tk.W, pady=5)
        
        # Age input
        ttk.Label(main_frame, text="Age:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.age_entry = ttk.Entry(main_frame, width=30)
        self.age_entry.grid(row=2, column=1, sticky=tk.W, pady=5)
        
        # Multilingual status
        ttk.Label(main_frame, text="Are you multilingual?").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.multilingual_var = tk.BooleanVar()
        multilingual_check = ttk.Checkbutton(main_frame, text="Yes", variable=self.multilingual_var,
                                           command=self.toggle_language_input)
        multilingual_check.grid(row=3, column=1, sticky=tk.W, pady=5)
        
        
        self.language_frame = ttk.LabelFrame(main_frame, text="Language Information", padding="10")
        self.language_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        # If multilingual
        ttk.Label(self.language_frame, text="Spoken Languages (comma separated):").grid(row=0, column=0, sticky=tk.W)
        self.languages_entry = ttk.Entry(self.language_frame, width=40)
        self.languages_entry.grid(row=0, column=1, sticky=tk.W, pady=5)
        
        # If not multilingual
        ttk.Label(main_frame, text="Desired Language:").grid(row=4, column=0, sticky=tk.W)
        self.desired_language = ttk.Combobox(main_frame, 
                                           values=list(self.language_tips.keys()), width=20)
        self.desired_language.grid(row=4, column=1, sticky=tk.W, pady=5)
        
        # Hide
        self.language_frame.grid_remove()
        
        # Submit Button
        submit_btn = ttk.Button(main_frame, text="Send Information", command=self.process_user_info)
        submit_btn.grid(row=6, column=0, columnspan=2, pady=20)
        
        #
        self.result_frame = ttk.LabelFrame(main_frame, text="Results", padding="10")
        self.result_frame.grid(row=7, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        
        self.result_text = tk.Text(self.result_frame, height=15, width=70, wrap=tk.WORD)
        self.result_text.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        
        scrollbar = ttk.Scrollbar(self.result_frame, orient=tk.VERTICAL, command=self.result_text.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.result_text.configure(yscrollcommand=scrollbar.set)
        
        # Saved user display button
        if self.user_data:
            saved_btn = ttk.Button(main_frame, text="Display Saved User", 
                                 command=self.display_saved_user)
            saved_btn.grid(row=8, column=0, columnspan=2, pady=10)
    
    def toggle_language_input(self):
        """Toggle language input field based on multilingual checkbox status"""
        if self.multilingual_var.get():
            self.language_frame.grid()
            self.languages_entry.focus()
        else:
            self.language_frame.grid_remove()
    
    def process_user_info(self):
        """Process user information"""
        try:
            name = self.name_entry.get().strip()
            age = int(self.age_entry.get().strip())
            
            if not name:
                messagebox.showerror("Error", "Please enter your name")
                return
            
            if age <= 0 or age > 150:
                messagebox.showerror("Error", "Please enter a valid age")
                return
            
            # User Info
            user_info = {
                "name": name,
                "age": age,
                "multilingual": self.multilingual_var.get(),
                "timestamp": datetime.datetime.now().isoformat()
            }
            
            if self.multilingual_var.get():
                languages = [lang.strip() for lang in self.languages_entry.get().split(',') if lang.strip()]
                user_info["languages"] = languages
            else:
                desired_lang = self.desired_language.get()
                if desired_lang:
                    user_info["desired_language"] = desired_lang
            
            # Save data
            self.user_data[name] = user_info
            self.save_user_data()
            
            # Display results
            self.display_results(user_info)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter your age as a number")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def _translate_sync(self, text: str, dest_code: str) -> str | None:
        time.sleep(0.5)  
        if not self.translator or not dest_code:
            return None
        try:
            r = self.translator.translate(text, dest=dest_code)
            if asyncio.iscoroutine(r):
                r = asyncio.run(r)
            return getattr(r, "text", None)
        except Exception:
            return None
    
    def display_results(self, user_info):
        """Display results"""
        self.result_text.delete(1.0, tk.END)
        
        result = f"Hello、{user_info['name']}！\n\n"
        
        
        result += "Age Privileges Checklist:\n"
        result += "=" * 40 + "\n"
        
        current_age = user_info['age']
        for age_limit, privilege in sorted(self.age_privileges.items()):
            if current_age >= age_limit:
                result += f"✅ {age_limit} years old: {privilege}\n"
            else:
                years_until = age_limit - current_age
                target_year = datetime.datetime.now().year + years_until
                result += f"⏳ {age_limit} years old: {privilege} (in {years_until} years, {target_year} years)\n"
        
        result += "\n"
        
        #
        if user_info['multilingual']:
            languages = user_info.get('languages', [])
            if languages:
                
                for lang in languages:
                
                    code = self.lang_name_to_code.get(str(lang).title())
                    greeting_text = self._translate_sync("Hello!", code)  #or fallback_greetings.get(str(lang).title(), "Hello!")
                    result += f"   {lang}: {greeting_text}\n"

        else:
            desired_lang = user_info.get('desired_language', '')
            if desired_lang:
                result += f"Learning Goal Language: {desired_lang}\n\n"
                result += "Learning Plan:\n"
                result += "=" * 30 + "\n"
                
                if desired_lang in self.language_tips:
                    tips = self.language_tips[desired_lang]
                    for i, tip in enumerate(tips, 1):
                        result += f"{i}. {tip}\n"
                    
                    # Calculation of recommended learning time
                    recommended_hours = random.randint(3, 8)
                    result += f"\nRecommended weekly learning time: {recommended_hours} hours\n"
                    result += f"Target completion date: {datetime.datetime.now().year + random.randint(1, 3)} years\n"
        
        self.result_text.insert(1.0, result)
    
    def display_saved_user(self):
        """Display saved user information"""
        if not self.user_data:
            return
        
        
        latest_user = max(self.user_data.values(), key=lambda x: x['timestamp'])
        self.display_results(latest_user)
        
        
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, latest_user['name'])
        
        self.age_entry.delete(0, tk.END)
        self.age_entry.insert(0, str(latest_user['age']))
        
        self.multilingual_var.set(latest_user['multilingual'])
        
        if latest_user['multilingual']:
            self.language_frame.grid()
            self.languages_entry.delete(0, tk.END)
            if 'languages' in latest_user:
                self.languages_entry.insert(0, ', '.join(latest_user['languages']))
        else:
            self.language_frame.grid_remove()
            if 'desired_language' in latest_user:
                self.desired_language.set(latest_user['desired_language'])

def main():
    """Main function"""
    root = tk.Tk()
    app = LanguageLearningApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 