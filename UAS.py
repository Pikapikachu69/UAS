# list opsi pilihan makanan dan aksi
food = [["BU", "Bakso Urat", 15000], 
        ["MA", "Mie Ayam", 12000], 
        ["NG", "Nasi Goreng Ayam", 12000], 
        ["ET", "Es Teh", 4000], 
        ["AG", "Ayam Goreng", 10000], 
        ["AGK", "Nasi Ayam Geprek Kriuk", 15000]]

# fungsi untuk menampilkan daftar menu
def show_menu():
    print("Menu :")
    for i in range(len(food)):
        print(f"{food[i][0]}: {food[i][1]} - Rp.{food[i][2]}")

# fungsi untuk menghitung total harga
def calculate_total_price(order_list):
    total_price = 0
    for i in range(len(order_list)):
        item = order_list[i]
        total_price += item[2] 
    return total_price

# fungsi untuk mengambil input dari user
def get_input():
    order_list = []
    show_menu()
    while True:
        order = input("Masukan item untuk mengorder makanan, atau 'q' untuk menyelesaikan order : ")
        if order.lower() == 'q':
            break
        else:
            item = next((item for item in food if item[0] == order.upper()), None)
            if item is not None:
                qty = int(input("Jumlah: "))
                item[2] = qty * item[2] 
                order_list.append(item)
                print(f"{item[1]} has been added to your order.")
            else:
                print("Menu tidak tersedia, mohon coba lagi.")
    return order_list

# fungsi untuk memproses pembayaran
def process_payment(total_price):
    while True:
        total_payment = int(input("Total Uang: Rp"))
        if total_payment < total_price:
            print("Mohon Maaf Uang Anda Tidak Cukup")
        else:
            change = total_payment - total_price
            print(f"Pembayaran Selesai. Terima Kasih")
            print(f"Kembalian anda adalah :  Rp {change}")
            break

# main program
order_list = get_input()
total_price = calculate_total_price(order_list)
print(f"Total price: Rp {total_price}")
process_payment(total_price)