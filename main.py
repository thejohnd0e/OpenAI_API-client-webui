import os
import json
from openai import OpenAI
import gradio as gr


# Functions for working with settings
def load_settings(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading settings: {str(e)}")
        return {}


def save_settings(settings, file_name):
    file_path = os.path.join("settings", f"{file_name}.json")
    os.makedirs("settings", exist_ok=True)
    with open(file_path, 'w') as f:
        json.dump(settings, f)
    return file_path


def get_saved_profiles():
    if not os.path.exists("settings"):
        return []
    return [f.split('.')[0] for f in os.listdir("settings") if f.endswith('.json')]


# Function to create OpenAI client
def create_client(api_key, base_url):
    return OpenAI(api_key=api_key, base_url=base_url)


# Function to process chat messages
def chat_with_ai(message, history, api_key, base_url, model, max_tokens, temperature, top_p, presence_penalty,
                 frequency_penalty, system_prompt):
    client = create_client(api_key, base_url)

    messages = [{"role": "system", "content": system_prompt}]
    for human, ai in history:
        messages.append({"role": "user", "content": human})
        if ai:
            messages.append({"role": "assistant", "content": ai})
    messages.append({"role": "user", "content": message})

    try:
        stream = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            presence_penalty=presence_penalty,
            frequency_penalty=frequency_penalty,
            stream=True
        )
        return stream, None
    except Exception as e:
        return None, f"An error occurred: {str(e)}"


# Creating Gradio interface
with gr.Blocks(css="#chatbot { height: 70vh !important; }") as demo:
    gr.Markdown("# OpenAI_API-client-webui")

    with gr.Row():
        with gr.Column(scale=4):
            chatbot = gr.Chatbot(label="Dialogue", elem_id="chatbot")
            msg = gr.Textbox(label="Enter a message", placeholder="Type your message here...")
            with gr.Row():
                clear = gr.Button("Clear")
                submit = gr.Button("Submit", variant="primary")

        with gr.Column(scale=1):
            with gr.Accordion("Settings", open=False):
                api_key = gr.Textbox(label="API Key", type="password")
                base_url = gr.Textbox(label="Base URL", value="https://api.together.xyz/v1")
                model = gr.Textbox(label="Model", value="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo")
                system_prompt = gr.Textbox(label="System Prompt", value="You are a helpful assistant.", lines=3)
                max_tokens = gr.Slider(minimum=1, maximum=2048, value=512, step=1, label="Max Tokens")
                temperature = gr.Slider(minimum=0, maximum=2, value=0.7, step=0.01, label="Temperature")
                top_p = gr.Slider(minimum=0, maximum=1, value=0.7, step=0.01, label="Top P")
                presence_penalty = gr.Slider(minimum=-2, maximum=2, value=0, step=0.01, label="Presence Penalty")
                frequency_penalty = gr.Slider(minimum=-2, maximum=2, value=0, step=0.01, label="Frequency Penalty")

                gr.Markdown("### Settings Profile Management")
                profile_name = gr.Textbox(label="Profile name to save")
                save_button = gr.Button("Save current settings")
                profiles_dropdown = gr.Dropdown(label="Select profile to load", choices=get_saved_profiles())
                load_button = gr.Button("Load selected profile")

    examples = gr.Examples(
        examples=[
            "Hello! How are you?",
            "Tell me about machine learning",
            "What's the weather like today?"
        ],
        inputs=msg
    )


    def user(user_message, history):
        return "", history + [[user_message, None]]


    def bot(history, api_key, base_url, model, max_tokens, temperature, top_p, presence_penalty, frequency_penalty,
            system_prompt):
        user_message = history[-1][0]
        stream, error = chat_with_ai(user_message, history[:-1], api_key, base_url, model, max_tokens, temperature,
                                     top_p, presence_penalty, frequency_penalty, system_prompt)

        if error:
            history[-1][1] = error
            yield history
            return

        bot_message = ""
        try:
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    bot_message += chunk.choices[0].delta.content
                    history[-1][1] = bot_message
                    yield history
        except Exception as e:
            history[-1][1] = f"Error processing response: {str(e)}"
            yield history


    def on_submit(message, chat_history, api_key, base_url, model, max_tokens, temperature, top_p, presence_penalty,
                  frequency_penalty, system_prompt):
        user_message, history = user(message, chat_history)
        for updated_history in bot(history, api_key, base_url, model, max_tokens, temperature, top_p, presence_penalty,
                                   frequency_penalty, system_prompt):
            yield "", updated_history


    def save_current_settings(profile_name, api_key, base_url, model, system_prompt, max_tokens, temperature, top_p,
                              presence_penalty, frequency_penalty):
        settings = {
            "api_key": api_key,
            "base_url": base_url,
            "model": model,
            "system_prompt": system_prompt,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "presence_penalty": presence_penalty,
            "frequency_penalty": frequency_penalty
        }
        save_settings(settings, profile_name)
        return gr.update(choices=get_saved_profiles())


    def load_selected_profile(profile):
        if not profile:
            return [gr.update() for _ in range(9)]
        try:
            settings = load_settings(os.path.join("settings", f"{profile}.json"))
            return [
                gr.update(value=settings.get("api_key", "")),
                gr.update(value=settings.get("base_url", "")),
                gr.update(value=settings.get("model", "")),
                gr.update(value=settings.get("system_prompt", "You are a helpful assistant.")),
                gr.update(value=settings.get("max_tokens", 512)),
                gr.update(value=settings.get("temperature", 0.7)),
                gr.update(value=settings.get("top_p", 0.7)),
                gr.update(value=settings.get("presence_penalty", 0)),
                gr.update(value=settings.get("frequency_penalty", 0))
            ]
        except Exception as e:
            print(f"Error loading profile: {str(e)}")
            return [gr.update() for _ in range(9)]


    save_button.click(
        save_current_settings,
        inputs=[profile_name, api_key, base_url, model, system_prompt, max_tokens, temperature, top_p, presence_penalty,
                frequency_penalty],
        outputs=[profiles_dropdown]
    )

    load_button.click(
        load_selected_profile,
        inputs=[profiles_dropdown],
        outputs=[api_key, base_url, model, system_prompt, max_tokens, temperature, top_p, presence_penalty,
                 frequency_penalty]
    )

    clear.click(lambda: None, None, chatbot, queue=False)

    submit.click(on_submit,
                 inputs=[msg, chatbot, api_key, base_url, model, max_tokens, temperature, top_p, presence_penalty,
                         frequency_penalty, system_prompt],
                 outputs=[msg, chatbot])
    msg.submit(on_submit,
               inputs=[msg, chatbot, api_key, base_url, model, max_tokens, temperature, top_p, presence_penalty,
                       frequency_penalty, system_prompt],
               outputs=[msg, chatbot])

# Launch the application
if __name__ == "__main__":
    demo.launch()