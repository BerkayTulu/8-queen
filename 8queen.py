import random
import time

# Çakışma sayısını hesaplayan fonksiyon
def calc_conflicts(board):
    conflicts = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            # Eğer iki vezir aynı sütunda ya da aynı çaprazda ise çakışma vardır
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1
    return conflicts

# Bir tahtanın tüm komşularını (bir vezirin bir adım hareket edebileceği tüm tahtalar) döndüren fonksiyon
def get_neighbors(board):
    neighbors = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i] != j:
                neighbor = list(board)
                neighbor[i] = j
                neighbors.append((neighbor, calc_conflicts(neighbor)))
    return neighbors

# Hill Climbing algoritmasını uygulayan fonksiyon
def hill_climbing(board):
    current_conflicts = calc_conflicts(board)
    steps = 0
    while steps < 1000:
        neighbors = get_neighbors(board)
        min_conflict = min(neighbors, key=lambda x: x[1])
        
        # Eğer çakışma sayısı 0 ise, ideal çözüm bulunmuştur
        if current_conflicts == 0:  
            return board, current_conflicts, steps

        # Eğer en az çakışmalı komşu mevcut durumdan daha iyi değilse, döngüyü sonlandır
        if min_conflict[1] == current_conflicts:
            return board, current_conflicts, steps
        
        # En az çakışmalı komşuyu yeni durum olarak belirle
        board = min_conflict[0]
        current_conflicts = min_conflict[1]
        steps += 1  # Her döngü adımında steps değişkenini artır

    return board, current_conflicts, steps

def find_solution():
    random_starts = 0  # Rastgele başlangıç durumlarının sayısını tutan sayaç
    while True:
        # 8 vezir problemi için rastgele bir başlangıç tahtası oluştur
        initial_board = [random.randint(0, 7) for _ in range(8)]
        print("Initial board configuration: ", initial_board)

        # Hill Climbing algoritmasıyla çözüm ara
        solution = hill_climbing(initial_board)

        # Eğer çakışma sayısı 0 ise, ideal çözüm bulunmuştur ve çözümü döndür
        if solution[1] == 0:
            return solution, random_starts

        random_starts += 1  # Her yeni rastgele başlangıç durumu için sayaçı artır

# Tahtayı yazdıran fonksiyon
def print_board(board):
    for i in range(len(board)):
        row = ""
        for j in range(len(board)):
            if board[i] == j:
                row += "Q "
            else:
                row += ". "
        print(row)
    print("\n")

# Rastgele bir başlangıç tahtası oluştur
initial_board = [random.randint(0, 7) for _ in range(8)]
print("Initial board configuration: ", initial_board)

# Ana fonksiyonu çağır
start_time = time.time()
solution, random_starts = find_solution()
end_time = time.time()
elapsed_time = end_time - start_time
# Çözümü, çakışma sayısını ve adım sayısını yazdır
print("Final board configuration: ", solution[0])
print_board(solution[0])
print("Number of conflicts: ", solution[1])
print("Number of steps: ", solution[2])
print("Number of random starts: ", random_starts)

print("Elapsed time: {:.5f} seconds".format(elapsed_time))