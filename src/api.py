import uvicorn
import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse,Response,FileResponse
from pydantic import BaseModel, Field
import os
# Local Imports
# FIX: Import the necessary Pydantic models (InventoryItem) 
# and the processing function from llm_chain.py, 
# since the models are defined there.
from src.core.llm_chain import process_grocery_list, InventoryItem 
from src.database.connection import save_grocery_list,get_latest_grocery_list
from src.utils.pdf_generator import create_invoice_pdf

# --- 1. Define Input Model ---
# This model ensures the incoming request body has a 'text' field.
class TextInput(BaseModel):
    """Model for accepting raw text input from the user."""
    text: str = Field(..., description="The voice input transcribed into raw text.")

# --- 2. Initialize FastAPI ---
app = FastAPI(
    title="Voice-to-DB Processor",
    description="API for processing transcribed voice input into a structured MongoDB entry using LangChain.",
    version="1.0.0"
)

# --- NEW: Root Endpoint (Health Check) ---
@app.get("/")
async def root():
    """Returns a simple greeting to confirm the API is running."""
    return {"message": "Welcome to the Voice-to-DB Processor API. Use /process-grocery-request/ to submit data."}

# --- 3. Define the Processing Endpoint ---
# FIX: Update the response_model to InventoryItem
@app.post("/process-grocery-request/", response_model=InventoryItem)
async def process_text_and_save(input: TextInput):
    """
    Accepts raw text, processes it with LangChain to extract a structured grocery list,
    and saves the result to MongoDB.
    """
    try:
        transcribed_text = input.text

        if not transcribed_text or not transcribed_text.strip():
            raise HTTPException(status_code=400, detail="Input text cannot be empty.")
        
        # Step 1: Process the text with the LangChain/LLM module
        # This returns a dictionary matching the InventoryItem schema
        grocery_list: dict = process_grocery_list(transcribed_text)
        
        # Step 2: Save the structured data to MongoDB
        save_grocery_list(grocery_list)

        # Step 3: Return the structured data to the user
        return JSONResponse(content={
            "status": "success",
            "message": "Text successfully processed and saved to MongoDB.",
            "data": grocery_list
        }, status_code=200)

    except HTTPException as http_exc:
        # Re-raise explicit HTTP exceptions (e.g., 400 bad request)
        raise http_exc
        
    except Exception as e:
        # Catch any unexpected errors and log them
        print(f"Internal Server Error during processing: {e}")
        raise HTTPException(
            status_code=500, 
            detail=f"An internal processing error occurred: {str(e)}"
        )
    
@app.get("/generate-invoice/")
async def generate_invoice():
    """
    Fetches the latest grocery list from MongoDB and generates a PDF invoice, 
    returning it as a downloadable file.
    """
    # 1. Fetch data from MongoDB
    latest_data = get_latest_grocery_list()
    
    if not latest_data:
        raise HTTPException(status_code=404, detail="No recent grocery list found in the database to generate an invoice.")
    
    # 2. Generate PDF bytes
    try:
        pdf_bytes = create_invoice_pdf(latest_data)
    except Exception as e:
        print(f"PDF Generation Error: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate PDF invoice.")
    
    # 3. Return the PDF file
    # The 'Content-Disposition' header tells the browser to download the file.
    # The MongoDB '_id' (converted to string) is used for the filename.
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"attachment; filename=invoice_{str(latest_data.get('_id', 'latest'))}.pdf"
        }
    )

        
# --- 4. Running the Application (Optional for direct execution) ---
if __name__ == "__main__":
    # To run this file directly (only for quick local testing):
    # uvicorn src.api:app --reload
    uvicorn.run(app, host="0.0.0.0", port=8000)
