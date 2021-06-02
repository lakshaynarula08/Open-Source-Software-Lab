# include <stdio.h>
# include <string.h>
   
int main( )
{
  
    
    FILE *filePointer ;
    char Written[50] = "Lakshay Narula B.Tech CSE 3rd Year";
	filePointer = fopen("osslab.c", "w") ;
     if ( filePointer == NULL )
    {
		printf( "osslab.c file failed to open." ) ;
    }
    else
    {
		printf("The file is now opened.\n")       
        
        if ( strlen (Written) > 0 )
        {
             fputs(Written, filePointer) ;   
            fputs("\n", filePointer) ;
        }
          fclose(filePointer) ;
          
        printf("Data successfully written in file osslab.c\n");
        printf("The file is now closed.") ;
    }
    return 0;        
}