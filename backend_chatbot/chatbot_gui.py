#!/usr/bin/env python3
"""
Fitness Chatbot GUI - Simple Testing Interface
A user-friendly GUI for testing the fitness chatbot locally
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
import requests
import json
import threading
from datetime import datetime

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Fitness Chatbot - Testing GUI")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Configuration
        self.api_url = "http://localhost:5000"
        self.is_loading = False
        
        # Color scheme
        self.bg_color = "#f0f0f0"
        self.bot_color = "#e8f4f8"
        self.user_color = "#dff0d8"
        self.error_color = "#f2dede"
        
        self.setup_ui()
        self.check_server_status()
    
    def setup_ui(self):
        """Setup the user interface"""
        # Title
        title_frame = tk.Frame(self.root, bg="#2c3e50", height=60)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(
            title_frame, 
            text="🏋️ Fitness Chatbot GUI",
            font=("Arial", 18, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        title_label.pack(pady=10)
        
        # Server status
        self.status_frame = tk.Frame(self.root, bg=self.bg_color)
        self.status_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.status_label = tk.Label(
            self.status_frame,
            text="🔴 Server: Checking...",
            font=("Arial", 10),
            bg=self.bg_color
        )
        self.status_label.pack(side=tk.LEFT)
        
        # Category selection
        category_frame = tk.Frame(self.root, bg=self.bg_color)
        category_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(
            category_frame,
            text="Select Category:",
            font=("Arial", 10, "bold"),
            bg=self.bg_color
        ).pack(side=tk.LEFT, padx=5)
        
        self.category_var = tk.StringVar(value="chat")
        categories = [
            ("General Chat", "chat"),
            ("Fitness 💪", "fitness"),
            ("Health ❤️", "health"),
            ("Diet 🥗", "diet"),
            ("Food 🍗", "food")
        ]
        
        for label, value in categories:
            tk.Radiobutton(
                category_frame,
                text=label,
                variable=self.category_var,
                value=value,
                bg=self.bg_color,
                font=("Arial", 9)
            ).pack(side=tk.LEFT, padx=5)
        
        # Chat display
        chat_label = tk.Label(
            self.root,
            text="Chat History:",
            font=("Arial", 11, "bold"),
            bg=self.bg_color
        )
        chat_label.pack(anchor=tk.W, padx=10, pady=(10, 2))
        
        self.chat_display = scrolledtext.ScrolledText(
            self.root,
            height=18,
            width=100,
            font=("Segoe UI", 10),
            bg="white",
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.chat_display.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        # Configure text tags for styling
        self.chat_display.tag_configure("user", foreground="#0066cc", font=("Segoe UI", 10, "bold"))
        self.chat_display.tag_configure("bot", foreground="#009900", font=("Segoe UI", 10))
        self.chat_display.tag_configure("error", foreground="#cc0000", font=("Segoe UI", 10))
        self.chat_display.tag_configure("time", foreground="#999999", font=("Segoe UI", 8))
        
        # Input section
        input_label = tk.Label(
            self.root,
            text="Your Message:",
            font=("Arial", 10, "bold"),
            bg=self.bg_color
        )
        input_label.pack(anchor=tk.W, padx=10, pady=(5, 2))
        
        input_frame = tk.Frame(self.root, bg=self.bg_color)
        input_frame.pack(padx=10, pady=5, fill=tk.X)
        
        self.input_text = tk.Entry(
            input_frame,
            font=("Arial", 10),
            width=70
        )
        self.input_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        self.input_text.bind("<Return>", lambda e: self.send_message())
        
        self.send_button = tk.Button(
            input_frame,
            text="Send",
            command=self.send_message,
            font=("Arial", 10, "bold"),
            bg="#0066cc",
            fg="white",
            width=10,
            cursor="hand2"
        )
        self.send_button.pack(side=tk.LEFT, padx=2)
        
        self.clear_button = tk.Button(
            input_frame,
            text="Clear",
            command=self.clear_chat,
            font=("Arial", 10),
            bg="#999999",
            fg="white",
            width=10,
            cursor="hand2"
        )
        self.clear_button.pack(side=tk.LEFT, padx=2)
        
        # Quick buttons
        quick_frame = tk.LabelFrame(
            self.root,
            text="Quick Test Queries",
            font=("Arial", 10, "bold"),
            bg=self.bg_color,
            padx=10,
            pady=5
        )
        quick_frame.pack(padx=10, pady=5, fill=tk.X)
        
        quick_buttons = [
            ("Beginner Workout", "What is a good beginner workout?"),
            ("Sleep Tips", "How many hours of sleep do I need?"),
            ("Weight Loss", "What should I eat for weight loss?"),
            ("Chicken Nutrition", "How many calories in chicken?"),
            ("Stress Relief", "How to manage stress?"),
            ("High Protein Foods", "What are high protein foods?")
        ]
        
        for i, (label, query) in enumerate(quick_buttons):
            btn = tk.Button(
                quick_frame,
                text=label,
                command=lambda q=query: self.send_quick_query(q),
                font=("Arial", 8),
                width=20,
                bg="#4CAF50",
                fg="white",
                cursor="hand2"
            )
            row = i // 3
            col = i % 3
            btn.grid(row=row, column=col, padx=3, pady=3)
    
    def check_server_status(self):
        """Check if the server is running"""
        try:
            response = requests.get(f"{self.api_url}/health", timeout=2)
            if response.status_code == 200:
                self.status_label.config(
                    text="🟢 Server: Connected",
                    fg="#009900"
                )
                self.send_button.config(state=tk.NORMAL)
                return True
        except:
            pass
        
        self.status_label.config(
            text="🔴 Server: Not Running (Start backend with 'python app.py')",
            fg="#cc0000"
        )
        self.send_button.config(state=tk.DISABLED)
        return False
    
    def send_message(self):
        """Send message to chatbot"""
        message = self.input_text.get().strip()
        
        if not message:
            messagebox.showwarning("Warning", "Please enter a message")
            return
        
        if self.is_loading:
            messagebox.showinfo("Info", "Please wait for the response...")
            return
        
        # Display user message
        self.display_message(f"You ({self.get_time()})", message, "user")
        self.input_text.delete(0, tk.END)
        
        # Send in thread to prevent UI freezing
        self.is_loading = True
        self.send_button.config(state=tk.DISABLED)
        
        thread = threading.Thread(target=self._send_to_api, args=(message,))
        thread.daemon = True
        thread.start()
    
    def _send_to_api(self, message):
        """Send message to API (in separate thread)"""
        try:
            endpoint = self.category_var.get()
            url = f"{self.api_url}/api/{endpoint}"
            
            payload = {
                "message": message,
                "user_id": "test_user"
            }
            
            response = requests.post(
                url,
                json=payload,
                timeout=30,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code in [200, 400]:
                data = response.json()
                bot_message = data.get("message", "No response")
                
                # Display response
                self.display_message(f"Bot ({self.get_time()})", bot_message, "bot")
                
                # Show metadata if available
                if data.get("data"):
                    friendly_metadata = self.format_metadata(data.get("data"))
                    if friendly_metadata:
                        self.display_message("Details", friendly_metadata, "bot")
                
            else:
                self.display_message("Error", f"Server error: {response.status_code}", "error")
                
        except requests.exceptions.Timeout:
            self.display_message("Error", "Request timeout - server may not be responding", "error")
        except requests.exceptions.ConnectionError:
            self.display_message("Error", "Cannot connect to server. Is it running?", "error")
        except Exception as e:
            self.display_message("Error", str(e), "error")
        
        finally:
            self.is_loading = False
            self.send_button.config(state=tk.NORMAL)
    
    def send_quick_query(self, query):
        """Send a quick query"""
        self.input_text.delete(0, tk.END)
        self.input_text.insert(0, query)
        self.send_message()
    
    def display_message(self, sender, message, msg_type="bot"):
        """Display message in chat window"""
        self.chat_display.config(state=tk.NORMAL)
        
        # Add sender
        self.chat_display.insert(tk.END, f"\n{sender}: ", ("user" if msg_type == "user" else "time"))
        
        # Add message
        tag = "user" if msg_type == "user" else ("error" if msg_type == "error" else "bot")
        self.chat_display.insert(tk.END, f"{message}\n", tag)
        
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)
    
    def clear_chat(self):
        """Clear chat history"""
        if messagebox.askyesno("Confirm", "Clear all chat history?"):
            self.chat_display.config(state=tk.NORMAL)
            self.chat_display.delete(1.0, tk.END)
            self.chat_display.config(state=tk.DISABLED)

    def format_metadata(self, data):
        """Convert response metadata into readable text"""
        if isinstance(data, dict):
            # Skip verbose knowledge-base dumps that look like code.
            noisy_keys = {"common_questions", "myths_debunked", "red_flags"}
            if any(key in data for key in noisy_keys):
                return "Tip: Ask a focused follow-up like '10-day diet plan', 'diet consistency tips', or 'high protein foods'."

            lines = []
            for idx, (key, value) in enumerate(data.items()):
                if idx >= 8:
                    lines.append("… more details available")
                    break
                label = key.replace("_", " ").title()
                if isinstance(value, dict):
                    lines.append(f"{label}:")
                    for sub_idx, (sub_key, sub_value) in enumerate(value.items()):
                        if sub_idx >= 4:
                            lines.append("  • …")
                            break
                        sub_label = sub_key.replace("_", " ").title()
                        lines.append(f"  • {sub_label}: {self._short_value(sub_value)}")
                elif isinstance(value, list):
                    lines.append(f"{label}: {', '.join(str(item) for item in value[:6])}")
                else:
                    lines.append(f"{label}: {value}")
            return "\n".join(lines)

        return str(data)

    def _short_value(self, value):
        """Shorten long metadata values for display"""
        if isinstance(value, list):
            text = ", ".join(str(item) for item in value[:6])
            return text[:180] + ("..." if len(text) > 180 else "")
        if isinstance(value, dict):
            text = ", ".join(f"{k}: {v}" for k, v in list(value.items())[:4])
            return text[:180] + ("..." if len(text) > 180 else "")
        text = str(value)
        return text[:180] + ("..." if len(text) > 180 else "")
    
    def get_time(self):
        """Get current time in HH:MM:SS format"""
        return datetime.now().strftime("%H:%M:%S")


def main():
    """Main function"""
    root = tk.Tk()
    app = ChatbotGUI(root)
    
    # Show welcome message
    root.after(500, lambda: app.display_message(
        "Bot",
        "Welcome to Fitness Chatbot! 🏋️\n"
        "Select a category, type your question, and press Send or Enter.\n"
        "You can also use the Quick Test Queries buttons below.\n"
        "Ask me about fitness, health, diet, or food!",
        "bot"
    ))
    
    root.mainloop()


if __name__ == "__main__":
    main()
