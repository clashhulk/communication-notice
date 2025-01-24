from flask import Flask, request, send_file
from docx import Document
from io import BytesIO
import pdfkit

app = Flask(__name__)


@app.route('/')
def upload_page():
    return '''
    <!DOCTYPE html>
    <html>
    <head><title>Upload and Edit Document</title></head>
    <body>
        <h2>Upload Word Document</h2>
        <form action="/preview" method="post" enctype="multipart/form-data">
            <input type="file" name="file" accept=".docx" required>
            <button type="submit">Upload</button>
        </form>
    </body>
    </html>
    '''


@app.route('/preview', methods=['POST'])
def preview_file():
    file = request.files['file']
    if not file:
        return "No file uploaded!", 400

    doc = Document(file)
    html_content = ""
    for paragraph in doc.paragraphs:
        html_content += f"<p>{paragraph.text}</p>"
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Edit Document</title>
        <script src="https://cdn.ckeditor.com/4.21.0/standard/ckeditor.js"></script>
    </head>
    <body>
        <h2>Edit Your Document</h2>
        <form action="/generate-pdf" method="post">
            <textarea name="content" id="editor">{html_content}</textarea>
            <button type="submit">Generate PDF</button>
        </form>
        <script>CKEDITOR.replace('editor');</script>
    </body>
    </html>
    '''


@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    edited_content = request.form['content']

    pdf_file = BytesIO()
    pdfkit.from_string(edited_content, pdf_file)
    pdf_file.seek(0)

    return send_file(pdf_file, as_attachment=True, download_name="output.pdf", mimetype="application/pdf")


if __name__ == '__main__':
    app.run(debug=True)
