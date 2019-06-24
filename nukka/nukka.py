from lark import Lark

def main():
  f = open('nukka/c.lark')
  l = Lark(f.read(), ambiguity='explicit')
  print(l.parse(
  '''
  int main() {
    int a = 200;
    a = 100;
  }
  ''').pretty())
  f.close()

if __name__ == '__main__':
  main()
