#include <stdio.h>
#include <string.h>

#define MAX_KEYBOARDS 10

// Define the keyboard struct
struct Keyboard {
    char brand[50];
    char model[50];
    int switches; // Number representing the type of switches (e.g., 1 for Cherry MX Red, 2 for Cherry MX Blue, etc.)
    float price;
};

// Function to add a keyboard to the collection
void addKeyboard(struct Keyboard collection[], int *count) {
    if (*count < MAX_KEYBOARDS) {
        struct Keyboard newKeyboard;

        printf("Enter the brand: ");
        scanf("%s", newKeyboard.brand);

        printf("Enter the model: ");
        scanf("%s", newKeyboard.model);

        printf("Enter the switches (1-Red, 2-Blue, etc.): ");
        scanf("%d", &newKeyboard.switches);

        printf("Enter the price: ");
        scanf("%f", &newKeyboard.price);

        collection[*count] = newKeyboard;
        (*count)++;

        printf("Keyboard added successfully!\n");
    } else {
        printf("Collection is full. Cannot add more keyboards.\n");
    }
}

// Function to display all keyboards in the collection
void displayKeyboards(struct Keyboard collection[], int count) {
    printf("\n--- Keyboard Collection ---\n");
    for (int i = 0; i < count; i++) {
        printf("Keyboard %d:\n", i + 1);
        printf("Brand: %s\n", collection[i].brand);
        printf("Model: %s\n", collection[i].model);
        printf("Switches: %d\n", collection[i].switches);
        printf("Price: $%.2f\n", collection[i].price);
        printf("--------------------------\n");
    }
}


int main() {
    struct Keyboard keyboardCollection[MAX_KEYBOARDS];
    int count = 0;
    int choice;

    while (1) {
        printf("\nMenu:\n");
        printf("1. Add a keyboard to the collection\n");
        printf("2. Display all keyboards in the collection\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                addKeyboard(keyboardCollection, &count);
                break;
            case 2:
                displayKeyboards(keyboardCollection, count);
                break;
            case 3:
                printf("Exiting program.\n");
                return 0;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    }

    return 0;
}
