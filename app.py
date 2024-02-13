from flask import Flask, render_template, request, send_file
from markdown import markdown
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        markdown_text = request.form['markdown_text']
        html_content = markdown(markdown_text)
        html_content_buffer = io.BytesIO()
        html_content_buffer.write(html_content.encode('utf-8'))
        html_content_buffer.seek(0)
        return send_file(
            html_content_buffer,
            as_attachment=True,
            mimetype='text/html',
            download_name='converted.html'
        )
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)