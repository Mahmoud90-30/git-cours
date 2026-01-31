#include <iostream>
#include <queue>
#include <stack>
using namespace std;
#define fast ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define el "\n"
#define sp " "
#define ll long long
deque<ll>q;
int main() {
    fast;
    ll n,m,a;
    string s;
    cin >> s;
    stack<char> st;
    for (char c : s) {
        if (!st.empty()) {
            if (st.top() =='('&&c==')') {
                st.pop();
            }
            else
                st.push(c);
        }
        else {
            st.push(c);
        }

    }
    cout << s.size()-st.size() << el;


    return 0;

}
