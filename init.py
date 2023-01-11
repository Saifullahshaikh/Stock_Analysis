import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, render_template
from flask import request
import yfinance

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/get_plot', methods=["GET","POST"])
def get_plot():
    if request.method == "POST":
        key=request.form['Stock_Key']
        pur = request.form['Purchase_price']
        sale1=request.form["Sale_price_1"]
        sale2=request.form["Sale_price_2"]
        key.upper()
        st_key = yfinance.Ticker(key)
        hist = st_key.history(period="1y")
        items= len(hist.index)
        purchase = [int(pur)]*items
        sale_val1= [int(sale1)]*items
        sale_val2 = [int(sale2)]*items
        plt.plot(hist.index, hist['Close'], label= "Original Price")
        plt.plot(hist.index, purchase, label= "Purchase Price")
        # plotting the line 2 points 
        plt.plot(hist.index, sale_val1,  label= "Sale Price 1")
        plt.plot(hist.index, sale_val2, label= "Sale Price 2")
        # giving a title to my graph
        plt.title("1y")
        # show a legend on the plot
        #plt.legend("Actual Price","Purchase Price", "Sale Price 1", "Sale Price 2")
        plt.savefig('static/myplot.png')
        return render_template('index.html',plot_url='static/myplot.png')
    else:
        return render_template('index.html')
app.secret_key = 'qwerty'

if __name__ == "__main__":
    app.run('127.0.0.1', 5000,debug=True)