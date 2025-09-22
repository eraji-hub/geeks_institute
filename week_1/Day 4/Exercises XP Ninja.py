import time
import copy

class GameOfLife:
    def __init__(self, rows, cols, initial_state=None):
        self.rows = rows
        self.cols = cols
      
        if initial_state:
            self.grid = initial_state
        else:
            self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def display(self):
        for row in self.grid:
            line = ""
            for cell in row:
                line += "█" if cell else " "  
            print(line)
        print("\n" + "-" * self.cols)

    def count_live_neighbors(self, r, c):
        directions = [(-1,-1), (-1,0), (-1,1),
                      (0,-1),         (0,1),
                      (1,-1), (1,0), (1,1)]
        count = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                count += self.grid[nr][nc]
        return count

    def next_generation(self):
        new_grid = copy.deepcopy(self.grid)
        for r in range(self.rows):
            for c in range(self.cols):
                live_neighbors = self.count_live_neighbors(r, c)
                if self.grid[r][c] == 1:  
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[r][c] = 0  
                else:  
                    if live_neighbors == 3:
                        new_grid[r][c] = 1  
        self.grid = new_grid
if __name__ == "__main__":
  
    glider = [
        [0,0,1,0,0],
        [1,0,1,0,0],
        [0,1,1,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]

    game = GameOfLife(5, 5, glider)

    generations = 10
    for i in range(generations):
        print(f"Generation {i+1}:")
        game.display()
        game.next_generation()
        time.sleep(0.5)  
