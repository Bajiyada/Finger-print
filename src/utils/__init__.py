def log_message(message):
    print(f"[LOG] {message}")

def load_config(file_path):
    import json
    with open(file_path, 'r') as f:
        return json.load(f)