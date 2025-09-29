from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import io
import datetime

def create_invoice_pdf(data: dict) -> bytes:
    """
    Generates a PDF invoice as bytes from structured data fetched from MongoDB.
    
    Args:
        data (dict): The MongoDB document containing the list of "items".
        
    Returns:
        bytes: The raw PDF file content, ready to be returned by FastAPI.
    """
    buffer = io.BytesIO()
    
    # SimpleDocTemplate handles the overall structure and page flow
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    # --- 1. Header Information ---
    
    # Invoice Title
    elements.append(Paragraph("Invoice: MerchEazy Voice Order", styles['Title']))
    
    # Metadata (Date, Order ID)
    # The _id field from MongoDB is a special ObjectId object, so we convert it to a string.
    invoice_id = str(data.get('_id', 'N/A'))
    invoice_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    elements.append(Paragraph(f"<b>Order ID:</b> {invoice_id}", styles['Normal']))
    elements.append(Paragraph(f"<b>Invoice Date:</b> {invoice_date}", styles['Normal']))
    elements.append(Paragraph("<br/>", styles['Normal'])) # Spacer

    # --- 2. Item Table Data ---
    
    # Define the table headers
    table_data = [['#', 'Item Name', 'Quantity (Text)', 'Qty (Num)', 'Category']]
    items = data.get('items', [])
    
    for i, item in enumerate(items):
        row = [
            str(i + 1),
            item.get('name', 'N/A'),
            item.get('qty', 'N/A'),
            # Ensure qty_num is formatted as a string with one decimal place for clarity
            f"{item.get('qty_num', 0.0):.1f}", 
            item.get('category', 'N/A'),
        ]
        table_data.append(row)
    
    # Create the table
    col_widths = [30, 160, 100, 80, 120] # Define column widths
    invoice_table = Table(table_data, colWidths=col_widths)

    # --- 3. Table Style ---
    
    style = TableStyle([
        # Header Row Styling
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        
        # General Cell Styling
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ])
    
    invoice_table.setStyle(style)
    elements.append(invoice_table)

    # --- 4. Footer ---
    elements.append(Paragraph("<br/><br/>", styles['Normal']))
    elements.append(Paragraph("Thank you for using the MerchEazy!", styles['Italic']))

    # Build the document
    doc.build(elements)
    
    # Get the value of the BytesIO buffer and close it
    pdf_bytes = buffer.getvalue()
    buffer.close()
    
    return pdf_bytes

if __name__ == "__main__":
    # Example usage for direct file testing:
    # This block generates a PDF file in the local directory.
    print("--- Testing PDF Generation ---")
    test_data = {
        "_id": "65b8c3d8e5f14a6b2c7d9e0f",
        "items": [
            {
                "name": "large pepperoni pizza", 
                "qty": "1", 
                "qty_num": 1.0, 
                "category": "order_food"
            },
            {
                "name": "dishwash gel", 
                "qty": "2 bottles", 
                "qty_num": 2.0, 
                "category": "cleaning supplies"
            },
        ],
        "source": "test_script"
    }
    
    pdf_output = create_invoice_pdf(test_data)
    
    with open("test_invoice.pdf", "wb") as f:
        f.write(pdf_output)
    
    print("PDF generated successfully: test_invoice.pdf (Check your local directory)")
