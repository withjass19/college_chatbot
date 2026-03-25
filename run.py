import json
import random
from flask import Flask, request, render_template, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

# -------- ChatBot Setup --------

chatbot = ChatBot(
    'My ChatBot',
    read_only=False,
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "Please type your inquiry.",
            "maximum_similarity_threshold": 0.90
        }
    ]
)

list_trainer = ListTrainer(chatbot)

# -------- Load Menu --------

with open("data/menu.json") as f:
    menu = json.load(f)

# -------- Load Intents --------

with open("data/intents.json") as file:
    intents = json.load(file)

# -------- Train Chatbot --------

for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        for response in intent["responses"]:
            list_trainer.train([pattern, response])

print("Training completed!")

# -------- User State --------

user_state = {}

# -------- Helper Function --------

def get_response_from_tag(tag):
    for intent in intents["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

    return "Sorry, I couldn't find information for that."

# -------- Routes --------

@app.route("/")
def home():
    return render_template("index.html")

# -------- Chat API --------

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    user_message = data.get("message", "").strip()

    user_id = "default_user"

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    # ---------- START CHAT ----------

    if user_message.lower() == "start":

        user_state[user_id] = menu["main"]

        return jsonify({
            "bot_messages": [
            "Hello!",
            "Welcome to PGGC11.",
            "Kindly choose from one of the following categories to get started."
        ],
            "options": list(menu["main"].keys())
        })

    # ---------- Initialize User State ----------

    if user_id not in user_state:
        user_state[user_id] = menu["main"]

    current_menu = user_state[user_id]

    # ---------- BACK BUTTON ----------

    if user_message.lower() == "back":

        user_state[user_id] = menu["main"]

        return jsonify({
            "bot": "Main Menu:",
            "options": list(menu["main"].keys())
        })

    # ---------- Menu Selection Handling ----------

    if isinstance(current_menu, dict) and user_message in current_menu:

        next_value = current_menu[user_message]

        if next_value == "other_inquiry":

            return jsonify({
                "bot": "If you cannot find your answer from the menu, please submit your query using the form below.",
                "options": ["Query Form", "Back"]
            })

        if isinstance(next_value, dict):

            user_state[user_id] = next_value

            return jsonify({
                "bot": f"You selected {user_message}. Please choose an option:",
                "options": list(next_value.keys()) + ["Back"]
            })

        else:

            response_text = get_response_from_tag(next_value)

            return jsonify({
                "bot": response_text,
                "options": ["Back"]
            })

    bot_response = chatbot.get_response(user_message)

    return jsonify({
        "bot": str(bot_response),
        "options": []
    })


@app.route("/submit_query", methods=["POST"])
def submit_query():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    message = data.get("message")

    print("Query Received:")
    print(name, email, phone, message)

    return jsonify({
        "status": "success",
        "message": "Query submitted successfully!"
    })


# -------- Run App --------

if __name__ == "__main__":
    app.run(debug=True)