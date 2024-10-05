from flask import Flask, render_template, request, redirect, url_for, jsonify
import ollama

app = Flask(__name__)

questions_list = [
    {
        "question": "Should you hit the Penjamin?",
        "options": ["Stress", "Boredom", "Social pressure", "Anger", "Fear", "Sadness", "Other"]
    },
    {
        "question": "What triggered your relapse?",
        "options": ["Work stress", "Personal issues", "Financial problems", "Social interactions"]
    },
    {
        "question": "What do you feel is the best coping mechanism?",
        "options": ["Exercise", "Meditation", "Talking to a friend", "Writing in a journal"]
    }
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/relax')
def relax():
    return render_template('relax.html')

@app.route('/sources')
def sources():
    return render_template('sources.html')

@app.route('/questions/<int:question_number>', methods=['GET', 'POST'])
def questions(question_number):
    if request.method == 'POST':
        selected_option = request.form.get('response')
        return redirect(url_for('questions', question_number=question_number + 1))
    if question_number <= len(questions_list):
        question_data = questions_list[question_number - 1]
        return render_template('questions.html', question_data=question_data, question_number=question_number)
    else:
        return redirect(url_for('submit'))


@app.route('/chat', methods=['GET'])
def chat_page():
    # get prompt from URL and run chat
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat_with_llm():
    data = request.json
    messages_resp = data.get('messages', [])
    # print(messages_resp)
    # print('^^^')
    # reformat messages
    # eg:
    # messages = [{'role': 'system', 'content': "You are a therapist AI named Dr. Nemo. Help guide the user with cognitive behavioral therapy techniques. Based upon the user's responses, use the principles of Cognitive Behavioral Therapy (CBT) to help the user understand their triggers and develop a plan to avoid them in the future."},
    # {'role': 'user', 'content': 'Begin the role play:'}]

    # first = {'role': 'system', 'content': "You are a therapist AI named Dr. Nemo. Help guide the user with cognitive behavioral therapy techniques. "+messages_resp[0]}
    # messages = [first]


    # if len(messages_resp)>1:
    #     for m in messages_resp[1:]:
    #         messages.append({'role':'user','content':m})

    messages = messages_resp

    # Use ollama to get the response based on the message history
    result = ollama.chat(model='llama3.2', messages=messages)
    # print(result)
    ai_message = result['message']['content']

    return jsonify({'message': ai_message})


if __name__ == "__main__":

    app.run(debug=True)

