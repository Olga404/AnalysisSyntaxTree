source_text = '22+1  *5*(  10-  (  24))'

class Node():
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

class Lexer(object):
  def __init__(self):
    self.digits = ['0','1','2','3','4','5','6','7','8','9',]  #символы,которые есть в алфавите
  def analyze(self, source_text):
    text = "".join(source_text
      .split())
    tokens = []
    token = ''
    for symbol in text:
      token = symbol
      tokens.append(symbol)
    return tokens
    
lexer = Lexer();
tokenized_text = lexer.analyze(source_text)
print(tokenized_text)