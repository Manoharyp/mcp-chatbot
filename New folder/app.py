from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Set Gemini API key directly in code
GEMINI_API_KEY = "AIzaSyDeK-laoOPdFbDm9WywtQdW1ukQpjMZ-SU"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')  # or 'gemini-2.5-flash' if available

def query_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Gemini API error: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_query = request.form.get('question') or request.json.get('question')
        answer = query_gemini(user_query)
        # If JSON requested, return JSON
        if request.is_json or request.headers.get('Accept') == 'application/json':
            return jsonify({"answer": answer})
        # Otherwise, render HTML
        return render_template('index.html', answer=answer)
    return render_template('index.html', answer=None)

if __name__ == '__main__':
    app.run(debug=True) 