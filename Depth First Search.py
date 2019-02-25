
# coding: utf-8

# In[3]:


graphAL2 = {0 : [1,2,3],
        1 : [0,3,4],
        2 : [0,4,5],
        3 : [0,1,5],
        4 : [1,2],
        5 : [2,3] }

def main():
    count = 0
    graphAL2v = {}

    for key, value in graphAL2.items():
         graphAL2v[key] = 0

    print(graphAL2v)

    for key in graphAL2v: 
        if graphAL2v[key] == 0: 
            dfs(key, count, graphAL2, graphAL2v)

    print(graphAL2v)


def dfs(v, count, graphal, graphvisited):
    count = count + 1
    print("Visiting ",v)
    graphvisited[v] = count
    for elem in graphal[v]:
        if not graphvisited[elem]:
            dfs(elem, count, graphal, graphvisited)

main()

