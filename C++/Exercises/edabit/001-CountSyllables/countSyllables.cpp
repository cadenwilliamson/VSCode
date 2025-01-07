#include <iostream>
#include <string>

using std::string;
using std::cout;
using std::endl;

string word_01 = ("buf-fet");
string word_02 = ("beau-ti-ful");
string word_03 = ("mon-u-men-tal");
string word_04 = ("on-o-mat-o-poe-ia");


int countSyllables(string word) {
    int count = 1;
    for (char c : word) {
        if (c == '-') {
            count++;
        }
    }
    cout << "'" << word << "' syllables: " << count << endl;

    // cout << word << endl;
    return 0;
}

int main() {
    countSyllables(word_01);
    countSyllables(word_02);
    countSyllables(word_03);
    countSyllables(word_04);

    return 0;
}