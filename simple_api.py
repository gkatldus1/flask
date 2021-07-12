from flask import Flask, request, jsonify

app = Flask(__name__)


people = [
    {
        "employee_number": 1,
        "name": "john",
        "age": 21,
        "job": "programmer",
        "height": 180,
        "salary": 40000000,
    },
    {
        "employee_number": 2,
        "name": "철수",
        "age": 12,
        "job": "model",
        "height": 154,
        "salary": 30000000,
    },
    {
        "employee_number": 3,
        "name": "영희",
        "age": 20,
        "job": "model",
        "height": 160,
        "salary": 35000000,
    },
    {
        "employee_number": 4,
        "name": "steve",
        "age": 30,
        "job": "programmer",
        "height": 175,
        "salary": 100000000,
    }
]


@app.route("/employee", methods=["GET"])
def find_employees():
    query_people = people[:]

    # 나이로 검색
    query_age = request.args["age"]
    if query_age is not None:
        for i in range(len(query_people)-1, -1, -1):
            if query_people[i]["age"] != int(query_age):
                query_people.pop(i)

    # 이름으로 검색
    query_name = request.args.get("name")
    if query_name is not None:
        for i in range(len(query_people)-1, -1, -1):
            if query_people[i]["name"] != query_name:
                query_people.pop(i)
    
    # 직업으로 검색.
    query_job = request.args.get("job")
    if query_job is not None:
        for i in range(len(query_people)-1, -1, -1):
            if query_people[i]["job"] != query_job:
                query_people.pop(i)
    
    return jsonify(query_people)

# 직원을 추가하는 api
@app.route("/employee", methods=["POST"])
def add_employee():
    people.append({
        "employee_number": int(request.form.get("employee_number")),
        "name": request.form.get("name"),
        "age": int(request.form.get("age")),
        "job": request.form.get("job"),
        "height": int(request.form.get("height")),
        "salary": int(request.form.get("salary"))
    
    })


    return "add_employee"

# 직원을 삭제하는 api
@app.route("/employee/<int:employee_number>", methods=["DELETE"])
def fire_employee(employee_number):
    for p in people:
        if p["employee_number"] == employee_number:
            people.remove(p)
            
    return "fire_employee"


if __name__ == '__main__':
    app.run(debug=True)