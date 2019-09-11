class Solution:
    
    def floodFill(self, image, sr, sc, newColor):
        startingColor = image[sr][sc]
  
        self.visited = []
        self.doit(image, sr, sc, newColor, startingColor)
        return image
    def doit(self, image, x, y, newColor, startingColor):
        if ((x,y) in self.visited):
            return
        if (x < 0 or y < 0 or x >= len(image) or y >= len(image[0])):
            return
        if (image[x][y] == startingColor):
            self.visited.append((x,y))
            image[x][y] = newColor
            self.doit(image, x+1, y, newColor, startingColor)
            self.doit(image, x-1, y, newColor, startingColor)
            self.doit(image, x, y+1, newColor, startingColor)
            self.doit(image, x, y-1, newColor, startingColor)
        if (image[x][y] != startingColor):
            return
x = Solution()
out = x.floodFill(
    
[[0,0,0],
[0,1,1]],
1,1, 1 )
        
print(out)