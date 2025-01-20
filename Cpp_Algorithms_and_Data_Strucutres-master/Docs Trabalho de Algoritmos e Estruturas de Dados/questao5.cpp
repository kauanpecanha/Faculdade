#include<iostream>
using namespace std;

class Node{ //declaração da classe do nó

	public:

		Node(int el=0,Node *ptr=0)
		{
			info=el;
			next=ptr;
		}

		int info;
		Node *next;
};


class List
{
    public:
        List() //construtor
        {
            head = tail = 0;
        }

        int isempty() //função que determina se a lista está vazia ou não
        {
            return head == 0;
        }

        void addtohead(int el) //função que adiciona um elemento(nó) no início da lista
        {
            head = new Node(el, head);
            if(tail==0)
            {
                tail = head;
            }
        }

        void addtotail(int el) //função que adiciona um elemento ao fim da lista
        {
            if(tail!=0)
            {
                tail->next = new Node(el);
                tail = tail->next;
            }
            else
            {
                head = tail = new Node(el);
            }
        }

        int deletefromhead()
        {
            int el = head->info;
            Node *tmp = head;

            if(head==tail)
            {
                head = tail = 0;
            }
            else
            {
                head = head->next;
            }

            delete tmp;

            return el;
        }

        int deletefromtail()
        {
            int el = tail->info;

            if(head==tail)
            {
                delete head;
                head = tail = 0;
            }
            else
            {
                Node *tmp;
                for(tmp=head;tmp->next!=tail;tmp = tmp->next);
                delete tail;
                tail = tmp;
                tail->next = 0;
            }

            return el;
        }

        bool isinlist(int el) const
        {
            Node *tmp;

            for(tmp=head;tmp!=0 && !(tmp->info==el);tmp=tmp->next);

            return tmp!=0;
        }

        void impressao()
        {
			for(Node*tmp=head;tmp!=0;tmp=tmp->next)
            {
				cout<<tmp->info<<endl;
			}
		}

    private:
        Node *head, *tail;
};


int main()
{
    List lista;

    bool primo(int num);

    int i = 1;

    //adicionado 10 números
    cout<<"\nAdicionando 10 numeros"<<endl;

    lista.addtohead(1);

    for(i=2;i<=10;i++)
    {
        lista.addtotail(i);
    }

    lista.impressao();

    system("pause");

    cout<<"\n\n"<<endl;
    //imprimir apenas os primos


    //inserir o número 14 no fim da lista

    cout<<"\nAdicionando 14 ao fim da lista"<<endl;

    lista.addtotail(14);

    lista.impressao();

    system("pause");

    cout<<"\n\n"<<endl;

    //ler um número e inseri-lo no meio da lista

    // ler um número e procurá-lo na lista, imprimindo a posição de sua primeira ocorrência a partir do início; se não estiver na lista, imprimir uma mensagem adequada


    return  0;
}

//fim do programa
