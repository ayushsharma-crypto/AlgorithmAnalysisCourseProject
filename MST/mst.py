import sys
import graphplot

lead = {}
rank = {}
mod = (int)(1e9+7)
edgelist = []
nodelist = []


def leader(a):
    # print(lead[a])
    # print(a)
    if lead[a] == a:
        return a
    return leader(lead[a])


def modExp(a, b):
    res = 1
    while b > 0:
        if b % 2 == 1:
            res = (res*a) % mod
        b /= 2
        a = (a*a) % mod
    return res % mod


if __name__ == "__main__":
    # print("enter n and m in")
    n = int(input("Enter n\n"))
    m = int(input("Enter m\n"))
    # print(n, m)
    i = 0
    print('''Enter m pairs of edges with weight and whether a bully or not\n
    Like 5 6 1 b means an edge between 5&6 with edge length 1 and a bully is present along that road\n
    2 3 5 n means edge between 2&3 of length 5 and no bully is present
    \n''')
    cnt_bully_enc = 0
    edges = []
    while i < m:
        temp = input().split(' ')
        n1 = int(temp[0])
        n2 = int(temp[1])
        el = int(temp[2])
        if(temp[3] == 'b'):
            edges.append((el+int(1e10), n1, n2))
        else:
            edges.append((el, n1, n2))
        i += 1
    i = 1
    edges.sort(reverse=False)
    while i <= n:
        lead[i] = i
        rank[i] = 1
        nodelist.append(i)
        i += 1
    i = -1
    cost = 0
    while i < m:
        i += 1
        if i==m:
            break
        a = edges[i][1]
        b = edges[i][2] 
        if(leader(a) != leader(b)):
            if edges[i][0] > int(1e10):
                continue
            if rank[a] < rank[b]:
                lead[b] = lead[a]
                rank[a] += 1
            else:
                lead[a] = lead[b]
                rank[b] += 1
            cost += edges[i][0]
            edgelist.append((edges[i][1], edges[i][2], edges[i][0]))
    i=1
    flag=-1
    while i<=n:
        # print('Node:%d, leader:%d, rank: %d'%(i,lead[i],rank[i]))
        if lead[i]==i and rank[i]==1:
            print('Node %d not visited'%(i))
            flag=1
        i+=1
    if flag==-1:
        print('All nodes visited succesfully')
    print("COST:", cost)
    graphplot.drawGraph(node_list=nodelist,edge_list=edgelist)
