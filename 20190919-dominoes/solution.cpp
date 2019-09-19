#include <iostream>
#include <cmath>
#include "solution.h"
using namespace std;


string Solution::pushDominoes(string dominoes)
{
  string final_state = "";

  cout << dominoes << endl;  
  
  int length = dominoes.length();
  bool going_right = false;
  int last_index = 0;
  int runway;

  for (int i = 0; i<length ; i++) {
	switch (dominoes[i]) {
		case '.':
			break;
		case 'R':
			if (going_right) {
				cout << "can I get a what what ";
				for (int j = last_index; j < i; j++) {
					dominoes[j] = 'R';
				}
			}

			last_index = i;
			going_right = true;
			break;
		case 'L':
			cout << "found an L ";
			if (going_right) {
				going_right = false;
				runway = floor(((i - last_index) - 1) / 2);
				for (int j = 1; j <= runway; j++) {
					dominoes[last_index + j] = 'R';
					dominoes[i - j] = 'L'; 
				}
			} else {
				for (int j = last_index; j < i; j++) {
                                        dominoes[j] = 'L';
                                }
			}
			last_index = i;
			break;
	}
	cout << i << ": " << dominoes[i] << " going_right: " << going_right <<  endl;
  }

  cout << endl << "result: " << dominoes << endl;

  return final_state;
}


int main() 
{
    cout << "Hello, World!";
    Solution::pushDominoes("..L....R....R...R.....L...L...RRRR..R..");
    return 0;
}
