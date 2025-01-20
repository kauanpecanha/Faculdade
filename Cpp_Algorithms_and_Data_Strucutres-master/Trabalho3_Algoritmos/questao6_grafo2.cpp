#include "iostream"
#include <list>
#include <algorithm> // função find
using namespace std;


int indice = 0;

class Node
{
public:
	int info;
	Node *next;

	Node()
	{
		next = 0;
	}
	Node(int el, Node *prx = 0)
	{
		info = el;
		next = prx;
	}
};

class List
{
private:
	Node *head, *tail;
public:
	List()
	{
		head = tail=0;
	}
	void addToTail(int el)
	{
		if (tail != 0)
        { // if list not empty;
			tail->next = new Node(el);
			tail = tail->next;
		}
		else head = tail = new Node(el);
	}
	int getHeadInfo()
	{
		return head->info;
	}
	Node *getHead()
	{
		return head;
	}
};


class Grafo
{
	int V;
	List *adj;
protected:
    int MA[50][50];
    Node *tail, *head;
public:
	Grafo(int Vert)
	{
	    V = Vert;
        adj = new List[V];
	}
	void InsereVertice(int Vert)
	{
	    adj[indice].addToTail(Vert);
        indice++;
	}
	void printVertices()
	{
	    for (int i=0; i < indice; i++)
        {
            printf("\n%d", adj[i].getHeadInfo());
        }
	}
	void adicionarAresta(int v1, int v2)
	{
	    int v1cont=0, v2cont=0, i;
            for (i=0; i < indice; i++)
            {
                if (v1 == adj[i].getHeadInfo())
                {
                    v1cont++;
                }
                if (v2 == adj[i].getHeadInfo())
                {
                    v2cont++;
                }
            }
            if (v1cont !=0  && v2cont !=0)
            {
                for (i=0; i < indice; i++)
                {
                    if (v1 == adj[i].getHeadInfo())
                    {
                        break;
                    }
                }
                cout << "\n Adicionar a aresta (" << v1 << "," << v2 << ")";
                adj[i].addToTail(v2);
            }
            else
            {
                if (v1cont==0)
                {
                    cout << "\n Nao foi possível adicionar a aresta (" << v1 << "," << v2 << " ) porque o vertice " << v1 << " nao consta no grafo";
                }
                if (v2cont==0)
                {
                    cout << "\n Nao foi possível adicionar a aresta (" << v1 << "," << v2 << " ) porque o vertice " << v2 << " nao consta no grafo";
                }
            }
	}

	int verificaAresta(int v1, int v2)
	{
	    int i; Node *tmp;
            for (i=0; i < indice; i++)
            {
                if (v1 == adj[i].getHeadInfo())
                {
                    break;
                }
            }

            tmp=adj[i].getHead();
            for ( tmp=tmp->next; tmp != 0 ; tmp = tmp->next)
            {
                if (tmp->info == v2)
                {
                    return 1;
                }
            }
            return 0;
    }

	void printVerticeIncDo(int v1)
	{
	    int i, val=0;
        for (i=0; i < indice; i++)
        {
            if (v1 == adj[i].getHeadInfo())
            {
                break;
            }
        }

        Node *tmp;
        tmp=adj[i].getHead();
        cout << v1 <<"| ";
        for( tmp=tmp->next; tmp != 0 ; tmp = tmp->next)
        {
            cout << tmp->info<<" ";
            val++;
        }

	}
};

int main()
{
	int n, valor, m;

    //---------------------------------------------------------------------------------------------------

    cout<<endl<<endl;
    cout<<"Entre com os nohs do segundo grafo(1, 2, 3, 4, 5):\n"<<endl;

	cout << "\n O grafo tera quantos vertices? (qtd de nohs do primeiro grafo: 5)";
	cin >> m;

	Grafo grafo2(m);

	cout << "\n insira os Vertices no grafo";
	for (int i=0;i<m;i++)
	{
		cout << "\n Insira o valor do vertice no indice " << i << " do array (a = 1, b = 2, c = 3, d = 4, e = 5, f = 6): ";
		cin >> valor;
		grafo2.InsereVertice(valor);
	}
	grafo2.printVertices();

	cout<<endl;
	cout<<"Fase de determinacao de arestas do grafo!"<<endl;

    grafo2.adicionarAresta(1,2);
    grafo2.adicionarAresta(1,3);
    grafo2.adicionarAresta(1,4);
    grafo2.adicionarAresta(1,5);

    grafo2.adicionarAresta(3,2);
    grafo2.adicionarAresta(3,4);
    grafo2.adicionarAresta(3,5);

    system("pause");

    cout<<endl<<endl;
    cout<<"Lista de Adjacencias:"<<endl;

    for(int i = 1; i<=m; i++)
    {
        grafo2.printVerticeIncDo(i);
        cout<<endl;
    }

    cout<< endl << endl;
    cout<<"Matriz de Adjacencias:"<<endl;

    int x;

    for(int i = 1; i<=m; i++)
    {
        for(int j = 1; j<=m; j++)
        {
            x = grafo2.verificaAresta(i, j);

            cout<<x<<" ";

            if(j%5 == 0)
            {
                cout<<endl;
            }
        }
    }

	return 0;
}
