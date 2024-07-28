import math

def kalkulator(Operator):
    try:
        Operator = Operator.replace('sin', 'math.sin')
        Operator = Operator.replace('cos', 'math.cos')
        Operator = Operator.replace('tan', 'math.tan')
        Operator = Operator.replace('log', 'math.log10')
        Operator = Operator.replace('ln', 'math.log')
        Operator = Operator.replace('sqrt', 'math.sqrt')
        Operator = Operator.replace('pi', 'math.pi')
        Operator = Operator.replace('e', 'math.e')
        
        while '!' in Operator:
            index = Operator.index('!')
            jumlah = ''
            while index > 0 and Operator[index - 1].isdigit():
                index -= 1
                jumlah = Operator[index] + jumlah
            result = math.factorial(int(jumlah))
            Operator = Operator.replace(jumlah + '!', str(result))
        
        # Evaluasi Operator
        hasil = eval(Operator)
        return hasil
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Ketik 'open' untuk masuk ke kalkulator atau Ketik 'exit' untuk keluar.")
    while True:
        command = input("Masukkan Perintah: ").strip().lower()
        if command == 'open':
            while True:
                inputKalkulator = input("Masukkan Angka atau 'exit' untuk keluar: ")
                if inputKalkulator.strip().lower() == 'exit':
                    break
                hasil = kalkulator(inputKalkulator)
                print("Hasil:", hasil)
        elif command == 'exit':
            print("Terima kasih telah menggunakan kalkulator.")
            break
        else:
            print("Perintah tidak dikenal, silakan coba lagi.")

if __name__ == "__main__":
    main()
