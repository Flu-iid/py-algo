#include <iostream>
#include <algorithm>
using namespace std;

void to_play(pair<int, int> a[], int n)
{
    int index = 0;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
        {
            a[index] = {i, j};
            index++;
        }
}

void to_score(pair<int, int> plays[], int scores[], int teams[][3], int n)
{
    for (int i = 0; i < n * (n - 1) / 2; i++)
    {
        int t1 = plays[i].first, t2 = plays[i].second;
        int goal1 = scores[t1 * n + t2];
        int goal2 = scores[t2 * n + t1];

        if (goal1 == goal2)
        {
            teams[t1][0]++;
            teams[t2][0]++;
        }
        else if (goal1 > goal2)
        {
            teams[t1][0] += 3;
            teams[t1][1] += goal1 - goal2;

            teams[t2][1] += goal2 - goal1;
        }
        else
        {
            teams[t2][0] += 3;
            teams[t2][1] += goal2 - goal1;

            teams[t1][1] += goal1 - goal2;
        }
    }
}

bool sort_key(int a, int b)
{
    return a[0] * 100000 + a[1] * 100 - a[2] > b[0] * 100000 + b[1] * 100 - b[2];
}

int main()
{
    int n;
    cin >> n;
    int scores[n * n];
    for (int i = 0; i < n * n; i++)
        cin >> scores[i];

    pair<int, int> plays[n * (n - 1) / 2];
    to_play(plays, n);

    int teams[n][3];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < 3; j++)
        {
            if (j == 2)
                teams[i][j] = i;
            else
                teams[i][j] = 0;
        }

    to_score(plays, scores, teams, n);

    sort(teams, teams + n, sort_key);

    for (int i = 0; i < n; i++)
    {
        char view = 'a' + teams[i][2];
        cout << view;
    }
}