
import random
from fastapi import FastAPI
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