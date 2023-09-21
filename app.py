from flask import Flask, render_template, request

# app = Flask(__name__, static_url_path='/static', static_folder='static')
#  app = Flask(__name__, template_folder='templates', static_folder='staticFiles')

app = Flask(__name__) 

@app.route("/", methods=['GET', 'POST'])
def basic_calc():
    num_1,num_2,operations,result,err= None,None,None,None,None
    if request.method == 'POST':
        num_1 = request.form['num_1'] # num_1 = float(request.form.get('num_1'))
        num_2 = request.form['num_2']
        operation = request.form['operations'] 
        if not num_1.isdigit() or not num_2.isdigit() :
            err = 'The entered value is not digit/number. \n Both inputs must be numeric!'
        
        else:
            num_1 = float(num_1)
            num_2 = float(num_2)
            if operation == '+':
                result = num_1 + num_2
            elif operation == '-':
                result = num_1 - num_2
            elif operation == '*':
                result = num_1 * num_2
            elif operation == '/':
                if num_2 == 0.0:
                    error_msg  = 'Division by zero is not allowed.'                    
                    return render_template('index.html', error_msg= error_msg)
                else:
                    result = num_1 / num_2
                result = num_1 / num_2
            
            else:
                 err = 'Please select a valid operation sign (+, -, *, /)'
    # display_result = '{} {} {} = {}' .format(num_1, operations ,num_2,result)
    display_result = f'{num_1} {operation} {num_2} = {result}' if result is not None else ''
    error_msg = err
    return render_template('index.html', result = result,display_result= display_result, error_msg = error_msg)
 
if __name__=='__main__':
    app.run(debug = True)