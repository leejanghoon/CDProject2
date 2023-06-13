#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main(void) {
	FILE* fp;// = fopen("vid_1.txt", "rt");
	FILE* fwp = fopen("output1.txt", "wt");
	//int idx = 1;
	char str[1024];
	char filename[30] = "vid4_";
	char temp[30];
	//fgets(str, 1024, fp);
	for (int i = 1001; i <=1014 ; i++) {
		sprintf(temp, "%d", i);

		strcat(filename, temp);
		strcat(filename, ".txt");
		printf("%s\n", filename);
		fp = fopen(filename, "rt");
		while (1) {
			fgets(str, 1024, fp);
			
			if (feof(fp))
				break;
			fprintf(fwp, "%d ", i);
			fprintf(fwp, "%s", str);
			//printf("%d ", i);
			//printf("%s", str);
		}
		strcpy(filename, "vid4_");
	}

	return 0;
}