#include<iostream>
using namespace std;

class Node
{
public:
    int info;
    Node *next;

    Node()
    {
        next = 0;
    }
    Node(int el, Node *pr)
    {
        info = el;
        next = pr;
    }
};

class Stack
{
public:
    Node *head;

    Stack()
    {
        head = 0;
    }
    void push(int el)
    {
        head = new Node(el, head);
        head->info = el;
    }
    void pop()
    {
        //cout<<"Elemento removido!"<<endl;
        popEl();

        if(head != NULL)
        {
            Node *tmp = head;
            head = head->next;
            delete tmp;
        }
    }
    int popEl()
    {
        if(head == NULL)
        {
            cout<<"\nPilha vazia!"<<endl;

            return -1;
        }
        else
        {
            return head->info;
        }
    }

    Node *returnHead()
    {
        if(head == NULL)
        {
            cout<<"\nPilha vazia!"<<endl;

            return NULL;
        }
        else
        {
            return head;
        }
    }
    void printStack()
    {
        Node *tmp = head;
        while(tmp!=NULL)
        {
            cout<<"\n"<<tmp->info;
            tmp = tmp->next;
        }
    }
    bool isEmpty()
    {
        if(head == NULL)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    int pilha_igual(Stack *x, Stack *y)
    {
        Node *aux1 = x->head; //ponteiro para head da pilha1
        Node *aux2 = y->head; //ponteiro para head da pilha2

    while (aux1!=NULL && aux2!=NULL) //enquanto alguma das duas pilhas não estiver vazia
    {
        if (aux1->info != aux2-> info) //se o elemento de determinada pilha for diferente de seu correspondente na segunda
        {
            return 0; //retorna 0(pilhas diferentes)
        }

        aux1=aux1->next; //o ponteiro aux1 passa a ser o próximo nó da pilha1
        aux2=aux2->next; //o ponteiro aux2 passa a ser o próximo nó da pilha2
    }

    return 1;
    }
};

int main()
{
    Stack s1, s2;

    int contador1 = 0, contador2 = 0, val;

    cout<<"Entre com os valores a serem inseridos na primeira pilha, a seguir:"<<endl;

    do
    {
        cin>>val;

        s1.push(val);

        contador1++;
    }
    while(contador1<5);

    cout<<"Resultado final:"<<endl;
    s1.printStack();
    cout<<endl;

    system("pause");

    cout<<"Entre com os valores a serem inseridos na segunda pilha, a seguir:"<<endl;

    do
    {
        cin>>val;

        s2.push(val);

        contador2++;
    }
    while(contador2<5);

    cout<<"Resultado final:"<<endl;
    s2.printStack();

    cout<<endl;
    cout<<endl;

    int aux = s1.pilha_igual(&s1, &s2);

    cout<<"Codigo: 1 para pilhas iguais, 2 para pilhas diferentes"<<endl;
    cout<<aux;

    if(aux == 1)
    {
        cout<<endl;
        cout<<"Pilhas iguais!"<<endl;
    }
    else
    {
        cout<<endl;
        cout<<"Pilhas diferentes"<<endl;
    }


}
