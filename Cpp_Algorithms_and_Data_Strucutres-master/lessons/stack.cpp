//pilhas

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
        Node(int el, Node *ptr)
        {
            info = el;
            next = ptr;
        }
};

class Stack
{
public:
    Node *head;

    Stack()
    {
        head = 0;
    }
    void clear();
    bool isEmpty();
    void push(int el);
    void pop();
    int popEl();
    void printStack();
};

void Stack::clear()
{
    Node *tmp = head;

    while(tmp != NULL)
    {
        tmp = tmp->next;
        delete head;
        head = tmp;
    }
}

void Stack::push(int el)
{
    head = new Node(el, head);
    head->info = el;
}

void Stack::pop()
{
    if(head!=NULL)
    {
        Node *tmp = head;
        head = head->next;
        delete tmp;
    }
    else
    {
        cout<<endl<<"A pilha esta vazia!"<<endl;
    }
}

void Stack::printStack()
{
    Node *tmp = head;

    while(tmp!=NULL)
    {
        cout<<endl<<tmp->info;
        if(tmp == head)
        {
            cout<<" (head)";
        }
        tmp = tmp->next;
    }
}