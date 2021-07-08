from flask import Flask, jsonify
import func

app = Flask(__name__)


@app.route("/question", methods=["GET"])
def question():
        rows = func.get_all("select q.number, q.content , a.option_key, a.option_content from questions q inner join answers_option a on q.number = a.number")
        data = []
        for i in rows:
            data.append({
                "Number": i[0],
                "Content": i[1],
                "Option key": i[2],
                "Option content":i[3]
            })
        return jsonify({"Question": data})

@app.route("/answer", methods=["GET"])
def answer():
    rows = func.get_all("select * from answer")
    data = []
    for i in rows:
        data.append({
            "Number" : i[0],
            "Answer" : i[1]
        })
    return jsonify({"Answer":data})

if __name__ == "__main__":
    app.run()
