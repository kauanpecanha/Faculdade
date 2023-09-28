#include<iostream>
#include<string>
using namespace std;

class aluno{
    public:
        string nome;
        string matric;
        string codTurmas[];
        
        aluno(){
            char nome;
            string matric;
        }
        void addInfo(string n, string m){
            nome = n;
            matric = m;
        }
};


int main(){

    aluno a1;
    string name;
    string matr;
    string codigo;

    cout<<"\nEntre com o nome do aluno: ";
    cin>>name;
    cout<<"\n"<<endl;
    cout<<"\nEntre com a matric deste aluno: ";
    cin>>matr;

    
    
    a1.addInfo(name, matr);

    cout<<"\nO nome do aluno 1 eh: "<<a1.nome<<" e sua matric eh: "<<a1.matric<<endl;

    for(int i = 0; i<=4; i++){
        cout<<"Entre com o codigo da disciplina: ";
        cin>>codigo;
    }

    return 0;
}