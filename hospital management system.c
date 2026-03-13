#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Patient node structure
struct Patient {
    int patientID;           // Unique patient ID
    char name[50];          // Patient name
    int psi;                // Patient Severity Index
    int height;             // AVL height
    struct Patient *left, *right;
};

// Utility functions
int max(int a, int b) { return (a > b) ? a : b; }
int height(struct Patient* node) { return node ? node->height : 0; }
int balanceFactor(struct Patient* node) { return node ? height(node->left) - height(node->right) : 0; }
void updateHeight(struct Patient* node) { node->height = max(height(node->left), height(node->right)) + 1; }

// Right rotation for AVL
struct Patient* rightRotate(struct Patient* y) {
    struct Patient* x = y->left;
    struct Patient* T2 = x->right;
    x->right = y;
    y->left = T2;
    updateHeight(y);
    updateHeight(x);
    return x;
}

// Left rotation for AVL
struct Patient* leftRotate(struct Patient* x) {
    struct Patient* y = x->right;
    struct Patient* T2 = y->left;
    y->left = x;
    x->right = T2;
    updateHeight(x);
    updateHeight(y);
    return y;
}

// Insert patient with AVL balancing
struct Patient* insertBST(struct Patient* root, int patientID, char name[], int psi) {
    if (!root) {
        struct Patient* newNode = (struct Patient*)malloc(sizeof(struct Patient));
        newNode->patientID = patientID;
        strcpy(newNode->name, name);
        newNode->psi = psi;
        newNode->left = newNode->right = NULL;
        newNode->height = 1;
        return newNode;
    }
    if (patientID < root->patientID)
        root->left = insertBST(root->left, patientID, name, psi);
    else if (patientID > root->patientID)
        root->right = insertBST(root->right, patientID, name, psi);
    else
        return root; // Duplicate ID

    updateHeight(root);
    int bf = balanceFactor(root);
    // Left-Left case
    if (bf > 1 && patientID < root->left->patientID)
        return rightRotate(root);
    // Right-Right case
    if (bf < -1 && patientID > root->right->patientID)
        return leftRotate(root);
    // Left-Right case
    if (bf > 1 && patientID > root->left->patientID) {
        root->left = leftRotate(root->left);
        return rightRotate(root);
    }
    // Right-Left case
    if (bf < -1 && patientID < root->right->patientID) {
        root->right = rightRotate(root->right);
        return leftRotate(root);
    }
    return root;
}

// Inorder traversal with PSI priority
void priorityInorder(struct Patient* root) {
    if (root) {
        priorityInorder(root->left);
        if (root->psi >= 3)
            printf("Priority Patient: ID: %d, Name: %s, PSI: %d\n", root->patientID, root->name, root->psi);
        else
            printf("ID: %d, Name: %s, PSI: %d\n", root->patientID, root->name, root->psi);
        priorityInorder(root->right);
    }
}

// Main function
int main() {
    struct Patient* root = NULL;
    root = insertBST(root, 101, "John Doe", 5);    // Critical, 2 hrs
    root = insertBST(root, 102, "Jane Smith", 3);  // Moderate, 1 hr
    root = insertBST(root, 103, "Alice Brown", 1); // Stable, 0 hr
    printf("Patient Records (Priority Inorder):\n");
    priorityInorder(root);
    return 0;
}