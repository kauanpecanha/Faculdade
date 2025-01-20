#include<iostream>
#define SPACE 10
using namespace std;

class TreeNode //classe de n�s
{
    public:

        int value;
        TreeNode *left;
        TreeNode *right;

        TreeNode() //construtor sem par�metros
        {
            value = 0;
            left = NULL;
            right = NULL;
        }

        TreeNode(int v) //construtor com par�metros
        {
            value = v;
            left = NULL;
            right = NULL;
        }
};

class AVL //classe de �rvore
{
    public:

        TreeNode *root;
        AVL() //construtor sem par�metros
        {
            root = NULL;
        }

        bool isTreeEmpty() //fun��o de determina��o se a AVL est� vazia
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


  int height(TreeNode *r) //fun��o de determina��o da altura
  {
    if(r == NULL)
    {
        return -1;
    }
    else
    {
        //altura das sub�rvores(lheight = altura da sub�rvore da esquerda; rheight: da altura da sub�rvore da direita)
        int lheight = height(r->left);
        int rheight = height(r->right);


        if (lheight>rheight) //determina��o da maior altura = altura da �rvore
        {
            return (lheight + 1);
        }
        else
        {
            return (rheight + 1);
        }
    }
  }

  int balanceFactor(TreeNode *n) //rotina que determina o fator de balanceamento da �rvore
  {
    if(n == NULL)
    {
        return -1;
    }
    return height(n -> left) - height(n -> right);
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
    y -> left = x;
    x -> right = T2;

    return y;
  }

  TreeNode *insert(TreeNode *r, TreeNode *newNode) //rotina de inser��o de um n� � �rvore
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

    int bf = balanceFactor(r); //o fator de balanceamento deve ser obtido atrav�s desta rotina, j� definida anteriormente
    // Left Left Case
    if(bf > 1 && newNode->value < r->left->value)
    {//se o fator de balanceamento for maior que 1 e o valor do novo n� for menor que o � esquerda da raiz:
        return rightRotate(r); //performar a rota��o para a direita
    }


    if (bf < -1 && newNode -> value > r -> right -> value)
    { //se o fator de balanceamento for menor que -1 e o valor do novo n� for maior que o � direita da raiz:
        return leftRotate(r); //performar a rota��o para a esquerda
    }


    if(bf > 1 && newNode->value > r->left->value)
    { //se o fator de balanceamento for maior que 1 e o valor do novo n� for maior que o � esquerda da raiz:
        r->left = leftRotate(r->left); //deve haver uma rota��o do tipo Left-Right
        return rightRotate(r);
    }


    if(bf < -1 && newNode->value < r->right->value)
    { //se o fator de balanceamento for maior que -1 e o valor do novo n� for menor que o � direita da raiz:
        r->right = rightRotate(r->right); //deve haver uma rota��o do tipo Right-Left
        return leftRotate(r);
    }

    return r;

  }

  TreeNode *minimunNode(TreeNode *node) //rotina para percorrer a �rvore at� o n� mais � esquerda poss�vel(o menor)
  {
    TreeNode *current = node;
    while(current->left!=NULL)
    {
        current = current->left; //direcionamento deste para seu filho imediato � esquerda
    }
    return current;
  }

  TreeNode *deleteNode(TreeNode *r, int v) //rotina para deletar n�s + rebalanceamento
  {
    if(r == NULL) //condi��o necess�ria para a verifica��o de exist�ncia da �rvore
    {
        return NULL;
    }
    else if(v < r->value)
    {
        r->left=deleteNode(r->left, v); //implementa��o recursiva
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

    //fase de verifica��o do balanceamento da �rvore

    int bf = balanceFactor(r);
    // Rota��o Left-Left
    if(bf == 2 && balanceFactor(r->left) >= 0)
    {
        return rightRotate(r);
    }
    // Rota��o Left-Right
    else if(bf == 2 && balanceFactor(r->left) == -1)
    {
      r->left = leftRotate(r->left);
      return rightRotate(r);
    }
    // Rota��o Right-Right
    else if(bf == -2 && balanceFactor(r->right) <= -0)
    {
        return leftRotate(r);
    }
    // Rota��o Right-Left
    else if (bf == -2 && balanceFactor(r->right) == 1)
    {
      r->right = rightRotate(r->right);
      return leftRotate(r);
    }

    return r;
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

  void printPreorder(TreeNode *r) //rotina de impress�o desta AVL em percurso Pre-Order
  {
    if (r == NULL)
    {
        return;
    }
    cout<<r->value<<" ";
    printPreorder(r->left);
    printPreorder(r->right);
  }

  void printInorder(TreeNode *r) //  Impress�o da AVL em percurso In-Order
  {
    if (r == NULL)
    {
        return;
    }
    printInorder(r->left);
    cout<<r->value<<" ";
    printInorder(r->right);
  }

  void printPostorder(TreeNode *r) //Impress�o da AVl em Post-Order
  {
    if (r == NULL)
    {
        return;
    }
    printPostorder(r->left);
    printPostorder(r->right);
    cout<<r->value<<" ";
  }

  void printGivenLevel(TreeNode *r, int level) //impress�o de todos os n�s em dado n�vel
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

  void printLevelOrderBFS(TreeNode *r) //impress�o deste percurso em BFS(profundidade)
  {
    int h = height(r);
    for(int i = 0; i <= h; i++)
    {
        printGivenLevel(r, i);
    }
  }

  TreeNode *iterativeSearch(int v) //rotina de busca por um determinado elemento, utilizando itera��es(loops)
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

  TreeNode *recursiveSearch(TreeNode *r, int val) //rotina de busca por um determinado elemento, utilizando recurs�o
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
  AVL obj; //declara��o do objeto obj do tipo AVL
  int option, val, aux; //a vari�vel op��o ser� utilizada para o controle de desejo do usu�rio; val, para inser��o, dele��o, etc

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

        //declara��o de um novo n�
        TreeNode *newNode = new TreeNode();

        switch(option) //utiliza��o de uma estrutura switch para adequar a escolha do usu�rio
        {


        //caso 0 - finaliza��o da fun��o
        case 0:
            break;

        //caso 1 - inser��o de um novo n�
        case 1:
            cout<<endl;
            cout<<" INSERCAO DE UM NOVO NOH" << endl;
            cout<<" Entre com o valor a ser inserido: ";
            cin>>val;


            newNode->value = val; //o valor inserido ser� armazenado no novo n� rec�m-criado


            obj.root = obj.insert(obj.root, newNode); //chamada da fun��o de inser��o
            cout<<endl;
            break;

        //caso 2 - Procura por um elemento espec�fico, na AVL
        case 2:
            cout<<endl;
            cout<<" PROCURA POR UM NOH ESPECIFICO"<<endl;
            cout<<" Entre com o valor a ser procurado: ";
            cin>>val;


            //ser� utilizado o m�todo de busca recursivo
            newNode = obj.recursiveSearch(obj.root, val); //chamada da fun��o


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

        //caso 3 - dele��o de um n�
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


        //caso 5 - obten��o da altura da �rvore
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

        //caso base - n�o determina��o de uma das op��es
        default:
            cout<<endl;
            cout<<" Entre com uma das opcoes anteriormente citadas!"<<endl;
    }

  }while(option != 0);

  return 0; //FIM DO PROGRAMA
}
