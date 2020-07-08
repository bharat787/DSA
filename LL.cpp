#include <bits/stdc++.h>
using namespace std;

class Node {
    public: 
        int data;
        Node* next;
};

void printList(Node* n){
    while (n != NULL) {
        cout << n->data << " ";
        n = n->next;
    }
}

void push (Node** head_ref, int new_data){
    Node* new_node = new Node();
    new_node -> data = new_data;
    new_node -> next = (*head_ref);
    (*head_ref) = new_node;
}

void insertAfer (struct Node* prev_node, int new_data){
    if (prev_node == NULL){
        printf("the given previous node cannot be NULL");
        return;
    }

    struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));

    new_node -> data = new_data;
    new_node -> next = prev_node->next;
    prev_node -> next = new_node;
    
    }

void append ( struct Node** head_ref, int new_data){
    struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));

    struct Node* last = *head_ref;

    new_node -> data = new_data;
    new_node -> next = NULL;

    if (*head_ref == NULL){
        *head_ref = new_node;
        return;
    }

    while (last->next != NULL){
        last = last->next;
    }

    last ->next = new_node;
    return;
}

int main () {
    Node* head = NULL;
    // Node* second = NULL;
    // Node* third = NULL;

    // //allocate new nodes
    // head = new Node();
    // second = new Node();
    // third  = new Node();

    // head->data = 1;
    // head->next = second;

    // second->data = 2;
    // second->next = third;

    // third->data = 3;
    // third->next = NULL;

    // printList(head);
    // cout << ".....";

    // push(&head, 5);
    // printList(head);
    
    append(&head, 6);
    push(&head, 7);
    push(&head, 1);
    append(&head, 4);
    insertAfer(head->next, 8);

    cout<<"ll rn is: ";
    printList(head);
    return 0;
}