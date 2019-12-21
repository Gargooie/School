FILE *ptr;
int a[10];
int b[10];
int c;

for (c=0;c<10;c++){
    a[c] =c;
};

ptr = fopen("datafile.bin", "wb");
fwrite(a, sizeof(a[0]), sizeof(a)/sizeof(a[0]),ptr);
fclose(ptr);

ptr = fopen("datafile.bin", "rb");
fread(b,sizeof(a[0]), sizeof(a)/sizeof(a[0]),ptr);

fclose(ptr);

 for (c=0;c<10;c++){
     printf("%d", b[c]);
};
