#include<iostream>
#include<queue>
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

        int printInOrder(TreeNode *r) //fun��o de impress�o de uma �rvore em In-Order
        {
            if(r==NULL)
            {
                return -1;
            }
            else
            {
                int x = r->value;

                printInOrder(r->left);
                return x;
                printInOrder(r->right);
            }
        }

        int countingNodes(TreeNode *r) //rotina para contar quantos n�s h� em determinada �rvore
        {
            if(r==NULL)
            {
                return 0;
            }
            else
            {
                return 1 + countingNodes(r->left) + countingNodes(r->right);
            }
        }

        int countingLeafs(TreeNode *r) //rotina para contar quantas folhas h� nesta �rvore
        {
            if(r==NULL)
            {
                return 0;
            }
            else
            {
                if((r->left==NULL)&&(r->right==NULL))
                {
                    return 1;
                }
                else
                {
                    return countingLeafs(r->left)+countingLeafs(r->right);
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
        void nodeData(TreeNode *r)
        {
            TreeNode *tmp = r;
            int altura = 0;

            if(tmp==NULL)
            {
                return;
            }
            else
            {
                cout<<"Valor do noh: "<<tmp->value<<endl;
                cout<<"Altura deste noh: "<<alturaSub(tmp, tmp->value)<<endl;
                cout<<endl;


                if(tmp->left!=NULL&&tmp->right!=NULL)
                {
                    nodeData(r->left);
                    nodeData(r->right);
                }
                else if(tmp->left!=NULL)
                {
                    nodeData(r->left);
                }
                else if(tmp->right!=NULL)
                {
                    nodeData(r->right);
                }
                else
                {
                    return;
                }
            }
        }

        TreeNode *findNode(TreeNode *r, int v)
        {
            if(r==NULL)
            {
                return NULL;
            }
            else
            {
                TreeNode *tmp = r;

                if(tmp->value == v)
                {
                    return tmp;
                }
                else if(tmp->value > v)
                {
                     return findNode(r->left, v);
                }
                else
                {
                     return findNode(r->right, v);
                }
            }
        }
        int alturaSub(TreeNode *r, int v)
        {
            TreeNode *tmp = findNode(r, v);
            if(tmp!=NULL)
            {
                return height(tmp);
            }
            else
            {
                return -1;
            }
        }
        void deleteLeafs(TreeNode *r) //rotina pra apagar todas as folhas
        {
            queue <int> captureLeafs;
            TreeNode *tmp = r;
            TreeNode *aux;

            if(tmp==NULL) //se n�o houver �rvore
            {
                return;
            }
            else //do contr�rio, executar o seguinte:
            {
                if(tmp->left == NULL && tmp->right == NULL)
                { // se os filhos � esquerda e direitas forem iguais a NULL, enviar o valor armazenado neste n� para a fila
                    captureLeafs.push(tmp->value);
                }
                else if(tmp->left != NULL)
                { //se houver filho � esquerda, executar recursivamente esta mesma fun��o para o filho � esquerda
                    deleteLeafs(tmp->left);
                }
                else
                { // do contr�rio, executar para o filho � direita
                    deleteLeafs(tmp->right);
                }
            }
            while(!captureLeafs.empty()) //enquanto houverem valores na fila, executar:
            {
                aux = findNode(r, captureLeafs.front()); //vari�vel tempor�ria que armazena o primeiro n� da fila
                deleteNode(r, aux->value); //execu��o da fun��o de dele��o de n�, para o n� folha
            }
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

        TreeNode *deleteNode(TreeNode *r, int v) //rotina de dele��o de um n�
        {
            if (r == NULL)
            {
                return NULL;
            }
            else if (v < r -> value)
            {
                r -> left = deleteNode(r -> left, v);
            }
            else if (v > r -> value)
            {
                r -> right = deleteNode(r -> right, v);
            }
            else
            {
                if (r -> left == NULL)
                {
                    TreeNode *temp = r -> right;
                    delete r;
                    return temp;
                }
                else if(r -> right == NULL)
                {
                    TreeNode *temp = r -> left;
                    delete r;
                    return temp;
                }
                else
                {
                    TreeNode *temp = minValueNode(r -> right);
                    r -> value = temp -> value;
                    r -> right = deleteNode(r -> right, temp -> value);
                }
            }
            return r;
        }

        TreeNode *minValueNode(TreeNode *node) //rotina de determina��o do menor n� na BST
        {
            TreeNode *current = node;

            while (current -> left != NULL)
            {
                current = current -> left;
            }
            return current;
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

    cout<<endl;
    cout<<"Arvore antes: "<<endl;
    obj.print2D(obj.root, 5);

    obj.deleteLeafs(obj.root);
    cout<<"Arvore depois: "<<endl;
    obj.print2D(obj.root, 5);


    return 0; //FIM DO PROGRAMA
}
