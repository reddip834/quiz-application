
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "quiz_secret_key"

questions = [
    {
        "passage": "Seven boxes A, B, G, H, T, V and P are kept one above another. Three boxes are between T and B. B is at an even-numbered position. One box is between B and V. A is above H but below G.",
        "question": "1. Which box is kept at the topmost position?",
        "options": ["Box A", "Box T", "Box B", "Box G"],
        "answer": "Box G"
    },
    {
        "passage": "Seven boxes A, B, G, H, T, V and P are kept one above another. Three boxes are between T and B. B is at an even-numbered position. One box is between B and V. A is above H but below G.",
        "question": "2. What is the position of box T from the bottom?",
        "options": ["First", "Fourth", "Third", "Second"],
        "answer": "Second"
    },
    {
        "passage": "Seven boxes A, B, G, H, T, V and P are kept one above another. Three boxes are between T and B. B is at an even-numbered position. One box is between B and V. A is above H but below G.",
        "question": "3. If all boxes are arranged alphabetically from top to bottom, how many boxes will remain in the same position?",
        "options": ["One", "Two", "Three", "Four"],
        "answer": "Two"
    },
    {
        "passage": "Seven boxes A, B, G, H, T, V and P are kept one above another. Three boxes are between T and B. B is at an even-numbered position. One box is between B and V. A is above H but below G.",
        "question": "4. Which box is kept immediately above box H?",
        "options": ["Box T", "Box P", "Box A", "Box V"],
        "answer": "Box T"
    },
    {
        "passage": "Seven boxes A, B, G, H, T, V and P are kept one above another. Three boxes are between T and B. B is at an even-numbered position. One box is between B and V. A is above H but below G.",
        "question": "5. Find the box that does not belong to the group.",
        "options": ["Box H", "Box A", "Box V", "Box P"],
        "answer": "Box V"
    },
    {
        "passage": "Eight persons M, P, Q, R, S, T, U and V are sitting around a square table. Four sit at the corners facing inside and four sit in the middle sides facing outside. Three persons sit between U and Q. U sits third to the right of R. M sits immediately right of R. Two persons sit between M and V. S sits adjacent to V and T. V is not adjacent to Q. P does not face inside.",
        "question": "6. How many persons sit between R and V when counted clockwise from R?",
        "options": ["One", "Two", "Four", "Three"],
        "answer": "Three"
    },
    {
        "passage": "Eight persons M, P, Q, R, S, T, U and V are sitting around a square table. Four sit at the corners facing inside and four sit in the middle sides facing outside. Three persons sit between U and Q. U sits third to the right of R. M sits immediately right of R. Two persons sit between M and V. S sits adjacent to V and T. V is not adjacent to Q. P does not face inside.",
        "question": "7. What is the position of T with respect to U?",
        "options": ["Immediate right", "Third to the left", "Second to the right", "Immediate left"],
        "answer": "Third to the left"
    },
    {
        "passage": "Eight persons M, P, Q, R, S, T, U and V are sitting around a square table. Four sit at the corners facing inside and four sit in the middle sides facing outside. Three persons sit between U and Q. U sits third to the right of R. M sits immediately right of R. Two persons sit between M and V. S sits adjacent to V and T. V is not adjacent to Q. P does not face inside.",
        "question": "8. Which pair represents the persons sitting opposite to each other?",
        "options": ["M and U", "P and S", "V and T", "U and Q"],
        "answer": "U and Q"
    },
    {
        "passage": "Eight persons M, P, Q, R, S, T, U and V are sitting around a square table. Four sit at the corners facing inside and four sit in the middle sides facing outside. Three persons sit between U and Q. U sits third to the right of R. M sits immediately right of R. Two persons sit between M and V. S sits adjacent to V and T. V is not adjacent to Q. P does not face inside.",
        "question": "9. If all persons are arranged alphabetically in clockwise order starting from M, how many persons remain in their original positions, excluding M?",
        "options": ["One", "Two", "Three", "Four"],
        "answer": "Three"
    },
    {
        "passage": "Eight persons M, P, Q, R, S, T, U and V are sitting around a square table. Four sit at the corners facing inside and four sit in the middle sides facing outside. Three persons sit between U and Q. U sits third to the right of R. M sits immediately right of R. Two persons sit between M and V. S sits adjacent to V and T. V is not adjacent to Q. P does not face inside.",
        "question": "10. Find the person who does not belong to the group.",
        "options": ["V", "U", "T", "R"],
        "answer": "U"
    }
]


@app.route("/", methods=["GET", "POST"])
def home():

    if "index" not in session:
        session["index"] = 0
        session["score"] = 0
        session["submitted"] = False

    if request.method == "POST":

        action = request.form.get("action")

        if action == "submit" and not session["submitted"]:
            selected = request.form.get("answer")
            current = questions[session["index"]]

            if selected == current["answer"]:
                session["score"] += 1

            session["selected"] = selected
            session["submitted"] = True

        elif action == "next":
            session["index"] += 1
            session["submitted"] = False
            session.pop("selected", None)

            if session["index"] >= len(questions):
                return redirect(url_for("result"))

    current = questions[session["index"]]

    return render_template(
        "index.html",
        question=current,
        index=session["index"],
        total=len(questions),
        submitted=session["submitted"],
        selected=session.get("selected"),
        score=session["score"]
    )


@app.route("/result")
def result():
    return render_template(
        "result.html",
        score=session.get("score", 0),
        total=len(questions)
    )


@app.route("/restart")
def restart():
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
