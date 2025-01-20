#include<iostream>
#include<queue>
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

        int printInOrder(TreeNode *r) //função de impressão de uma árvore em In-Order
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

        int countingNodes(TreeNode *r) //rotina para contar quantos nós há em determinada árvore
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

        int countingLeafs(TreeNode *r) //rotina para contar quantas folhas há nesta árvore
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

            if(tmp==NULL) //se não houver árvore
            {
                return;
            }
            else //do contrário, executar o seguinte:
            {
                if(tmp->left == NULL && tmp->right == NULL)
                { // se os filhos à esquerda e direitas forem iguais a NULL, enviar o valor armazenado neste nó para a fila
                    captureLeafs.push(tmp->value);
                }
                else if(tmp->left != NULL)
                { //se houver filho à esquerda, executar recursivamente esta mesma função para o filho à esquerda
                    deleteLeafs(tmp->left);
                }
                else
                { // do contrário, executar para o filho à direita
                    deleteLeafs(tmp->right);
                }
            }
            while(!captureLeafs.empty()) //enquanto houverem valores na fila, executar:
            {
                aux = findNode(r, captureLeafs.front()); //variável temporária que armazena o primeiro nó da fila
                deleteNode(r, aux->value); //execução da função de deleção de nó, para o nó folha
            }
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

        TreeNode *deleteNode(TreeNode *r, int v) //rotina de deleção de um nó
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

        TreeNode *minValueNode(TreeNode *node) //rotina de determinação do menor nó na BST
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
