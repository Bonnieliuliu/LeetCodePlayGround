# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Walking Robot Simulation.py
time: 2018/8/22 1:55
"""

typedef pair<int, int> ii;
const int d[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        set<ii> A;
        for (auto& it : obstacles) {
            A.insert({it[0], it[1]});
        }
        int dir = 0, x = 0, y = 0;
        int ret = 0;
        for (auto& it : commands) {
            if (it == -2) {
                dir = (dir + 3) % 4;
            } else if (it == -1) {
                dir = (dir + 1) % 4;
            } else {
                for (int k = 0; k < it; ++k) {
                    int nx = x + d[dir][0];
                    int ny = y + d[dir][1];
                    if (A.count({nx, ny})) break;
                    x = nx;
                    y = ny;
                }
            }
//            cout << x << " " << y << " " << dir << endl;
            ret = max(ret, x * x + y * y);
        }
        return ret;
    }
