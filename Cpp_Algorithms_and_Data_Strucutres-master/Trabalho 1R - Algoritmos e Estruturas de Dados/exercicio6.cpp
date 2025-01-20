//exercício 6 - fila
#include<iostream>
using namespace std;

class Queue
{
    private:
      int front;
      int rear;
      int arr[5];

    public:
        Queue()
        {
            front = -1;
            rear = -1;
            for (int i = 0; i < 5; i++)
            {
                arr[i] = 0;
            }
        }
        void enqueue(int val)
        {
            if (isFull())
            {
                cout << "Fila cheia!" << endl;
                return;
            }
            else if (isEmpty())
            {
                rear = 0;
                front = 0;
                arr[rear] = val;
            }
            else
            {
                rear++;
                arr[rear] = val;
            }

        }
        int count()
        {
            return (rear - front + 1);
        }
        void display()
        {
            cout << "Os valores armazenados nesta fila sao:" << endl;
            for (int i = 0; i < 5; i++)
            {
                cout << arr[i] << "  ";
            }
        }
        bool isEmpty()
        {
            if (front == -1 && rear == -1)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        bool isFull()
        {
            if (rear == 4)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        int dequeue()
        {
            int x = 0;
            if (isEmpty())
            {
                cout << "A fila esta vazia!" << endl;
                return x;
            }
            else if (rear == front)
            {
                x = arr[rear];
                rear = -1;
                front = -1;
                return x;
            }
            else
            {
                x = arr[front];
                arr[front] = 0;
                front++;
                return x;
            }
        }
};

void somas(Queue queue1, int *p, int *i)
{
    int somaImpares = 0, somaPares = 0, aux, cont;

    for(cont = 0; cont<5; cont++)
    {
        aux = queue1.dequeue();

        if(aux == 0)
        {
            break;
        }
        else if(aux % 2 == 0)
        {
            somaPares += aux;
        }
        else
        {
            somaImpares += aux;
        }
    } //até aqui, tudo correto

    *p = somaPares;
    *i = somaImpares;
}

int main()
{
    Queue q1;
    int value, contador = 0;

    cout<<"Entre com os 5 numeros a seguir:"<<endl;

    do
    {
        cin>>value;
        q1.enqueue(value);

        contador++;
    }
    while(contador<5);

    q1.display();

    int pares, impares;

    somas(q1, &pares, &impares);

    cout<<endl;
    cout<<"A soma dos pares eh equivalente a: "<<pares<<endl;
    cout<<"A soma dos impares eh equivalente a: "<<impares<<endl;

    return 0;
}
