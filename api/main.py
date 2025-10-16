
import random
# FastAPI is a Python library that 
# allows us to 
# - take in a request (typically sent from the client)
# - send back a response
from fastapi import FastAPI

# CORS (Cross-Origin Resource Sharing)
# allows us to restrict/enable which
# client urls are allowed to call 
# this backend code. 
# CORS is part of the FastAPI library.
from fastapi.middleware.cors import CORSMiddleware

# 1. Data Source (In-Memory List)
# This list simulates a simple, pre-defined dataset.
FOOD_CHOICES = [
    "Pizza 🍕",
    "Tacos 🌮",
    "Sushi 🍣",
    "Classic Burger 🍔",
    "Thai Curry 🌶️",    
    "Grilled Cheese & Tomato 🍅",
    "Chicken Shawarma 🐔",
    "Vegan Bowl 🥗",
    "Pho Noodle Soup 🍲"
]
# Initialize the FastAPI application
app = FastAPI(
    title="FastAPI Example",
    description="This is an example of using FastAPI"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # star means all client urls allowed 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")           #endpoint, or route, always starts with a forward slash
def default_route():    #route handler function
    """
    This is the default endpoint for this back-end.
    """
    return "You have reached the default route. Back-end server is listening..."
    
@app.get("/example")  
def get_example():    
    """
    This endpoint returns a JSON object consisting of a simple message.
    """
    return {"message": "Hello World!","year":2025}

@app.get("/example2")  
def get_example2(name):    # can also pass in parameters
    """
    This endpoint takes in a parameter called "name"
    """
    return {"message": f"Hello {name}!"}

# When a user sends a GET request to '/random-choice', this function runs.
@app.get("/random-choice")
def get_random_food_choice():
    """
    Returns a single random food choice from the FOOD_CHOICES list.
    """
    # Use the built-in Python 'random' module to pick one item.
    selected_choice = random.choice(FOOD_CHOICES)
    
    # Return a Python dictionary, which FastAPI converts to a JSON response.
    return {"status": "success", "choice": selected_choice}

    @app.get("/my-choice/")
def get_my_food_choice(choice):    
    # convert to integer
    choiceNumber = int(choice)

    # check if choice is a valid index i.e. between 0 and length of list
    if choiceNumber >= 0 and choiceNumber < len(FOOD_CHOICES):
      # Use the passed in choice number; passed in as query parameter
      selected_choice = FOOD_CHOICES[choiceNumber]
    
      # Return a Python dictionary, which FastAPI converts to a JSON response.     
      return {"status": "success", "choice": selected_choice}
    else:
      return {"status": "error", "message": f"invalid choice:{choice}"}  


@app.get("/alternative-choice/{choice}")
def get_my_alt_choice(choice):    
    # convert to integer
    choiceNumber = int(choice)

    # check if choice is a valid index i.e. between 0 and length of list
    if choiceNumber >= 0 and choiceNumber < len(FOOD_CHOICES):
      # Use the passed in choice number; passed in as path parameter aka REST parameter
      selected_choice = FOOD_CHOICES[choiceNumber]
    
      # Return a Python dictionary, which FastAPI converts to a JSON response.     
      return {"status": "success", "altchoice": selected_choice}
    else:
      return {"status": "error", "message": f"invalid choice:{choice}"}  
      
# 2. Define the endpoint at the path /madlib/
# It accepts three query parameters: noun, adjective, and verb
@app.get("/madlib/")
def generate_madlib(noun, adjective, verb):
    """
    Generates a silly sentence using the provided words.    
    """
    
    # 3. Construct the sentence (the "Mad Lib") using an f-string
    sentence = (
        f"The {adjective} {noun} decided to {verb} "
        f"loudly in the park today, much to everyone's surprise!"
    )
    
    # 4. Return a JSON response containing the full sentence
    return {
        "title": "Your Generated Mad Lib",
        "adjective": adjective,
        "noun": noun,
        "verb": verb,
        "madlib_sentence": sentence
    }

# TO RUN:
# 1. Put this code in api/main.py and deploy to Vercel
# 2. Test by using your-vercel-backend-url/docs
# 3. Later call from front-end using JavaScript fetch()