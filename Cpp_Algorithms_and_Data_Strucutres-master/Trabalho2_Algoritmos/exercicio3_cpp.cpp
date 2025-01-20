#include<iostream>
#include<math.h>
using namespace std;

#define SPACE 10

class TreeNode //classe de nó
{
    public:
        TreeNode *left, *right; //declaração dos ponteiros que apontam para os nós da direita e esquerda
        int value; //key or data

        TreeNode() //construtor sem parâmetros do nó
        {
            value = 0;
            left = NULL;
            right = NULL;
        }
        TreeNode(int v) //construtor parametrizado
        {
            value = v;
            left = NULL;
            right = NULL;
        }
};

class BST
{
    public:
        TreeNode *root; //declaração do ponteiro que aponta para a raiz

        BST() //construtor de árvore sem parâmtros
        {
            root = NULL;
        }

        void insertNode(TreeNode *new_node) //função de inserção de um novo nó à árvore
        {
            if(root==NULL)
            {
                root = new_node;
                cout<<" Valor inserido como noh raiz"<<endl;
            }
            else
            {
                TreeNode *tmp = root;
                while(tmp!=NULL)
                {
                    if(new_node->value==tmp->value)
                    {
                        cout<<" Valor ja existente, insira outro valor!"<<endl;
                        return;
                    }
                    else if((new_node->value<tmp->value)&&(tmp->left==NULL))
                    {
                        tmp->left = new_node;
                        cout<<" Valor inserido a esquerda!"<<endl;
                        break;
                    }
                    else if((new_node->value<tmp->value))
                    {
                        tmp=tmp->left;
                    }
                    else if((new_node->value>tmp->value)&&(tmp->right==NULL))
                    {
                        tmp->right=new_node;
                        cout<<" Valor inserido a direita!"<<endl;
                        break;
                    }
                    else
                    {
                        tmp=tmp->right;
                    }
                }
            }
        }

        int height(TreeNode *r) //rotina pra determinar a altura de uma árvore
        {
            if(r==NULL)
            {
                return -1;
            }
            else
            {
                int lheight = height(r->left);
                int rheight = height(r->right);

                if(lheight>rheight)
                {
                    return(lheight + 1);
                }
                else
                {
                    return(rheight + 1);
                }
            }
        }
        TreeNode *rightRotate(TreeNode *y) //rotina que realiza a rotação da árvore para a direita(Right-Right Rotation)
        {
            TreeNode *x = y->left;
            TreeNode *T2 = x->right;

            // comandos de rotação
            x->right = y;
            y->left = T2;

            return x;
        }

        TreeNode *leftRotate(TreeNode *x) //rotina que realiza a rotação da árvore para a esquerda(Left-Left Rotation)
        {
            TreeNode *y = x->right;
            TreeNode *T2=y->left;

            // comandos de rotação
            y->left = x;
            x->right = T2;

            return y;
        }

        void print2D(TreeNode *r, int space) //melhor representação gráfica possível de uma BST ou AVL, no prompt
        {
            if(r == NULL)
            {
                return;
            }
            space += SPACE;
            print2D(r->right, space);
            cout<<endl;
            for(int i = SPACE; i < space; i++)
            {
                cout<<" ";
            }
            cout<<r->value<<"\n";
            print2D(r->left, space);
        }

        //Código Day-Stout-Warren (DSW)

        int makeBackbone(TreeNode *grand) //fase 1 - criação da espinha dorsal
        {
            int count = 0;
            TreeNode* tmp = grand->right;

            // percorrer enquanto tmp for diferente de NULL
            while (tmp)
            {

                //se o filho à esquerda de tmp for diferente de NULL, então fazer um Right Rotate
                if (tmp->left)
                {
                    TreeNode* oldTmp = tmp;
                    tmp = tmp->left;
                    oldTmp->left = tmp->right;
                    tmp->right = oldTmp;
                    grand->right = tmp;
                }

                //se o filho à direita de tmp for diferente de NULL, então adicionar 1 à variável count e
                //atravessar até a direita para "achatar" a bst
                else
                {
                    count++;
                    grand = tmp;
                    tmp = tmp->right;
                }
            }

        return count;
        }

        // função para comprimir a bst dada com sua raiz como raiz->direita
        void compress(TreeNode* grand, int m) //fase 2 - criação da bst balanceada
        {
            //criar ponteiro tmp para atravessar e comprimir tal bst
            TreeNode* tmp = grand->right;

            //atravessar e rotaacionar a raiz para a esquerda, 'm' vezes
            //para comprimir a forma espinha dorsal da bst
            for (int i = 0; i < m; i++)
            {
                TreeNode* oldTmp = tmp;
                tmp = tmp->right;
                grand->right = tmp;
                oldTmp->right = tmp->left;
                tmp->left = oldTmp;
                grand = tmp;
                tmp = tmp->right;
            }
        }

        TreeNode* balanceBST(TreeNode* root) //função para balancear a espinha dorsal e imprimir a bst balanceada
        {
            // criação de nó fictício com valor 0
            TreeNode* grand = new TreeNode(0);

            // atribuição do filho direito ao nó fictício como a raiz de bst
            grand->right = root;

            // conseguir a quantidade de nós na BST fornecida e
            //simultanemanete converter isso em uma lista ligada à direita
            int count = makeBackbone(grand);

            // pega a altura da árvore em que todos os nós estão completamente preenchidos
            int h = log2(count + 1); //análogo à fórmula fornecida no material

            // conseguir o número de nós até o penúltimo nível
            int m = pow(2, h) - 1;

            // rotação para a esquerda para o excesso de nós no último nível
            compress(grand, count - m);

            // rotação para a esquerda até m ter valor 0
            //finalização
            for (m = m / 2; m > 0; m /= 2)
            {
                compress(grand, m);
            }

            // retorno da árvore já balanceada
            return grand->right;
        }
        bool isInBST(TreeNode *r, int v)
        {
            if(r==NULL)
            {
                return false;
            }
            else
            {
                TreeNode *tmp = r;

                if(tmp->value == v)
                {
                    return true;
                }
                else if(tmp->value > v)
                {
                     return isInBST(r->left, v);
                }
                else
                {
                     return isInBST(r->right, v);
                }
            }
        }
};

int main()
{
    int contador = 0, val, lim, aux;
    BST obj;

    cout<<" Quantos numeros deseja?";
    cin>>lim;
    cout<<endl;

    while(contador<lim)
    {
        cout<<" INSERCAO DE ELEMENTOS"<<endl;
        cout<<endl;
        //insertion code

        cout<<" Entre com o valor a ser inserido na BST: ";
        cin>>val;
        cout<<endl;

        if(obj.isInBST(obj.root, val))
        {
            cout<<endl;
            cout<<" Este elemento ja se encontra na lista. Por favor, digite outro!"<<endl;

            continue;
        }

        TreeNode *new_node = new TreeNode(val);

        obj.insertNode(new_node);

        contador++;

        cout<<endl;
    }

    cout<<"Arvore inserida:"<<endl;
    obj.print2D(obj.root, 5);

    cout<<"Pressione ENTER para comecar o processo de linearizacao!"<<endl;
    system("pause");

    obj.root = obj.balanceBST(obj.root); //chamada da função responsável pelo método DSW

    obj.print2D(obj.root, 5);
    return 0; //FIM DO PROGRAMA
}
