import pygame
import random
import sys
from typing import List, Tuple, Optional

# Pygame初期化
pygame.init()

# 定数
BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SCREEN_WIDTH = BLOCK_SIZE * (GRID_WIDTH + 8)
SCREEN_HEIGHT = BLOCK_SIZE * GRID_HEIGHT

# 色の定義
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)

# テトロミノの形状定義
TETROMINOES = {
    'I': {
        'shape': [(0, 0), (0, 1), (0, 2), (0, 3)],
        'color': CYAN
    },
    'O': {
        'shape': [(0, 0), (0, 1), (1, 0), (1, 1)],
        'color': YELLOW
    },
    'T': {
        'shape': [(0, 1), (1, 0), (1, 1), (1, 2)],
        'color': PURPLE
    },
    'S': {
        'shape': [(0, 1), (0, 2), (1, 0), (1, 1)],
        'color': GREEN
    },
    'Z': {
        'shape': [(0, 0), (0, 1), (1, 1), (1, 2)],
        'color': RED
    },
    'J': {
        'shape': [(0, 0), (1, 0), (1, 1), (1, 2)],
        'color': BLUE
    },
    'L': {
        'shape': [(0, 2), (1, 0), (1, 1), (1, 2)],
        'color': ORANGE
    }
}

class Tetromino:
    def __init__(self, x: int, y: int, shape: str):
        self.x = x
        self.y = y
        self.shape = shape
        self.rotation = 0
        self.color = TETROMINOES[shape]['color']
        self.blocks = TETROMINOES[shape]['shape']
    
    def get_blocks(self) -> List[Tuple[int, int]]:
        """現在の回転状態でのブロック位置を取得"""
        if self.shape == 'O':
            return self.blocks
        
        rotated = []
        for x, y in self.blocks:
            if self.rotation == 0:
                rotated.append((x, y))
            elif self.rotation == 1:
                rotated.append((-y, x))
            elif self.rotation == 2:
                rotated.append((-x, -y))
            elif self.rotation == 3:
                rotated.append((y, -x))
        
        return rotated
    
    def rotate(self):
        """テトロミノを回転"""
        self.rotation = (self.rotation + 1) % 4
    
    def move(self, dx: int, dy: int):
        """テトロミノを移動"""
        self.x += dx
        self.y += dy

class TetrisGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('テトリス')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        self.grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = None
        self.next_piece = None
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.game_over = False
        self.paused = False
        
        self.fall_time = 0
        self.fall_speed = 500  # ミリ秒
        
        self.spawn_new_piece()
        self.spawn_new_piece()
    
    def spawn_new_piece(self):
        """新しいテトロミノを生成"""
        if self.current_piece is None:
            self.current_piece = self.next_piece
        else:
            self.current_piece = self.next_piece
        
        shape = random.choice(list(TETROMINOES.keys()))
        self.next_piece = Tetromino(GRID_WIDTH // 2 - 1, 0, shape)
    
    def is_valid_position(self, piece: Tetromino, dx: int = 0, dy: int = 0) -> bool:
        """指定された位置が有効かチェック"""
        for x, y in piece.get_blocks():
            new_x = piece.x + x + dx
            new_y = piece.y + y + dy
            
            if (new_x < 0 or new_x >= GRID_WIDTH or 
                new_y >= GRID_HEIGHT or 
                (new_y >= 0 and self.grid[new_y][new_x] is not None)):
                return False
        return True
    
    def place_piece(self):
        """現在のピースをグリッドに配置"""
        for x, y in self.current_piece.get_blocks():
            grid_x = self.current_piece.x + x
            grid_y = self.current_piece.y + y
            if 0 <= grid_y < GRID_HEIGHT:
                self.grid[grid_y][grid_x] = self.current_piece.color
        
        self.clear_lines()
        self.spawn_new_piece()
        
        if not self.is_valid_position(self.current_piece):
            self.game_over = True
    
    def clear_lines(self):
        """完成したラインを消去"""
        lines_to_clear = []
        for y in range(GRID_HEIGHT):
            if all(cell is not None for cell in self.grid[y]):
                lines_to_clear.append(y)
        
        for y in lines_to_clear:
            del self.grid[y]
            self.grid.insert(0, [None for _ in range(GRID_WIDTH)])
        
        if lines_to_clear:
            self.lines_cleared += len(lines_to_clear)
            self.score += len(lines_to_clear) * 100 * self.level
            self.level = self.lines_cleared // 10 + 1
            self.fall_speed = max(50, 500 - (self.level - 1) * 50)
    
    def handle_input(self):
        """ユーザー入力の処理"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_p:
                    self.paused = not self.paused
                elif event.key == pygame.K_r and self.game_over:
                    self.__init__()
                
                if not self.paused and not self.game_over:
                    if event.key == pygame.K_LEFT:
                        if self.is_valid_position(self.current_piece, -1, 0):
                            self.current_piece.move(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        if self.is_valid_position(self.current_piece, 1, 0):
                            self.current_piece.move(1, 0)
                    elif event.key == pygame.K_DOWN:
                        if self.is_valid_position(self.current_piece, 0, 1):
                            self.current_piece.move(0, 1)
                    elif event.key == pygame.K_UP:
                        rotated_piece = Tetromino(self.current_piece.x, self.current_piece.y, self.current_piece.shape)
                        rotated_piece.rotation = (self.current_piece.rotation + 1) % 4
                        if self.is_valid_position(rotated_piece):
                            self.current_piece.rotate()
                    elif event.key == pygame.K_SPACE:
                        while self.is_valid_position(self.current_piece, 0, 1):
                            self.current_piece.move(0, 1)
        
        return True
    
    def update(self):
        """ゲーム状態の更新"""
        if self.paused or self.game_over:
            return
        
        current_time = pygame.time.get_ticks()
        if current_time - self.fall_time > self.fall_speed:
            if self.is_valid_position(self.current_piece, 0, 1):
                self.current_piece.move(0, 1)
            else:
                self.place_piece()
            self.fall_time = current_time
    
    def draw(self):
        """画面の描画"""
        self.screen.fill(BLACK)
        
        # グリッドの描画
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.grid[y][x]:
                    pygame.draw.rect(self.screen, self.grid[y][x],
                                   (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(self.screen, WHITE,
                                   (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
        
        # 現在のピースの描画
        if self.current_piece:
            for x, y in self.current_piece.get_blocks():
                screen_x = (self.current_piece.x + x) * BLOCK_SIZE
                screen_y = (self.current_piece.y + y) * BLOCK_SIZE
                if 0 <= self.current_piece.y + y < GRID_HEIGHT:
                    pygame.draw.rect(self.screen, self.current_piece.color,
                                   (screen_x, screen_y, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(self.screen, WHITE,
                                   (screen_x, screen_y, BLOCK_SIZE, BLOCK_SIZE), 1)
        
        # 右側の情報パネル
        panel_x = GRID_WIDTH * BLOCK_SIZE + 20
        
        # スコア
        score_text = self.font.render(f'スコア: {self.score}', True, WHITE)
        self.screen.blit(score_text, (panel_x, 20))
        
        # レベル
        level_text = self.font.render(f'レベル: {self.level}', True, WHITE)
        self.screen.blit(level_text, (panel_x, 60))
        
        # ライン数
        lines_text = self.font.render(f'ライン: {self.lines_cleared}', True, WHITE)
        self.screen.blit(lines_text, (panel_x, 100))
        
        # 次のピース
        next_text = self.font.render('次のピース:', True, WHITE)
        self.screen.blit(next_text, (panel_x, 160))
        
        if self.next_piece:
            for x, y in self.next_piece.get_blocks():
                screen_x = panel_x + x * BLOCK_SIZE + 20
                screen_y = 200 + y * BLOCK_SIZE
                pygame.draw.rect(self.screen, self.next_piece.color,
                               (screen_x, screen_y, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(self.screen, WHITE,
                               (screen_x, screen_y, BLOCK_SIZE, BLOCK_SIZE), 1)
        
        # 操作説明
        controls = [
            '操作説明:',
            '←→: 移動',
            '↓: 落下',
            '↑: 回転',
            'Space: 即座落下',
            'P: 一時停止',
            'R: リスタート',
            'ESC: 終了'
        ]
        
        for i, control in enumerate(controls):
            control_text = self.small_font.render(control, True, GRAY)
            self.screen.blit(control_text, (panel_x, 350 + i * 25))
        
        # ゲームオーバー表示
        if self.game_over:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(128)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))
            
            game_over_text = self.font.render('ゲームオーバー!', True, RED)
            restart_text = self.small_font.render('Rキーでリスタート', True, WHITE)
            
            self.screen.blit(game_over_text, 
                           (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 
                            SCREEN_HEIGHT // 2 - 50))
            self.screen.blit(restart_text, 
                           (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, 
                            SCREEN_HEIGHT // 2))
        
        # 一時停止表示
        if self.paused:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(128)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))
            
            pause_text = self.font.render('一時停止', True, WHITE)
            self.screen.blit(pause_text, 
                           (SCREEN_WIDTH // 2 - pause_text.get_width() // 2, 
                            SCREEN_HEIGHT // 2))
        
        pygame.display.flip()
    
    def run(self):
        """メインゲームループ"""
        running = True
        while running:
            running = self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

def main():
    """メイン関数"""
    print("テトリスゲームを開始します...")
    print("pygameライブラリが必要です。インストールされていない場合は以下のコマンドでインストールしてください:")
    print("pip install pygame")
    
    try:
        game = TetrisGame()
        game.run()
    except ImportError:
        print("エラー: pygameライブラリがインストールされていません。")
        print("以下のコマンドでインストールしてください:")
        print("pip install pygame")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()
