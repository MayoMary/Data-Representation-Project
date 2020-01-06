from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='../')

#@app.route('/')
#def index():
#   return"Hello, World!"

@app.route('/books')
def getAll():
   return "in getALL"

@app.route('/books/<int:id>')
def findById(id):
   return "in find by ID for id " +str(id)

@app.route('/books', methods=['POST'])
def create():
   return "in create " +str(id)

@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
   return "in update for id" +str(id)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
   return "in delete for id" +str(id)
 

if __name__ == '__main__' :
    app.run(debug= True)