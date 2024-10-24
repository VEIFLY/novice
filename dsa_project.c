#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct inventory
{
    int id;
    char nm[50];
    int qty;
    struct inventory *nadr;
};
struct inventory *head, *ptr, *pptr;


void view()
{
    ptr=head;
    if(ptr==NULL)
        printf("Inventory is empty.");
    else 
    {
        printf("\nINVENTORY :>>");
        printf("\n|\tID\t|\tNAME\t|\tQTY\t|");
        printf("\n-------------------------------------------------");
        while(ptr!=NULL)
        {
            printf("\n|\t%d\t|\t%s\t|\t%d\t|",ptr->id,ptr->nm,ptr->qty);
            ptr=ptr->nadr;
        }
    }   
}


void add()
{
    int n,id,qty,mfg,exp;
    char nm[50];
    printf("Enter the no.of items: ");
    scanf("%d", &n);
    for (int i=1; i<=n;i++)
    {
    if (head==NULL)
    {
        head=(struct inventory*)malloc(sizeof(struct inventory));
        printf("\nItem 1 Details:->");
        printf("\nID: ");
        scanf("%d", &id);
        printf("Item Name: ");
        scanf("%s", &nm);
        printf("Item Quantity: ");
        scanf("%d", &qty);
        head->id=id;
        strcpy(head->nm,nm);
        head->qty=qty;
        ptr=head;
    }
    else 
        {
            struct inventory *new=(struct inventory*)malloc(sizeof(struct inventory));
            if (new==NULL)
                printf("Memory cannot beallocated.Not enough space :(");
            else 
            {
                printf("\nItem %d Details:->",i);
                printf("\nID: ");
                scanf("%d", &id);
                printf("Item Name: ");
                scanf("%s", &nm);
                printf("Item Quantity: ");
                scanf("%d", &qty);
                new->id=id;
                strcpy(new->nm,nm);
                new->qty=qty;
                new->nadr=NULL;
                ptr->nadr=new;
            }
        }
    }
    }


void search()
{
    int i,c=0;
    printf("\nEnter the Item's ID: ");
    scanf("%d", &i);
    ptr=head;
    while (ptr->id!=i)
    {
        if (ptr->nadr!=NULL)
            ptr=ptr->nadr;
        else if (ptr->nadr==NULL)
        {
            printf("Item not found in Inventory.");
            return;
        }
    }
    printf("\nItem Found");
    printf("\nDetails:->");
    printf("\n|\tID\t|\tNAME\t|\tQTY\t|");
    printf("\n---------------------------------------------");
    printf("\n|\t%d\t|\t%s\t|\t%d\t|",ptr->id,ptr->nm,ptr->qty);
}

void update()
{
    int i,u,c=0;
    char ch[10],su[50];
    printf("Enter the Item's ID: ");
    scanf("%d", &i);
    ptr=head;
    while(ptr->id!=i)
    {
        if (ptr->nadr!=NULL)
            ptr=ptr->nadr;
        else if (ptr->nadr==NULL)
        {
            printf("Item not found in Inventory.");
            return ;
        }
    }
            printf("Enter the field you wish to change: ");
            scanf("%s", &ch);
            if (strcmp(ch,"ID")==0)
            {
                printf("Udated ID: ");
                scanf("%d",&u);
                ptr->id=u;
            }
            else if (strcmp(ch,"NAME")==0)
            {
                printf("Udated Name: ");
                scanf("%s",&su);
                strcpy(ptr->nm,su);
            }
            else if (strcmp(ch,"QTY")==0)
            {
                printf("Udated Quantity: ");
                scanf("%d",&u);
                ptr->qty=u;
            }
            else 
                printf("Ivlaid input. Please enter a valid field.");
    }


void delete()
{
    int i;
    printf("Enter the Item's ID: ");
    scanf("%d", &i);
    ptr=head;
    pptr=ptr;
    while (ptr->id!=i)
    {
        if (ptr->nadr!=NULL)
            ptr=ptr->nadr;
        else if (ptr->nadr==NULL)
        {
            printf("Item not foundin inventory.");
            return;
        }
    }
    if (ptr==head)
    {
        head=ptr->nadr;
        free(ptr);
    }
    else if (ptr->nadr==NULL)
    {
        free(ptr);
    }
    else
    {
        pptr->nadr=ptr->nadr;
        free(ptr);
    }
}


int main()
{
    int c;
    printf("\n\nWelcome! You've entered VED Corporations Inventory Management System.");
    while (0<1)
    {
    printf("\n\n==============Inventory Management System==============");
    printf("\n              1. View all Items"              );
    printf("\n              2. Add New Item"                );
    printf("\n              3. Search Item"                 );
    printf("\n              4. Update Item Details"         );
    printf("\n              5. Delete Item"                 );
    printf("\n              6. Exit");
    printf("\n{Item's ID are unique}");
    printf("\n\nEnter your choice: ");
    scanf("%d", &c);
    if (c==1) 
        view();
    else if (c==2) 
        add();
    else if (c==3)
        search();
    else if (c==4)
        update();
    else if (c==5)
        delete();
    else if (c==6)
    {
        printf("\nExiting the Program.");
        break;
    }
    else
    printf("\nInvalid choice. Please enter again.");
}
    
}