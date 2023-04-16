# Define the knowledge base as a dictionary of rules
knowledge_base = {
    "What is your name?": "My name is ExpertBot.",
    "What is your purpose?": "I am an AI-based expert system designed to provide answers and solutions in a specific domain.",
    "What is the weather like today?": "I am sorry, I do not have access to real-time data. Please check a weather website or app.",
    "What is the capital of France?": "The capital of France is Paris.",
    "What is the square root of 16?": "The square root of 16 is 4.",
    "What is the color of the sky?": "The color of the sky appears blue during the day due to scattering of sunlight by the atmosphere.",
    "How do I solve a quadratic equation?": "To solve a quadratic equation of the form ax^2 + bx + c = 0, you can use the quadratic formula: x = (-b ± √(b^2 - 4ac)) / (2a)",
    "How do I bake a chocolate cake?": "To bake a chocolate cake, you will need ingredients such as flour, sugar, cocoa powder, eggs, butter, milk, and baking powder. You can find detailed recipes and instructions online or in a cookbook.",
    "What are the symptoms of a common cold?": "Common symptoms of a cold include a runny or stuffy nose, cough, sore throat, sneezing, congestion, and mild body aches. However, it's important to consult a healthcare professional for accurate diagnosis and advice.",
    "Default Response": "I am sorry, I do not have enough information to provide an answer.",
}

# Define the function to query the expert system
def query_expert_system(query):
    # Check if the query is in the knowledge base
    if query in knowledge_base:
        return knowledge_base[query]
    else:
        return knowledge_base["Default Response"]

# Example usage
query = input("Enter your query: ")
response = query_expert_system(query)
print(response)
