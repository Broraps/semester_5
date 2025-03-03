#include <iostream>
#include <ctime>

using namespace std;

bool isPrime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }
    return true;
}

int main() {
    clock_t start = clock(); // Mulai mencatat waktu

    cout << "Bilangan prima antara 1 dan 500.000 adalah: ";
    for (int i = 1; i <= 500000; i++) {
        if (isPrime(i)) {
            cout << i << " ";
        }
    }

    clock_t end = clock(); // Akhiri pencatatan waktu
    double elapsed_time = double(end - start) / CLOCKS_PER_SEC; // Hitung waktu yang berlalu
    cout << "\nWaktu yang dibutuhkan: " << elapsed_time << " detik." << endl;

    return 0;
}
