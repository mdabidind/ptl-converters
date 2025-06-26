# ptl-converters
Python script for PDF to Word conversion
for filename in os.listdir(queue_dir):
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(queue_dir, filename)
        docx_name = os.path.splitext(filename)[0] + ".docx"
        docx_path = os.path.join(output_dir, docx_name)

        # Convert...
