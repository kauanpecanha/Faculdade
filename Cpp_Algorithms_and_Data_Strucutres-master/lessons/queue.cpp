//queues

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

    Node(int v, Node *ptr)
    {
        info = v;
        next = ptr;
    }
};

class queue
{
    protected:
        Node *head, *tail;
    public:
        queue()
        {
            head = tail = 0;
        }
        void clearQ();
        bool isEmpty();
        void enqueue(int el);
        void dequeue();
        int firstEl();
        int lastEl();
        void printQueue();
    };

    void queue::clearQ()
    {
        Node *tmp = head;
        while(tmp!=NULL)
        {
            tmp=tmp->next;
            delete head;
            head = tmp;
        }
    }

    bool queue::isEmpty()
    {
        return (head == NULL);
    }

    void queue::enqueue(int el)
    {
        if(tail!=NULL)
        {
            tail->next = new Node(el, 0);
            tail = tail->next;
        }
        else
        {
            head = tail = new Node(el, 0);
        }
    }

    void queue::dequeue()
    {
        if(!isEmpty())
        {
            Node *tmp = head;

            if(head == tail)
            {
                head = tail = 0;
            }
            else
            {
                head = head->next;
                delete tmp;
            }
        }
        else
        {
            cout<<"A pilha esta vazia! Nao eh possivel deletar nenhum elemento."<<endl;
        }
    }

    int queue::lastEl()
    {
        Node *tmp = head;

        while(tmp->next != NULL)
        {
            tmp=tmp->next;
        }

        return(tmp->info);
    }

    int queue::firstEl()
    {
        if(head == NULL)
        {
            return -1;
        }
        else
        {
            return (head->info);
        }
    }

    void queue::printQueue()
    {
        Node *tmp = head;

        while(tmp!=NULL)
        {
            cout<<tmp->info<<" ";

            tmp=tmp->next;
        }
    }