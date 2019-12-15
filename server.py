from flask import Flask, render_template, request, redirect,session,flash
import random
app = Flask(__name__)
app.number = random.randint(1,100)
app.secret_key = 'secretkey'
@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'list' not in session:
        session['list'] = []
    if 'counter' not in session:
        session['counter'] = 0
    if 'status' not in session:
        session['status'] = ''
    return render_template('index.html')

@app.route('/get_gold',methods=['POST'])
def getGold():
    form = request.form
    session['counter'] +=1
    if form.get('which_form') == 'farm':
        random_number =  random.randint(0,20)
        session['gold'] += random_number
        session['list'].append({'message':f"You earned {random_number} gold from the farm", 'class': 'green'})
    elif form.get('which_form') == 'cave':
        random_number =  random.randint(5,10)
        session['gold'] += random_number
        session['list'].append({'message':f"You earned {random_number} gold from the cave", 'class': 'green'})
    elif form.get('which_form') == 'house':
        random_number =  random.randint(2,5)
        session['gold'] += random_number
        session['list'].append({'message':f"You earned {random_number} gold from the cave", 'class': 'green'})
    else:
        random_number =  random.randint(-50,50)
        session['gold'] +=random_number
        if random_number< 0:
            session['list'].append({'message':f"You lost {random_number} gold from the casino", 'class': 'red'})
        else:
            session['list'].append({'message':f"You earned {random_number} gold from the casino", 'class': 'green'})

    if session['gold'] > 100 and session['counter'] < 15:
        session['status'] = 'won'
        
    elif session['counter']> 15:
        session['status'] = 'lost'
        



    return redirect('/')

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)