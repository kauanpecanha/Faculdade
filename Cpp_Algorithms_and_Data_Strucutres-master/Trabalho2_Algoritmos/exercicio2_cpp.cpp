#include<iostream>
#define SPACE 10
using namespace std;

class TreeNode //classe de nós
{
    public:

        int value;
        TreeNode *left;
        TreeNode *right;

        TreeNode() //construtor sem parâmetros
        {
            value = 0;
            left = NULL;
            right = NULL;
        }

        TreeNode(int v) //construtor com parâmetros
        {
            value = v;
            left = NULL;
            right = NULL;
        }
};

class AVL //classe de árvore
{
    public:

        TreeNode *root;
        AVL() //construtor sem parâmetros
        {
            root = NULL;
        }

        bool isTreeEmpty() //função de determinação se a AVL está vazia
        {
            if(root == NULL)
            {
                return true;
            }
            else
            {
                return false;
            }
        }


  int height(TreeNode *r) //função de determinação da altura
  {
    if(r == NULL)
    {
        return -1;
    }
    else
    {
        //altura das subárvores(lheight = altura da subárvore da esquerda; rheight: da altura da subárvore da direita)
        int lheight = height(r->left);
        int rheight = height(r->right);


        if (lheight>rheight) //determinação da maior altura = altura da árvore
        {
            return (lheight + 1);
        }
        else
        {
            return (rheight + 1);
        }
    }
  }

  int balanceFactor(TreeNode *n) //rotina que determina o fator de balanceamento da árvore
  {
    if(n == NULL)
    {
        return -1;
    }
    return height(n -> left) - height(n -> right);
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
    y -> left = x;
    x -> right = T2;

    return y;
  }

  TreeNode *insert(TreeNode *r, TreeNode *newNode) //rotina de inserção de um nó à árvore
  {
    if(r == NULL)
    {
        r = newNode;
        cout << "Valor inserido com sucesso!" << endl;
        return r;
    }

    if(newNode->value < r->value)
    {
      r->left=insert(r->left, newNode);
    }
    else if(newNode->value > r->value)
    {
      r->right=insert(r->right, newNode);
    }
    else
    {
        cout<<"Valor ja inserido. Por favor, insira outro!"<<endl;
        return r;
    }

    int bf = balanceFactor(r); //o fator de balanceamento deve ser obtido através desta rotina, já definida anteriormente
    // Left Left Case
    if(bf > 1 && newNode->value < r->left->value)
    {//se o fator de balanceamento for maior que 1 e o valor do novo nó for menor que o à esquerda da raiz:
        return rightRotate(r); //performar a rotação para a direita
    }


    if (bf < -1 && newNode -> value > r -> right -> value)
    { //se o fator de balanceamento for menor que -1 e o valor do novo nó for maior que o à direita da raiz:
        return leftRotate(r); //performar a rotação para a esquerda
    }


    if(bf > 1 && newNode->value > r->left->value)
    { //se o fator de balanceamento for maior que 1 e o valor do novo nó for maior que o à esquerda da raiz:
        r->left = leftRotate(r->left); //deve haver uma rotação do tipo Left-Right
        return rightRotate(r);
    }


    if(bf < -1 && newNode->value < r->right->value)
    { //se o fator de balanceamento for maior que -1 e o valor do novo nó for menor que o à direita da raiz:
        r->right = rightRotate(r->right); //deve haver uma rotação do tipo Right-Left
        return leftRotate(r);
    }

    return r;

  }

  TreeNode *minimunNode(TreeNode *node) //rotina para percorrer a árvore até o nó mais à esquerda possível(o menor)
  {
    TreeNode *current = node;
    while(current->left!=NULL)
    {
        current = current->left; //direcionamento deste para seu filho imediato à esquerda
    }
    return current;
  }

