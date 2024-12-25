#include <cmath>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

bool comp(int a, int b) { return a > b; }

int main() {

  ifstream file("input.txt");
  string line;

  vector<int> left;
  vector<int> right;

  if (file.is_open()) {
    while (getline(file, line)) {
      stringstream ss(line);

      string t;

      char del = ' ';

      bool first = true;
      while (getline(ss, t, del)) {
        if (t.empty()) {
          first = false;
        } else if (first) {
          left.push_back(stoi(t));
        } else {
          right.push_back(stoi(t));
        }
      }
    }

    file.close();
  } else {
    cerr << "Unable to open file!" << endl;
  }

  int score = 0;
  for (int i : left) {
    int cnt = 0;
    for (int j : right) {
      if (i == j) {
        cnt++;
      }
    }

    score += i * cnt;
  }

  cout << "Total similarity score: " << score << endl;

  return 0;
}
