import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_GREEN = (0, 150, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇游戏")
clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 24)

class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.grow = False
        self.alive = True
    
    def reset(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.grow = False
        self.alive = True
    
    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        
        if new_head in self.body:
            return False
        
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        self.grow = False
        return True
    
    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction
    
    def check_collision(self):
        head = self.body[0]
        if (head[0] < 0 or head[0] >= GRID_WIDTH or 
            head[1] < 0 or head[1] >= GRID_HEIGHT):
            return True
        return False

def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (WIDTH, y))

def main():
    snake = Snake()
    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    score = 0
    game_state = "start"
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if game_state == "start":
                    if event.key == pygame.K_SPACE:
                        game_state = "playing"
                elif game_state == "playing":
                    if event.key == pygame.K_UP:
                        snake.change_direction((0, -1))
                    elif event.key == pygame.K_DOWN:
                        snake.change_direction((0, 1))
                    elif event.key == pygame.K_LEFT:
                        snake.change_direction((-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        snake.change_direction((1, 0))
                elif game_state == "gameover":
                    if event.key == pygame.K_r:
                        snake.reset()
                        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
                        while food in snake.body:
                            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
                        score = 0
                        game_state = "start"
        
        screen.fill(BLACK)
        draw_grid()
        
        if game_state == "start":
            title_text = font.render("贪吃蛇", True, GREEN)
            start_text = font.render("按 空格键 开始游戏", True, WHITE)
            title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
            start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
            screen.blit(title_text, title_rect)
            screen.blit(start_text, start_rect)
        
        elif game_state == "playing":
            if not snake.move():
                game_state = "gameover"
            
            if snake.check_collision():
                game_state = "gameover"
            
            head = snake.body[0]
            if head == food:
                snake.grow = True
                score += 10
                food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
                while food in snake.body:
                    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            
            for i, segment in enumerate(snake.body):
                color = DARK_GREEN if i > 0 else GREEN
                pygame.draw.rect(screen, color, 
                               (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, 
                                GRID_SIZE - 2, GRID_SIZE - 2), border_radius=4)
            
            pygame.draw.rect(screen, RED,
                            (food[0] * GRID_SIZE, food[1] * GRID_SIZE,
                             GRID_SIZE - 2, GRID_SIZE - 2), border_radius=4)
            
            score_text = font.render(f"得分: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))
        
        elif game_state == "gameover":
            for i, segment in enumerate(snake.body):
                color = DARK_GREEN if i > 0 else GREEN
                pygame.draw.rect(screen, color, 
                               (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, 
                                GRID_SIZE - 2, GRID_SIZE - 2), border_radius=4)
            
            pygame.draw.rect(screen, RED,
                            (food[0] * GRID_SIZE, food[1] * GRID_SIZE,
                             GRID_SIZE - 2, GRID_SIZE - 2), border_radius=4)
            
            gameover_text = font.render("Game Over", True, RED)
            final_score_text = font.render(f"最终得分: {score}", True, WHITE)
            restart_text = font.render("按 R 重新开始", True, WHITE)
            
            gameover_rect = gameover_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60))
            score_rect = final_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
            
            screen.blit(gameover_text, gameover_rect)
            screen.blit(final_score_text, score_rect)
            screen.blit(restart_text, restart_rect)
        
        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()
