#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <optional>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

bool comp(int a, int b) { return a > b; }

int main() {
  int good_reports = 0;

  ifstream file("input.txt");
  string line;

  if (file.is_open()) {
    while (getline(file, line)) {
      vector<int> report;

      stringstream ss(line);

      string num_str;
      char del = ' ';

      while (getline(ss, num_str, del)) {
        report.push_back(stoi(num_str));
      }

      std::optional<int> skippable = std::nullopt;
      while (!skippable.has_value() || skippable.value() < report.size()) {
        std::optional<int> prev_num = std::nullopt;
        std::optional<bool> incrementing = std::nullopt;
        bool valid = true;
        for (int i = 0; i < report.size(); ++i) {
          if (skippable.has_value() && skippable.value() == i)
            continue;

          int num = report[i];
          if (prev_num.has_value()) {
            auto diff = num - prev_num.value();
            if (diff == 0 || abs(diff) > 3) {
              if (skippable.has_value()) {
                skippable.value()++;
              } else {
                skippable = 0;
              }
              valid = false;
              break;
            }

            if (incrementing.has_value()) {
              if ((incrementing.value() && diff < 0) ||
                  (!incrementing.value() && diff > 0)) {
                if (skippable.has_value()) {
                  skippable.value()++;
                } else {
                  skippable = 0;
                }
                valid = false;
                break;
              }
            } else {
              incrementing = (diff > 0) ? true : false;
            }
          }
          prev_num = num;
        }
        if (valid) {
          good_reports++;
          break;
        }
      }
    }

    file.close();
  } else {
    cerr << "Unable to open file!" << endl;
  }

  cout << "Good reports: " << good_reports << endl;

  return 0;
}
