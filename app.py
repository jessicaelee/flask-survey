from flask import Flask, render_template, redirect, request, session
from surveys import surveys
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.debug = False

app.config['SECRET_KEY'] = '<Rockinn Richard>'

toolbar = DebugToolbarExtension(app)

responses = []
question_idx = 0

@app.route("/")
def root():
    responses = []
    title = surveys["satisfaction"].title
    instructions = surveys["satisfaction"].instructions
    return render_template("root.html", title=title, 
    instructions=instructions, question_idx=0)

@app.route("/question/<int:question_idx>")
def questions(question_idx):
    print(len(surveys["satisfaction"].questions), "response", responses, "questionidx", question_idx, "length", len(responses))
    if question_idx != len(responses):
        return redirect(f"/question/{len(responses)}")
    elif len(responses) == len(surveys["satisfaction"].questions):
       return redirect("/thankyou")
    else:
        title = surveys["satisfaction"].title
        question = surveys["satisfaction"].questions[question_idx].question
        choices = surveys["satisfaction"].questions[question_idx].choices
        # if int(question_idx) >= 0:
        #     responses.append(request.args.get("answer"))
        #     question_idx += 1
        return render_template("question.html", title=title, question=question, choices=choices,question_idx=question_idx) 
 
@app.route("/question/<int:question_idx>", methods=["POST"])
def get_answer(question_idx):
    print(request.args.get("answer"))
    responses.append(request.form.get("answer"))
    question_idx += 1
    return redirect(f"/question/{len(responses)}")

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html", title="Thank you")

