#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <optional>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

bool check_direction(const vector<vector<char>>& map, int i, int j, int di, int dj) {
    string result;
    for (int k = 0; k < 4; ++k) {
        result += map[i + k * di][j + k * dj];
    }
    return result == "XMAS";
}

int main() {
  int xmas_cnt = 0;

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

  string xmas = "XMAS";
  for (int i = 0; i < map.size(); ++i) {
    auto row = map[i];
    for (int j = 0; j < row.size(); ++j) {
      if (row[j] == 'X') {
        bool up = (i - 3 >= 0) ? true : false;
        bool down = (i + 3 < map.size()) ? true : false;
        bool left = (j - 3 >= 0) ? true : false;
        bool right = (j + 3 < row.size()) ? true : false;

        if (up) {
          if (check_direction(map, i, j, -1, 0))
            xmas_cnt++;
        }

        if (down) {
          if (check_direction(map, i, j, 1, 0))
            xmas_cnt++;
        }

        if (right) {
          if (check_direction(map, i, j, 0, 1))
            xmas_cnt++;
        }

        if (left) {
          if (check_direction(map, i, j, 0, -1))
            xmas_cnt++;
        }

        if (right && up) {
          if (check_direction(map, i, j, -1, 1))
            xmas_cnt++;
        }

        if (left && up) {
          if (check_direction(map, i, j, -1, -1))
            xmas_cnt++;
        }

        if (left && down) {
          if (check_direction(map, i, j, 1, -1))
            xmas_cnt++;
        }

        if (right && down) {
          if (check_direction(map, i, j, 1, 1))
            xmas_cnt++;
        }
      }
    }
  }

  cout << "Result: " << xmas_cnt << endl;

  return 0;
}
