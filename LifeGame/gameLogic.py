from Global import *
import numpy as np


class logic:
    dx=[-1,0,1,-1,1,-1,0,1]
    dy=[-1,-1,-1,0,0,1,1,1]
    def workEvolution(self, mp):
        tmp_mp = np.zeros([Width, Height])
        for i in range(Width):
            for j in range(Height):
                cnt = 0
                for k in range(8):
                    if (i + self.dx[k] < 0) or (i + self.dx[k] >= Width) or (j + self.dy[k] < 0) or (
                            j + self.dy[k] >= Height):
                        continue
                    cnt += mp[i + self.dx[k]][j + self.dy[k]]
                if cnt == 3:
                    tmp_mp[i][j] = 1
                elif cnt == 2 and mp[i][j] == 1:
                    tmp_mp[i][j] = 1
                else:
                    tmp_mp[i][j] = 0
        return tmp_mp
