// Contains all basic elements of matrix handling 
// Arrays are defined at compile time 
#include<iostream>

void sub_1(int row, int col, int vec[], int matr[][5]); 

int main() {
	int k, m, row=  3, col = 5;
	int vec[5];												//line a
	int matr[3][5];											//line b
	
	for(k=0; k<col;k++) vec[k] = k; 
	for(m=0; m < row; m++) {
		for(k = 0; k < col; k++)  matr[m][k] = m+10+k;
	}
	
	printf("\n\n Vector data in main(): \n");
	for(k=0; k<col; k++) printf("vector[%d] = %d ", k, vec[k]) ;
		printf("\n\nMatrix datain main() :");
	for(m=0; m<row; m++){
		printf("\n");
		for(k=0 ;k <col; k++){
			printf("matr[%d][%d] = %d ",m,k,matr[m][k]);
		}
	}
	printf("\n");
	sub_1(row, col, vec, matr); 							// line c
	return 0;
} // end main

void sub_1(int row, int col, int vec[], int matr[][5]) 		//line d 
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
