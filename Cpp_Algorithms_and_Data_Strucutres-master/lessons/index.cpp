#include<iostream>
using namespace std;

class Node
{
    public:
        int info;
        Node *next;

        Node()
        {
            next = 0;
        }
        Node(int el, Node *ptr = 0)
        {
            info = el;
            next = ptr;
        }
};

class List
{
    public:
        Node *head;
        Node *tail;
        List()
        {
            head = tail = 0;
        }
        int isEmpty();
        void addToHead(int el);
        void addToTail(int el);
        int deleteFromHead();
        int deleteFromTail();
        void deleteNode(int);
        void printList(); 
};

void List::addToHead(int el)
{
    head = new Node(el, head);
    if(tail==0)
    {
        tail = head;
    }
}

void List::addToTail(int el)
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

int List::deleteFromHead()
{
    int el = head->info;
    Node *tmp = head;

    if(head == tail)
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

int List::deleteFromTail()
{
    int el = tail->info;
    if(head == tail)
    {
        delete head;
        head = tail = 0;
    }
    else
    {
        Node *tmp;
        for(tmp=head;tmp->next!=tail; tmp = tmp->next);
        delete tail;
        tail = tmp;
        tail->next = 0;
    }
    return el;
}

void List::deleteNode(int el)
{
    if(head != 0)
    {
        if(head == tail && el == head->info)
        {
            delete head;
            head = tail = 0;
        }
        else if(el == head->info)
        {
            Node *tmp = head;
            head = head->next;
            delete tmp;
        }
    }
    else
    {
        Node *pred, *tmp;
        for(pred = head, tmp = head->next; tmp!= 0 && !(tmp->info == el); pred = pred->next, tmp = tmp->next);

        if(tmp!= 0)
        {
            pred->next = tmp->next;
            if(tmp == tail)
            {
                tail = pred;
            }
            delete tmp;
        }
    }
}

void List::printList()
{
    Node *tmp = head;

    while(tmp!=NULL)
    {
        cout<<tmp->info<<" ";

        tmp = tmp->next;
    }
}

int main()
{
    List l1;
    int contador = 0;
    int val;

    do
    {
        l1.addToTail(contador);
        contador++;
    } while (contador<10);
    

    l1.printList();   

    return 0;
}