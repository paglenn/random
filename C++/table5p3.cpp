// Contains all basic elements of matrix handling 
// Arrays are defined at compile time 
#include<iostream>
using namespace std; 
void sub_1(int row, int col, int vec[], int **matr); 
void **matrix(int row, int col, int num_bytes ); 
void free_matrix(void **matr) ;

int main() {
	int k, m, row,col, total = 0;
	int *vec;												// line a
	int **matr;												// line b
	
	printf("\n\nRead in number of rows = ");				// line c
	scanf("%d",&row);
	printf("\n\nRead in number of column = ");
	scanf("%d",&col);

	vec = new int [col];									// line d 
	matr = (int **)matrix(row,col,sizeof(int));				// line e
	for(k=0; k<col;k++) vec[k] = k; 	// store data in vector[]
	for(m=0; m < row; m++) {			// store data in array[][]
		for(k = 0; k < col; k++)  matr[m][k] = m+10+k;
	}
	
	printf("\n\n Vector data in main(): \n");	// print vector data 
	for(k=0; k<col; k++) printf("vector[%d] = %d ", k, vec[k]) ;
		printf("\n\nMatrix datain main() :");
	for(m=0; m<row; m++){
		printf("\n");
		for(k=0 ;k <col; k++){
			printf("matr[%d][%d] = %d ",m,k,matr[m][k]);
		}
	}
	printf("\n");
	for(m = 0; m < row; m++) {		// access the array
		for(k = 0; k< col; k++) total += matr[m][k];
	}
	printf("\n\nTotal = %d\n", total);
	sub_1(row, col, vec, matr); 							
	free_matrix((void**)matr);								// line f
	delete [] vec; 											// line g
	return 0;
} // end main

void sub_1(int row, int col, int vec[], int **matr) 		//line d 
{ 
	int k, m;

	printf("\n\nVector data in sub_1(): \n");		// print vector data 
	for(k=0; k<col; k++) printf("vector[%d] = %d",k, vec[k]);
	printf("\n\nMatrix data in sub_1():");
	for(m=0; m< row; m++) {
		printf("\n");
		for(k =0; k< col; k++) {
			printf("matr[%d][%d] = %d ", m, k, matr[m][k]);
		}
	}
	printf("\n");
} // end function sub_1()


// The function 
// 		void **matrix()
// reserves dynamic memory for a two-dimensional matrix 
// using the C++ command new. No initialization of the elements. 
// Input data: 
// int row 		 - number of rows 
// int col 		 - number of columns 
// int num_bytes - number of bytes for each element 
//
// Returns a void **pointer to the  reserved memory location. 
//
void **matrix(int row, int col, int num_bytes )
{
	int 	i, num; 
	char 	**pointer, *ptr; 
	pointer = new(nothrow) char * [row]; 
	if(!pointer) {
		cout << "Exception handling : Memory allocation failed" ;
		cout << " for " << row << "row addresses !" << endl;
		return NULL;
	}
	i = (row * col * num_bytes) / sizeof(char) ; 
	pointer[0] = new(nothrow) char [i];
	if(!pointer[0]) {
		cout << "Exception handling : Memory allocation failed" ;
		cout << "for address to " << i << " characters !" << endl; 
		return NULL;
	}
	ptr = pointer[0] ;  
	num = col * num_bytes ; 
	for(i = 0; i< row; i++, ptr += num) {
		pointer[i] = ptr; 
	}
	return (void **) pointer ; 
} // end: function void **matrix()

/* 
 * The function void free_matrix() 
 * releases the memory reserved by the function matrix[][]
 * Input data : 
 * void far ** matr - pointer to the matrix 
 */

void free_matrix(void **matr)
{
	delete [] (char *) matr[0];
}  // End: function free_matrix() 
		
