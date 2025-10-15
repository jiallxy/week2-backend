from fastapi import FastAPI

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
    
