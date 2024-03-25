
def get_width_between_points(start_pos, end_pos):
    return ((start_pos[0] - end_pos[0])**2 +(start_pos[1] - end_pos[1])**2)**0.5


def write_output_to_file(output_file_name, width, path):
    file = open(f'../resources/{output_file_name}', 'w')
    file.write(str(width) + '\n')
    file.write(str(path))
    file.close()


def get_path(from_vertex, start_pos, end_pos):
    path = []
    while end_pos != start_pos:
        path.append(end_pos)
        end_pos = from_vertex[end_pos]
    path.append(start_pos)
    return path[::-1]


def find_min_chess_horse_path_and_length(input_file_name, output_file_name):
    file = open(f'../resources/{input_file_name}', 'r')
    try:
        chessboard_size = int(file.readline())
        start_pos = tuple(map(int, file.readline().split(', ')))
        end_pos = tuple(map(int, file.readline().split(', ')))
    except ValueError:
        write_output_to_file(output_file_name, -1, [None])
        file.close()
        return
    file.close()

    queue = [start_pos]
    dist_to = {
        start_pos: 0,
    }
    from_vertex = {
        start_pos: None,
    }
    visited = set()

    while queue:
        vertex = queue.pop(0)
        if vertex in visited:
            continue
        visited.add(vertex)
        if vertex == end_pos:
            # return dist_to[vertex], get_path(from_vertex, start_pos, end_pos)
            write_output_to_file(output_file_name, dist_to[vertex], get_path(from_vertex, start_pos, end_pos))
        for potential_move in [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]:
            row, col = vertex[0] + potential_move[0], vertex[1] + potential_move[1]
            if 0 > row * col or row * col >= chessboard_size**2 or (row, col) in visited:
                continue
            if get_width_between_points((row, col), end_pos) < get_width_between_points(vertex, end_pos):
                queue.append((row, col))
                dist_to[(row, col)] = dist_to[vertex] + 1
                from_vertex[(row, col)] = vertex


# find_min_chess_horse_path_and_length(input_file_name='given_input.txt', output_file_name='output.txt')
