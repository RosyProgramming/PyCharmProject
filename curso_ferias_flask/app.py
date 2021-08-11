from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
      if request.method == 'GET':
        return render_template('index.html')

      else:

        nome = request.form['nome']
        idade = request.form['idade']
        profissao = request.form['profissao']

        return 'Nome {} Idade {} profissao'.format(nome,idade,profissao)



if __name__ =='__main__':
     app.run(debug=True)
