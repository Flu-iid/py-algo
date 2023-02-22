#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define L(s) (int)((s).size())

void printName(const string & name) {
    cout << char(toupper(name[0]));
    for (int i = 1; i < L(name); i++)
        cout << name[i];
}

void make_valid(string & name) {
    for (int i = 0; i < L(name); i++)
        if (isalpha(name[i]) && isupper(name[i]))
            name[i] = tolower(name[i]);
}
map<string, int> money;
void end_testcase() {
    static int tc = 0;
    cout << "Case #" << ++tc << ":" << endl;
    
    vector<pair<string, int> > dept, cred;

    for (map<string,int>::iterator it = money.begin(); it != money.end(); it++){
        if (it->second > 0)
            cred.push_back(*it);
        else if (it->second < 0)
            dept.push_back(*it);
    }
    
    cout << "Debtors:" << endl;
    for (int i = 0; i < L(dept); i++) {
        printName(dept[i].first);
        cout << " owes " << -dept[i].second << " Tomans." << endl;
    }
    
    cout << "Creditors:" << endl;
    for (int i = 0; i < L(cred); i++) {
        printName(cred[i].first);
        cout << " paid " << cred[i].second << " Tomans." << endl;
    }
    money.clear();
}

int main () {
    int Tc, l;
    cin >> Tc;
    while (Tc-- && cin >> l) {
        while (l--) {
            string buyer, temp;
            int cost, n;
            cin >> buyer >> cost >> n;
            make_valid(buyer);
            money[buyer] += cost;
            cost /= n;
            
            while (n-- && cin >> temp) {
                make_valid(temp);
                money[temp] -= cost;
            }
        }
        end_testcase();
    }
    return 0;

}