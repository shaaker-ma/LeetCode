def numIslands(grid):
    
    def search(i,j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] == "0":
            return
        grid[i][j] = "0"
        search(i-1,j)
        search(i+1,j)
        search(i,j-1)
        search(i,j+1)
    
    count_island = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j]=="1"):
                search(i,j)
                count_island +=1
    return count_island
            

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslands(grid))  # Output: 3