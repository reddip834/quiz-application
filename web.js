
let currentQuestion = 0;
let score = 0;
let answered = false;

function loadQuestion() {
    answered = false;

    const q = questions[currentQuestion];

    document.getElementById("question").innerText = q.question;

    document.getElementById("progress").innerText =
        `Question ${currentQuestion + 1} of ${questions.length}`;

    document.getElementById("result").innerText = "";

    document.getElementById("submitBtn").hidden = false;
    document.getElementById("nextBtn").hidden = true;

    let optionsHTML = "";

    q.options.forEach(option => {
        optionsHTML += `
            <label class="option">
                <input type="radio" name="answer" value="${option}">
                ${option}
            </label>
        `;
    });

    document.getElementById("options").innerHTML = optionsHTML;
}

function submitAnswer() {

    if (answered) return;

    const selected = document.querySelector(
        'input[name="answer"]:checked'
    );

    if (!selected) {
        alert("Please select an answer!");
        return;
    }

    answered = true;

    if (selected.value === questions[currentQuestion].answer) {
        score++;

        document.getElementById("result").innerText =
            "Correct Answer!";
    } else {
        document.getElementById("result").innerText =
            "Wrong Answer! Correct answer: " +
            questions[currentQuestion].answer;
    }

    document.getElementById("submitBtn").hidden = true;
    document.getElementById("nextBtn").hidden = false;

    if (currentQuestion === questions.length - 1) {
        document.getElementById("nextBtn").innerText = "View Result";
    }
}

function nextQuestion() {

    currentQuestion++;

    if (currentQuestion < questions.length) {
        loadQuestion();
    } else {
        document.getElementById("quiz-section").hidden = true;
        document.getElementById("final-result").hidden = false;

        document.getElementById("score").innerText =
            `Your Score: ${score} / ${questions.length}`;
    }
}

function restartQuiz() {
    currentQuestion = 0;
    score = 0;

    document.getElementById("quiz-section").hidden = false;
    document.getElementById("final-result").hidden = true;

    loadQuestion();
}

loadQuestion();
