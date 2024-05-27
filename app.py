from flask import Flask, request, jsonify, render_template
from main import get_wrong_text, get_correct_text

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        data = request.json.get('text')  
        wrong_text = get_wrong_text(data)
        res = []
        for t in wrong_text:
            suggest_text = get_correct_text(t)
            res.append({
                'wrong': t,
                'suggest': suggest_text,
            })
        return jsonify(res)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=6565)
   