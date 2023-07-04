# rand関数を使用して1〜6のランダムな数字を出力するサンプルプログラム

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    # 乱数の種を設定する
    srand(time(NULL));

    # 1〜6のランダムな数字を生成して出力する
    int randomNumber = rand() % 6 + 1;
    printf("出力されたランダムな数字: %d\n", randomNumber);

    return 0;
}
