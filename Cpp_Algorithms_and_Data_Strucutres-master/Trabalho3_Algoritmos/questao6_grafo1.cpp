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
        if (val == 0)
        {
            cout << "\n Nao existem vértice incidentes do noh "<< v1;
        }
	}
};

int main()
{
	int n, valor, m;

    cout<<"Entre com os nohs do primeiro grafo(a = 1, b = 2, c = 3, d = 4, e = 5, f = 6):\n"<<endl;

	cout << "\n O grafo tera quantos vertices? (qtd de nohs do primeiro grafo: 6)";
	cin >> n;

	Grafo grafo(n);

	cout << "\n insira os Vertices no grafo";
	for (int i=0;i<n;i++)
	{
		cout << "\n Insira o valor do vertice no indice " << i << " do array (a = 1, b = 2, c = 3, d = 4, e = 5, f = 6): ";
		cin >> valor;
		grafo.InsereVertice(valor);
	}
	grafo.printVertices();

	cout<<endl;
	cout<<"Fase de determinacao de arestas do grafo!"<<endl;

    grafo.adicionarAresta(1,2);
    grafo.adicionarAresta(1,6);

    grafo.adicionarAresta(2,1);
    grafo.adicionarAresta(2,3);
    grafo.adicionarAresta(2,4);
    grafo.adicionarAresta(2,6);

    grafo.adicionarAresta(3,2);
    grafo.adicionarAresta(3,3);
    grafo.adicionarAresta(3,6);

    grafo.adicionarAresta(4,2);
    grafo.adicionarAresta(4,3);
    grafo.adicionarAresta(4,6);

    grafo.adicionarAresta(5,4);
    grafo.adicionarAresta(5,6);

    grafo.adicionarAresta(6,1);
    grafo.adicionarAresta(6,2);
    grafo.adicionarAresta(6,3);
    grafo.adicionarAresta(6,4);
    grafo.adicionarAresta(6,5);

    cout<<endl<<endl;
    cout<<"Lista de Adjacencias:"<<endl;

    for(int i = 1; i<=n; i++)
    {
        grafo.printVerticeIncDo(i);
        cout<<endl;
    }

    int x;

    cout<< endl << endl;
    cout<<"Matriz de Adjacencias:"<<endl;

    for(int i = 1; i<=n; i++)
    {
        for(int j = 1; j<=n; j++)
        {
            x = grafo.verificaAresta(i, j);

            cout<<x<<" ";

            if(j%6 == 0)
            {
                cout<<endl;
            }
        }
    }

	return 0;
}
