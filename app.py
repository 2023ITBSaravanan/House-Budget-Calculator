from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/calculate', methods=['POST'])
def calculate():
    city = request.form['city']
    area = int(request.form['area'])
    years = int(request.form['years'])

    city_price = {
        
        "Bangalore": 5500,
        "Chennai": 4500,
        "Mumbai": 8500,
        "Delhi": 6500,
        "Hyderabad": 4800
    }

    base_price = city_price[city]
    future_price = base_price * (1 + 0.05) ** years
    total_cost = future_price * area

    return render_template(
        "index.html",
        city=city,
        area=area,
        years=years,
        cost=round(total_cost, 2),
        show=True
    )

if __name__ == "__main__":
    app.run(debug=True)