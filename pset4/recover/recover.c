#include<stdio.h>
#include <stdlib.h>




int main(int argc, char *argv[])
{
    //Accept only 1 command line argument
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }

    // Open memory card file
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    { 
        printf("Could not open.\n"); 
    }

    // Set counter 
    int found_images = 0;
    
    // Set counter 
    int count_files = 0;
    
    // Buffer to store images
    unsigned char buffer[512]; 
    
    // File for images
    FILE *image = NULL;
    
    // Set filename 
    char filename[8]; 
    
    // Read from file
    while (fread(buffer, 512, 1, file) == 1) 
    
        // Check if the image is JPG
    {
        if (buffer[0] == 0xff
            && buffer[1] == 0xd8
            && buffer[2] == 0xff
            && (buffer[3] & 0xf0) == 0xe0)
        {
            if (found_images == 1) 
            {
                fclose(image);
                
            }
            else 
            { 
                found_images = 1;
                
            }
            // Print filename
            sprintf(filename, "%03i.jpg", count_files); 
            // Open image file to write in
            image = fopen(filename, "w"); 
            // Increment counter
            count_files++; 
        }
        
        if (found_images == 1) 
        {
            fwrite(&buffer, 512, 1, image);
        }
    }
    
    fclose(file); 
    fclose(image);

    return 0;
}