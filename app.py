from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Fungsi perhitungan M/M/2 dengan pembulatan
def mm2_calculator(lambda_rate, mu_rate):
    rho = round(lambda_rate / (2 * mu_rate), 4)  # Utilisasi sistem dibatasi 4 digit
    p0 = round((1 - rho) / (1 - rho**2), 4)  # Probabilitas tidak ada pelanggan dibatasi 4 digit
    p1 = round(2 * rho * (1 - rho) / (1 - rho**2), 4)  # Probabilitas ada 1 pelanggan dibatasi 4 digit
    p2 = round(rho**2 / (1 - rho**2), 4)  # Probabilitas ada 2 pelanggan dibatasi 4 digit
    return p0, p1, p2, rho


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lambda_rate = float(request.form['lambda'])
        mu_rate = float(request.form['mu'])
        return redirect(url_for('result', lambda_rate=lambda_rate, mu_rate=mu_rate))
    return render_template('index.html')

@app.route('/result')
def result():
    lambda_rate = float(request.args['lambda_rate'])
    mu_rate = float(request.args['mu_rate'])
    p0, p1, p2, rho = mm2_calculator(lambda_rate, mu_rate)
    return render_template('result.html', p0=p0, p1=p1, p2=p2, rho=rho)

if __name__ == '__main__':
    app.run(debug=True)
