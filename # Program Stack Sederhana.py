# Program Stack Sederhana

stack = []

def push(data):
    stack.append(data)
    print(f"{data} berhasil ditambahkan ke stack.")

def pop():
    if len(stack) == 0:
        print("Stack kosong.")
    else:
        data = stack.pop()
        print(f"{data} dihapus dari stack.")

def display():
    if len(stack) == 0:
        print("Stack kosong.")
    else:
        print("Isi stack:", stack)


# Menambahkan data
push(10)
push(20)
push(30)

# Menampilkan stack
display()

# Menghapus data paling atas
pop()

# Menampilkan kembali
display()

def peek():
    if len(stack) > 0:
        print("Data paling atas:", stack[-1])
    else:
        print("Stack kosong")
        
peek()