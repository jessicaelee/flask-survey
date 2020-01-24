from flask import Flask, render_template, redirect, request, session
from surveys import surveys
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.debug = False

app.config['SECRET_KEY'] = '<Rockin Richard>'

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


# @app.route("/", methods=["POST"])
# def root_post():
#     return redirect(f"/question/{question_idx}")


@app.route("/question/<int:question_idx>")
def questions(question_idx):
    # if question_idx != len(responses):
    #     return redirect(f"/question/{question_idx}")
    if int(question_idx) < int(len(surveys["satisfaction"].questions)):
        title = surveys["satisfaction"].title
        question = surveys["satisfaction"].questions[question_idx].question
        choices = surveys["satisfaction"].questions[question_idx].choices

        if int(question_idx) > 0:
            responses.append(request.args.get("answer"))
            print(responses)
      
        question_idx += 1

        return render_template("question.html", title=title, question=question, choices=choices, question_idx=question_idx)
    else: 
        responses.append(request.args.get("answer"))
        print(responses)
        return redirect("/thankyou")


@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html", title="Thank you")


    # @app.route("/question/<int:question_idx>", methods=["POST"])
# def questions_answer(question_idx): 
#     answer = request.form.get("answer")
#     # responses.append(answer)
#     # print(responses)
#     session["answer"] = answer