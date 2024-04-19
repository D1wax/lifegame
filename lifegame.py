
import pygame

def colony_show(colony):
    for cell in colony:
        pygame.draw.rect(window, cell_color, 
                        (cell[0], cell[1], cell_size, cell_size))
            

clock = pygame.time.Clock()
pygame.init()



def field_net():
    for x in range(0, w_width, cell_size+1):
        for y in range(0, w_height, cell_size+1):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(window, t_color, rect, cell_size)

w_top = 0
w_left = 0
w_width = 1920
w_height = 1080

cell_size = 20
cell_color = (0, 0, 0)


t_x = 0
t_y = 0


t_width = 3
t_color = (150, 150, 150)


window = pygame.display.set_mode((w_width, w_height))

color_desk = (164, 120, 2)
window.fill(color_desk)


colony= []

is_setup = True
is_button_down = False
is_repeat = False

is_game = True

while is_game: 
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game = False

        elif event.type == pygame.MOUSEMOTION:
            m_x, m_y = pygame.mouse.get_pos()
            n_x = m_x  // cell_size
            n_y = m_y // cell_size
            if not(n_x == t_x and n_y == t_y):
                t_x = n_x
                t_y = n_y
                is_repeat = False
            else:
                is_repeat = True

            """
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                is_button_down = True
                is_repeat = False

            if event.type == pygame.MOUSEBUTTONUP:
                is_button_down = False
                is_repeat = False

            if is_button_down and not is_repeat:
                cell = []
                cell.append(t_x)
                cell.append(t_y)
                cell.append(0)
                colony_view(colony)
                pygame.draw.rect(window, t_color, (t_x * cell_size, t_y * cell_size, cell_size, cell_size), 3)
                pygame.display.flip()"""
            cursor = pygame.Rect( t_x, t_y, cell_size, cell_size)
            pygame.draw.rect(window, t_color, cursor, t_width)
            print(m_x, m_y)
            cursor.move_ip(event.rel)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cell = [m_x, m_y]
                
                if cell in colony and m_x % 2 == 0:
                    colony.remove(cell)
                else:
                    colony.append(cell)

    """    
    #if event.type == pygame.KEYDOWN and event.key in move_dict.keys():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            cell = [cur_x, cur_y]
            
            if cell in colony:
                colony.remove(cell)
            else:
                colony.append(cell)
        lst = [[[],[],[]],[]]
        if event.key == pygame.K_LEFT and cur_x > w_left:
            cur_x += -1
        if event.key == pygame.K_RIGHT and cur_x < w_width -1:
            cur_x += 1
        if event.key == pygame.K_UP and cur_y > w_top:
            cur_y += -1
        if event.key == pygame.K_DOWN and cur_y < w_height -1 :
            cur_y += 1
        cursor.update(cur_x * cell_size , cur_y * cell_size, cell_size, cell_size)


        cur_x = cur_x + move_dict[event.key][0]
        cur_y = cur_y + move_dict[event.key][1] 
        if cur_x < w_left: cur_x = w_left
        if cur_x > w_width: cur_x = w_width
        if cur_y < w_top: cur_y = w_left
        if cur_y > w_height: cur_x = w_width
        
        cursor.move_ip(move_dict[event.key][0]*cell_size, move_dict[event.key][1]*cell_size)
        """
    window.fill(color_desk)
    field_net()
    colony_show(colony)
    
    pygame.draw.rect(window, t_color, cursor, t_width)
    pygame.display.update()
    pygame.display.flip()
    
  

