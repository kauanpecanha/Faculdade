#include<iostream>
using namespace std;

#define SPACE 10

class TreeNode
{
    public:
        TreeNode *left, *right;
        int value; //key or data

        TreeNode()
        {
            value = 0;
            left = NULL;
            right = NULL;
        }
        TreeNode(int v)
        {
            value = v;
            left = NULL;
            right = NULL;
        }
};

class BST
{
    public:
        TreeNode *root;

        BST()
        {
            root = NULL;
        }

        bool isEmpty() //função para determinação da situação de preenchimento da árvore
        {
            if(root==NULL)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        void insertNode(TreeNode *new_node) //função de inserção de um novo nó à árvore
        {
            if(root==NULL)
            {
                root = new_node;
                cout<<"Value inserted as root node"<<endl;
            }
            else
            {
                TreeNode *tmp = root;
                while(tmp!=NULL)
                {
                    if(new_node->value==tmp->value)
                    {
                        cout<<"Value already exist,"
                        <<"Insert another value!"<<endl;
                        return;
                    }
                    else if((new_node->value<tmp->value)&&(tmp->left==NULL))
                    {
                        tmp->left = new_node;
                        cout<<"Value inserted to the left!"<<endl;
                        break;
                    }
                    else if((new_node->value<tmp->value))
                    {
                        tmp=tmp->left;
                    }
                    else if((new_node->value>tmp->value)&&(tmp->right==NULL))
                    {
                        tmp->right=new_node;
                        cout<<"Value inserted to the right!"<<endl;
                        break;
                    }
                    else
                    {
                        tmp=tmp->right;
                    }
                }
            }
        }
        void print2D(TreeNode *r, int space)
        {
            if(r==NULL)
            {
                return; //red
            }
            space += SPACE; //
            print2D(r->right, space); //red
            cout<<endl;
            for(int i = SPACE; i<space; i++)
            {
                cout<<" ";
            }
            cout<<r->value<<"\n"; // red
            print2D(r->left, space); //red
        } //os comandos red são os únicos NÃO RESPONSÁVEIS por imprimir os espaços

        void printPreOrder(TreeNode *r)
        { //*r é um ponteiro que inicialmente aponta para o nó raiz
            if(r==NULL) //se o nó raiz não existir, então esta função será impedida de executar
            {
                return; //fim da função
            }
            else
            {
                cout<<r->value; //impressão do N (node)
                printPreOrder(r->left); //impressão do R (right)
                printPreOrder(r->right); //impressão do L (left)
            }
        } //note que a recursividade é uma funcionalidade essencial para a perfeita execução deste código de pre-order

        void printInOrder(TreeNode *r)
        {
            if(r==NULL)
            {
                return;
            }
            else
            {
                printInOrder(r->left);
                cout<<r->value;
                printInOrder(r->right);
            }
        }
        void printPostOrder(TreeNode *r)
        {
            if(r==NULL)
            {
                return;
            }
            else
            {
                printPostOrder(r->left);
                printPostOrder(r->right);
                cout<<r->value;
            }
        }

        TreeNode *iteractiveSearch(int v)
        {
            if(root==NULL)
            {
                return 0;
            }
            else
            {
                TreeNode *tmp = root;

                while(tmp!=NULL)
                {
                    if(v == tmp->value)
                    {
                        return tmp;
                    }
                    else if(v<tmp->value)
                    {
                        tmp=tmp->left;
                    }
                    else
                    {
                        tmp=tmp->right;
                    }
                }
                return NULL;
            }
        }

        int height(TreeNode *r)
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
        void printGivenLevel(TreeNode *r, int level)
        {
            if(r==NULL)
            {
                return;
            }
            else if(level==0)
            {
                cout<<r->value<<endl;
            }
            else
            {
                printGivenLevel(r->left, level-1);
                printGivenLevel(r->right, level-1);
            }
        }
        void printLevelOrderBFS(TreeNode *r)
        {
            int h = height(r);
            for(int i = 0; i<=h; i++)
            {
                printGivenLevel(r, i);
            }
        }
        TreeNode *minValueNode(TreeNode *node)
        {
            TreeNode *current = node;

            while(current->left != NULL)
            {
                current = current->left;
            }
            return current;
        }
        TreeNode *deleteNode(TreeNode *r, int v)
        {
            if(r==NULL)
            {
                return NULL;
            }
            else if(v<r->value)
            {
                r->left = deleteNode(r->left, v);
            }
            else if(v>r->value)
            {
                r->right = deleteNode(r->right, v);
            }
            else
            {
                if(r->left == NULL)
                {
                    TreeNode *tmp = r->right;
                    delete r;
                    return tmp;
                }
                else if(r->right == NULL)
                {
                    TreeNode *tmp = r->left;
                    delete r;
                    return tmp;
                }
                else
                {
                    TreeNode *tmp = minValueNode(r->right);
                    r->value = tmp->value;
                    r->right = deleteNode(r->right, tmp->value);
                }
            }
            return r;
        }
};