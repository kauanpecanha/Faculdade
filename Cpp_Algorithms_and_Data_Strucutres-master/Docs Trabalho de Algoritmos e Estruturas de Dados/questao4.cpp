#include <iostream>
using namespace std;

class Node{ //declara��o da classe do n�

	public:

		Node(int el=0,Node *ptr=0)
		{
			info=el;
			next=ptr;
		}

		int info;
		Node *next;
};

class Stack{ //declara��o da classe de pilha

	public:

		Stack() // construtor
		{
			head=0;
		}

		void push(int el) //fun��o para adicionar um elemento � pilha
		{
			head=new Node(el, head);
		}

		void pop() //fun��o para excluir um elemento da pilha
		{
			if(head==0)
            {
				cout<<"\nPilha vazia"<<endl;
			}
			else if(head->next==0)
			{
				head=0;
			}
			else
            {
				Node *tmp=head->next;
				delete head;
				head=tmp;
			}
		}

		int popEl() //fun��o para excluir um elemento especifico
		{
			if(head == 0)
            {
				cout<<"\nPilha vazia"<<endl;
				return -1;
			}
			else
			{
				return head->info;
			}
		}
		void clear() //fun��o para excluir a pilha
		{
			Node *tmp=head;

			while(tmp!=0)
            {
                tmp=tmp->next;
				delete head;
				head=tmp;
			}
		}

		bool is_empty() //fun��o para determinar se a pilha est� vazia
		{
			return(head==0);
		}

		void printStack() //fun��o para imprimir a pilha
		{
			for(Node *tmp=head;tmp!=0;tmp=tmp->next)
            {
				cout<<"\nElemento:"<<tmp->info<<endl;
			}
		}

    private:
        Node *head;
};

class Queue //declara��o da classe de fila
{
	public:
		Queue() //construtor da fila
		{
			head=tail=0;
		}

		void enqueue(int el) //fun��o para enfileirar elementos
		{
			if(head == 0)
            {
				head=tail=new Node(el, 0);
			}
			else
			{
				tail->next=new Node(el, 0);
				tail=tail->next;
			}
		}

		void dequeue() //fun��o para desenfilar elementos
		{
			if(!is_empty())
                {
				cout<<"\nElemento removido: "<<firstEl();
				Node *tmp=head;

				if(head==tail)
                {
					head=tail=0;
				}
				else
				{
					head=head->next;
				}

				delete tmp;
			}
			else
            {
				cout<<"\nLista vazia, nao pode ser retirado nenhum elemento";
			}
		}

		int firstEl() //fun��o para retornar o primeiro elemento da fila
		{
			if(head==0)
			{
				cout<<"\nFila vazia"<<endl;
				return -1;
			}
			else
			{
				return head->info;
			}
		}

		void clear_queue() //fun��o para limpar a fila
		{
			Node *tmp = head;

			while(tmp!= 0)
            {
				tmp=tmp->next;
				delete head;
				head=tmp;
			}
		}

		bool is_empty() //fun��o para determinar se a fila est� vazia
		{
			return(head==0);
		}

		void print_queue() //fun��o para imprimir a fila
		{
			for(Node *tmp=head;tmp!=0;tmp=tmp->next)
            {
				cout<<"\nElemento:"<<tmp->info<<endl;
			}
		}

		void reverse_queue() //fun��o para reverter a fila
		{
			Stack p;

			for(Node *tmp=head;tmp!= 0;tmp=tmp->next)
            {
				p.push(tmp->info);
			}

			clear_queue();

			while(!p.is_empty())
            {
				enqueue(p.popEl());
				p.pop();
			}

		}
    private:
        Node *head, *tail;
};

int main()
{

	Queue q; //cria��o de uma fila

	q.enqueue(25);
	q.enqueue(05);
	q.enqueue(2004);
	q.enqueue(30);
	q.enqueue(03);
	q.enqueue(1974);

	cout<<"\nFila:"<<endl;
	q.print_queue();

	q.reverse_queue(); //momento da invers�o da fila

	cout<<"\nFila invertida:"<<endl;
	q.print_queue();

	return 0;
}

//fim do programa
