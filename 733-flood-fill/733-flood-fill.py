class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        colorToChange = image[sr][sc]
        self.DFS(sr, sc, image, newColor, colorToChange)
        
        return image
    
    def DFS (self, r, c, image, newColor, colorToChange):
        if r < 0 or c < 0 or r > len(image) - 1 or c > len(image[0]) - 1 or image[r][c] == newColor or image[r][c] != colorToChange:
            return 
        
        image[r][c] = newColor
        
        self.DFS(r + 1, c,image, newColor, colorToChange)
        self.DFS(r - 1, c,image, newColor, colorToChange)
        self.DFS(r, c + 1,image, newColor, colorToChange)
        self.DFS(r, c - 1,image, newColor, colorToChange)