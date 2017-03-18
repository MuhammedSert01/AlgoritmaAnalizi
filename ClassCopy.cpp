#include <iostream>
using namespace std;
class myclass{
    int dizi[100];
    int index;
public:
    myclass(){
        item=0;
    }
    void add(int x);
    void print();
    myclass & operator=(myclass & x);
    int getDiziEleman(int i);
    int getIndex(){
        return item;
    };

};
void myclass::add(int x){
    myclass::dizi[item]=x;
    myclass::item++;

}
void myclass::print(){
    for(int i = 0; i < item; i++)
        cout << dizi[i] << " ";
    cout << endl;
}
int myclass::getDiziEleman(int x){
    return dizi[x];
}
myclass & myclass::operator=(myclass & x){
    for(int i=0; i< x.getIndex(); i++){
        this->add(x.getDiziEleman(i));
    }
}
int main()
{
    myclass a,b;
    a.add(1);
    a.add(2);
    a.add(3);
    a.add(4);
    a.add(5);
    b=a;
    b.print();
    cout << "KARMASIKLIK = " << "O(" << b.getIndex() << ") = O(n)" << end;
    return 0;
}