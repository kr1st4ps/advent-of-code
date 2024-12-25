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
  int x_mas_cnt = 0;

  ifstream file("input.txt");
  char ch;
  vector<vector<char>> map;
  map.emplace_back();

  if (file.is_open()) {
    while (file.get(ch)) {
      if (ch == '\n') {
        map.emplace_back();
      } else {
        map.back().push_back(ch);
      }
    }

    file.close();
  } else {
    cerr << "Unable to open file!" << endl;
  }

  for (int i = 0; i < map.size(); ++i) {
    auto row = map[i];
    for (int j = 0; j < row.size(); ++j) {
      if (row[j] == 'A') {
        bool up = (i - 1 >= 0) ? true : false;
        bool down = (i + 1 < map.size()) ? true : false;
        bool left = (j - 1 >= 0) ? true : false;
        bool right = (j + 1 < row.size()) ? true : false;

        if (up && down && right && left) {
          char top_left = map[i - 1][j - 1];
          char top_right = map[i - 1][j + 1];
          char bottom_left = map[i + 1][j - 1];
          char bottom_right = map[i + 1][j + 1];

          bool left = ((top_left == 'M' && bottom_right == 'S') ||
                       (top_left == 'S' && bottom_right == 'M'))
                          ? true
                          : false;
          bool right = ((top_right == 'M' && bottom_left == 'S') ||
                        (top_right == 'S' && bottom_left == 'M'))
                           ? true
                           : false;

          if (left && right)
            x_mas_cnt++;
        }
      }
    }
  }

  cout << "Result: " << x_mas_cnt << endl;

  return 0;
}
