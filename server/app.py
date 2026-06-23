from flask import Flask

app = Flask(__name__)

# Given models
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

# Default route
@app.route("/")
def home():
    return "Welcome to Flatiron Cars"

# Model route
@app.route("/<model>")
def get_model(model):
    # Make comparison case-insensitive
    formatted_model = model.lower()

    # Normalize list for comparison
    normalized_models = [m.lower() for m in existing_models]

    if formatted_model in normalized_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog"


if __name__ == "__main__":
    app.run(debug=True)