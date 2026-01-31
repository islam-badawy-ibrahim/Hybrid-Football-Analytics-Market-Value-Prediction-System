#include <iostream>
#include <iomanip>
#include <string>

using namespace std;
double calculatePerformance(int goals, int assists, int minutes) {
    if (minutes <= 0) return 0;
    return ((double)(goals + assists) / minutes) * 90;
}

int main() {
    string playerName;
    int goals, assists, minutes;

    cout << "Football Player Performance Calculator." << endl;
    cout << "Enter Player Name: ";
    getline(cin, playerName);
    cout << "Enter Goals: "; cin >> goals;
    cout << "Enter Assists: "; cin >> assists;
    cout << "Enter Minutes Played: "; cin >> minutes;

    double score = calculatePerformance(goals, assists, minutes);

    cout << "\nResults for: " << playerName << endl;
    cout << "Performance Score (Per 90 mins): " << fixed << setprecision(2) << score << endl;

    return 0;
}