  TreeNode *deleteNode(TreeNode *r, int v) //rotina para deletar nós + rebalanceamento
  {
    if(r == NULL) //condição necessária para a verificação de existência da árvore
    {
        return NULL;
    }
    else if(v < r->value)
    {
        r->left=deleteNode(r->left, v); //implementação recursiva
    }
    else if(v > r->value)
    {
        r->right=deleteNode(r->right, v);
    }
    else
    {
      if(r->left == NULL)
      {
        TreeNode *temp = r->right;
        delete r;
        return temp;
      }
      else if(r->right == NULL)
      {
        TreeNode *temp = r->left;
        delete r;
        return temp;
      }
      else
      {
        TreeNode *temp = minimunNode(r->right);
        r->value = temp->value;
        r->right = deleteNode(r->right, temp->value);
      }
    }

    //fase de verificação do balanceamento da árvore

    int bf = balanceFactor(r);
    // Rotação Left-Left
    if(bf == 2 && balanceFactor(r->left) >= 0)
    {
        return rightRotate(r);
    }
    // Rotação Left-Right
    else if(bf == 2 && balanceFactor(r->left) == -1)
    {
      r->left = leftRotate(r->left);
      return rightRotate(r);
    }
    // Rotação Right-Right
    else if(bf == -2 && balanceFactor(r->right) <= -0)
    {
        return leftRotate(r);
    }
    // Rotação Right-Left
    else if (bf == -2 && balanceFactor(r->right) == 1)
    {
      r->right = rightRotate(r->right);
      return leftRotate(r);
    }

    return r;
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

  void printPreorder(TreeNode *r) //rotina de impressão desta AVL em percurso Pre-Order
  {
    if (r == NULL)
    {
        return;
    }
    cout<<r->value<<" ";
    printPreorder(r->left);
    printPreorder(r->right);
  }

  void printInorder(TreeNode *r) //  Impressão da AVL em percurso In-Order
  {
    if (r == NULL)
    {
        return;
    }
    printInorder(r->left);
    cout<<r->value<<" ";
    printInorder(r->right);
  }

  void printPostorder(TreeNode *r) //Impressão da AVl em Post-Order
  {
    if (r == NULL)
    {
        return;
    }
    printPostorder(r->left);
    printPostorder(r->right);
    cout<<r->value<<" ";
  }

  void printGivenLevel(TreeNode *r, int level) //impressão de todos os nós em dado nível
  {
    if(r == NULL)
    {
        return;
    }
    else if(level == 0)
    {
        cout<<r->value<<" ";
    }
    else // level > 0
    {
      printGivenLevel(r->left, level - 1);
      printGivenLevel(r->right, level - 1);
    }
  }

  void printLevelOrderBFS(TreeNode *r) //impressão deste percurso em BFS(profundidade)
  {
    int h = height(r);
    for(int i = 0; i <= h; i++)
    {
        printGivenLevel(r, i);
    }
  }

  TreeNode *iterativeSearch(int v) //rotina de busca por um determinado elemento, utilizando iterações(loops)
  {
    if(root == NULL)
    {
        return root;
    }
    else
    {
      TreeNode *temp = root;
      while(temp != NULL)
      {
        if(v == temp->value)
        {
            return temp;
        }
        else if(v < temp->value)
        {
            temp = temp->left;
        }
        else
        {
            temp = temp->right;
        }
      }
      return NULL;
    }
  }

  TreeNode *recursiveSearch(TreeNode *r, int val) //rotina de busca por um determinado elemento, utilizando recursão
  {
    if(r == NULL || r -> value == val)
    {
        return r;
    }

    else if(val < r->value)
    {
        return recursiveSearch(r->left, val);
    }

    else
    {
        return recursiveSearch(r->right, val);
    }
  }

  void nodeData(TreeNode *r)
  {
      TreeNode *tmp = r;

      if(tmp==NULL)
      {
          return;
      }
      else
      {
          cout<<"Valor do noh: "<<tmp->value<<endl;
          cout<<"Fator de balanceamento: "<<balanceFactor(r)<<endl;
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

};

int main()
{
  AVL obj; //declaração do objeto obj do tipo AVL
  int option, val, aux; //a variável opção será utilizada para o controle de desejo do usuário; val, para inserção, deleção, etc

  do
  {
        cout<<" Que operacao gostaria de operar?";
        cout<<" Digite o numero da opcao. Entre com 0 para finalizar."<<endl;
        cout<<" 1. Insercao de um noh" <<endl;
        cout<<" 2. Procura de um noh especifico" <<endl;
        cout<<" 3. Delecao de um noh" <<endl;
        cout<<" 4. Impressao dos valores da AVL(2D, Pre O. , I.O , Post O.)" <<endl;
        cout<<" 5. Altura da arvore" <<endl;
        cout<<" 0. Finalizar programa" <<endl;

        cout<<endl;
        cout<<"Opcao selecionada: ";
        cin>>option;

        //declaração de um novo nó
        TreeNode *newNode = new TreeNode();

        switch(option) //utilização de uma estrutura switch para adequar a escolha do usuário
        {


        //caso 0 - finalização da função
        case 0:
            break;

        //caso 1 - inserção de um novo nó
        case 1:
            cout<<endl;
            cout<<" INSERCAO DE UM NOVO NOH" << endl;
            cout<<" Entre com o valor a ser inserido: ";
            cin>>val;


            newNode->value = val; //o valor inserido será armazenado no novo nó recém-criado


            obj.root = obj.insert(obj.root, newNode); //chamada da função de inserção
            cout<<endl;
            break;

        //caso 2 - Procura por um elemento específico, na AVL
        case 2:
            cout<<endl;
            cout<<" PROCURA POR UM NOH ESPECIFICO"<<endl;
            cout<<" Entre com o valor a ser procurado: ";
            cin>>val;


            //será utilizado o método de busca recursivo
            newNode = obj.recursiveSearch(obj.root, val); //chamada da função


            if(newNode != NULL)
            {
                cout<<" Valor encontrado! Ele eh:";
                cout<<newNode;
                cout<<endl;
            }
            else
            {
                cout<<" Valor nao encontrado"<<endl;
            }
            break;

        //caso 3 - deleção de um nó
        case 3:
            cout<<endl;
            cout<<" DELECAO DE UM NOH" << endl;
            cout<<" Entre com o valor a ser deletado, a seguir: ";
            cin>> val;
            newNode = obj.recursiveSearch(obj.root, val);
            if(newNode != NULL)
            {
                obj.root = obj.deleteNode(obj.root, val);
                cout<<" Valor deletado!"<<endl;

                cout<<"O fator de balanceamento de cada noh, apos esta delecao, sao:"<<endl;
                cout<<endl;
                obj.nodeData(obj.root);
            }
            else
            {
                cout << "Valor nao encontrado." << endl;
            }
            break;

        //caso 4 - impressao da AVL
        case 4:

            //impressao 2d

            cout<<endl;
            cout<<" IMPRESSAO 2D: "<<endl;
            obj.print2D(obj.root, 5);
            cout<<endl;

            //impressao BFS(profundidade)

            cout<<endl;
            cout <<" Print Level Order BFS: ";
            obj.printLevelOrderBFS(obj.root);
            cout <<endl;

            //impressao Pre-Order

            cout<<endl;
            cout <<" PRE-ORDER: ";
            obj.printPreorder(obj.root);
            cout<<endl;

            //impressao In-Order

            cout<<endl;
            cout <<" IN-ORDER: ";
            obj.printInorder(obj.root);
            cout<<endl;

            //impressao Post-Order

            cout<<endl;
            cout <<" POST-ORDER: ";
            obj.printPostorder(obj.root);
            cout<<endl;
            cout<<endl;

            break;


        //caso 5 - obtenção da altura da árvore
        case 5:
            cout<<endl;
            cout<<" Altura da arvore:"<<endl;

            aux = obj.height(obj.root);

            if(aux == -1)
            {
                cout<<" ainda inexistente!(-1)";
                cout<<"\n"<<endl;
            }
            else
            {
                cout<<" Altura: "<<aux<<endl;
                cout<<"\n"<<endl;
            }
            break;

        //caso base - não determinação de uma das opções
        default:
            cout<<endl;
            cout<<" Entre com uma das opcoes anteriormente citadas!"<<endl;
    }

  }while(option != 0);

  return 0; //FIM DO PROGRAMA
}
