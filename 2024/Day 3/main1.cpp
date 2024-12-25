#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <optional>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main() {
  int result = 0;

  ifstream file("input.txt");
  char ch;
  string window = "";

  if (file.is_open()) {
    while (file.get(ch)) {
      if (window.size() == 4) {
        window = window.substr(1, 3) + ch;
      } else {
        window += ch;
      }

      if (window == "mul(") {
        string first_str, second_str = "";
        bool collecting_first = true;
        while (file.get(ch)) {
          if (ch == ',') {
            if (collecting_first) {
              collecting_first = false;
            } else {
              break;
            }
          } else if (ch == ')') {
            if (!collecting_first) {
              result += stoi(first_str) * stoi(second_str);
            }
            window = "";
            break;
          } else if (isdigit(ch)) {
            if (collecting_first) {
              first_str += ch;
            } else {
              second_str += ch;
            }
          } else {
            break;
          }
        }
      }
    }

    file.close();
  } else {
    cerr << "Unable to open file!" << endl;
  }

  cout << "Result: " << result << endl;

  return 0;
}
