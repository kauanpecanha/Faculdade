#include<iostream>
#include<math.h>
using namespace std;

#define SPACE 10

class TreeNode //classe de n�
{
    public:
        TreeNode *left, *right; //declara��o dos ponteiros que apontam para os n�s da direita e esquerda
        int value; //key or data

        TreeNode() //construtor sem par�metros do n�
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
        TreeNode *root; //declara��o do ponteiro que aponta para a raiz

        BST() //construtor de �rvore sem par�mtros
        {
            root = NULL;
        }

        void insertNode(TreeNode *new_node) //fun��o de inser��o de um novo n� � �rvore
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

        int height(TreeNode *r) //rotina pra determinar a altura de uma �rvore
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
        TreeNode *rightRotate(TreeNode *y) //rotina que realiza a rota��o da �rvore para a direita(Right-Right Rotation)
        {
            TreeNode *x = y->left;
            TreeNode *T2 = x->right;

            // comandos de rota��o
            x->right = y;
            y->left = T2;

            return x;
        }

        TreeNode *leftRotate(TreeNode *x) //rotina que realiza a rota��o da �rvore para a esquerda(Left-Left Rotation)
        {
            TreeNode *y = x->right;
            TreeNode *T2=y->left;

            // comandos de rota��o
            y->left = x;
            x->right = T2;

            return y;
        }

        void print2D(TreeNode *r, int space) //melhor representa��o gr�fica poss�vel de uma BST ou AVL, no prompt
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

        //C�digo Day-Stout-Warren (DSW)

        int makeBackbone(TreeNode *grand) //fase 1 - cria��o da espinha dorsal
        {
            int count = 0;
            TreeNode* tmp = grand->right;

            // percorrer enquanto tmp for diferente de NULL
            while (tmp)
            {

                //se o filho � esquerda de tmp for diferente de NULL, ent�o fazer um Right Rotate
                if (tmp->left)
                {
                    TreeNode* oldTmp = tmp;
                    tmp = tmp->left;
                    oldTmp->left = tmp->right;
                    tmp->right = oldTmp;
                    grand->right = tmp;
                }

                //se o filho � direita de tmp for diferente de NULL, ent�o adicionar 1 � vari�vel count e
                //atravessar at� a direita para "achatar" a bst
                else
                {
                    count++;
                    grand = tmp;
                    tmp = tmp->right;
                }
            }

        return count;
        }

        // fun��o para comprimir a bst dada com sua raiz como raiz->direita
        void compress(TreeNode* grand, int m) //fase 2 - cria��o da bst balanceada
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

        TreeNode* balanceBST(TreeNode* root) //fun��o para balancear a espinha dorsal e imprimir a bst balanceada
        {
            // cria��o de n� fict�cio com valor 0
            TreeNode* grand = new TreeNode(0);

            // atribui��o do filho direito ao n� fict�cio como a raiz de bst
            grand->right = root;

            // conseguir a quantidade de n�s na BST fornecida e
            //simultanemanete converter isso em uma lista ligada � direita
            int count = makeBackbone(grand);

            // pega a altura da �rvore em que todos os n�s est�o completamente preenchidos
            int h = log2(count + 1); //an�logo � f�rmula fornecida no material

            // conseguir o n�mero de n�s at� o pen�ltimo n�vel
            int m = pow(2, h) - 1;

            // rota��o para a esquerda para o excesso de n�s no �ltimo n�vel
            compress(grand, count - m);

            // rota��o para a esquerda at� m ter valor 0
            //finaliza��o
            for (m = m / 2; m > 0; m /= 2)
            {
                compress(grand, m);
            }

            // retorno da �rvore j� balanceada
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

    obj.root = obj.balanceBST(obj.root); //chamada da fun��o respons�vel pelo m�todo DSW

    obj.print2D(obj.root, 5);
    return 0; //FIM DO PROGRAMA
}
