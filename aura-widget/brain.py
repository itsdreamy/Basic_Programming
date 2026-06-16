import ollama
import pyperclip

class AIBrain:
    def __init__(self):
        # Keeps track of the chat history so the AI remembers context
        self.conversation_history = [
            {"role": "system", "content": "You are AURA, a sleek, brilliant desktop AI companion. Be concise, clever, and highly helpful."}
        ]

    def get_clipboard_text(self):
        """Grabs whatever text is currently copied on the user's PC."""
        try:
            return pyperclip.paste().strip()
        except Exception:
            return ""

    def process_response(self, user_input, include_clipboard=False):
        """Sends the prompt to Ollama and returns the AI's response."""
        try:
            # If requested, inject clipboard data into the prompt automatically
            if include_clipboard:
                clipboard_content = self.get_clipboard_text()
                if clipboard_content:
                    user_input = f"{user_input}\n\n[Context from Clipboard]:\n{clipboard_content}"

            # Append user message to memory
            self.conversation_history.append({"role": "user", "content": user_input})

            # Call local Ollama engine
            response = ollama.chat(
                model='llama3.2:3b',
                messages=self.conversation_history
            )

            ai_reply = response['message']['content']
            
            # Append AI reply to memory
            self.conversation_history.append({"role": "assistant", "content": ai_reply})
            return ai_reply

        except Exception as e:
            return f"Error connecting to AI engine: {str(e)}"