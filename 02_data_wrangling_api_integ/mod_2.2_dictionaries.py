'''
Your Task:

    Create a dictionary named ollama_payload with the following Key-Value pairs:

        Key: "model" | Value: "gemma4:26b"

        Key: "prompt" | Value: "Analyze TD visualizer network."

        Key: "stream" | Value: False

    Using the explicit key, extract and print() only the name of the model being requested.

    Mutate the dictionary: Overwrite the "stream" value from False to True.

    Mutate the dictionary: Add a brand new Key called "temperature" and assign it a Float value of 0.7.

    print() the entire ollama_payload dictionary to verify the mutations.
'''

ollama_payload = {
    "model": "gemma4:26b",
    "prompt": "Analyze TD visualizer network",
    "stream": False
}

print(ollama_payload["model"])

ollama_payload["stream"] = True
ollama_payload["temperature"] = 0.7

print(ollama_payload)