#include<stdio.h>
#include<stdlib.h>

int main(int argc,char *argv[])
{
    int i,j;

    FILE *fp;
    char newline[10],*tempch=" ";
    int nodenum,edgenum,cost,begin,end;

	fp=fopen("cost239","r");
	fgets(newline,10,fp);

	sscanf(newline,"%i %i",&nodenum,&edgenum);

    int A[nodenum][nodenum];//�x�s�s�u���I
    for(i=0;i<nodenum;i++)
        for(j=0;j<nodenum;j++)
            A[i][j]=0;
    while(fgets(newline,10,fp) != NULL)
	{
	   sscanf(newline,"%i %i %i",&begin,&end,&cost);
	   A[begin][end]=1;
	   A[end][begin]=1;
	}
	fclose(fp);

            int r,f;
   /*         for(r=0;r<nodenum;r++)
               {
                    for(f=0;f<nodenum;f++)
                        printf("%d ",A[r][f]);
                    printf("\n");
               }printf("\n");
*/


    int k,c,pre,no;//��no��
    int b=0;//��b��temp(�h�X�Ӫ��ƦC�զX)
    int s=0,e=nodenum,cycle=0;
    int temp[nodenum];
    int order[20000][nodenum];//�w�]��-1
    int check_re[20000];
    int check_cycle[nodenum];
    for(i=0;i<20000;i++)
        for(j=0;j<nodenum;j++)
            order[i][j]=-1;
    for(i=0;i<nodenum;i++)
        order[i][0]=i;
    int adde;
    int t;//��j�p�ɪ�temp
    int smallest,compare;
    int m,n;

    for(no=1;no<nodenum;no++)//�]�wno
    {


        adde=0;
        s=0;
        for(k=0;k<e;k++)//��e���[���s�u(e�w�]��nodenum)
        {
           s=s+b;
           b=0;
           pre=order[s][no-1];//pre�O�e�@�ӳ��I
           for((i=order[s][0]+1);i<nodenum;i++)//i=pre+1�ק�ק�ק�ק�ק�ק�ק�ק�ק�ק�ק�
           {
              if(A[pre][i]==1)
              {
                for(j=1;j<(no-1);j++)//for�j�� �ˬd���S�����ƪ����I
                {
                    if(order[s][j]==i)
                    {
                        j=-1;
                        break;
                    }
                }
                if(j!=-1)
                    temp[b++]=i;//b�p��h�X�Ӫ��ƦC�զX
              }
           }
           c=0;

           if(b>0)
           {
               adde=adde+b-1;
               for(i=e+adde;i>s;i--)//���Ჾ (���:e->e+adde)
               {
                  for(j=0;j<no;j++)
                      order[i+b-1][j]=order[i][j];
               }
               for(i=s;i<(s+b);i++)//�ɤW&�s�s�u
               {
                   order[i][no]=temp[c++];
                   for(j=0;j<no;j++)
                       order[i][j]=order[s][j];

                   //�ˬdcycle
                   if(no>1&&A[order[i][no]][order[i][0]]==1)
                   {

                       for(m=0;m<=no;m++)
                           check_cycle[m]=order[i][m];

                       compare=0;//�ˬd�O�_���ϧ�

                       for(m=1;m<=no;m++)
                           compare=compare*10+check_cycle[m];
                       compare=compare*10+check_cycle[0];

                       check_re[i]=0;
                       for(m=no;m>=0;m--)
                           check_re[i]=check_re[i]*10+check_cycle[m];

                       for(m=0;m<i;m++)
                       {
                           if(check_re[m]==compare)
                           {
                               m=-1;
                               break;
                           }
                       }
                       if(m!=-1)
                       {
                            /*fp=fopen("cycle.txt","w");
 for(j=0;j<=no;j++)
fprintf("%d->",order[i][j]);
fprintf("%d",order[i][0]);
fprintf("\n");
fclose(fp);*/




                            for(j=0;j<=no;j++)
                                printf("%d->",order[i][j]);
                            printf("%d",order[i][0]);
                            printf("\n");
                            cycle++;
                       }

                   }
               }
           }
           else//b==0
           {
               for(i=s;i<e+adde;i++)//���e��1��
               {
                  for(j=0;j<=no;j++)
                      order[i][j]=order[i+1][j];
               }
               adde--;
           }
        }
        e=e+adde;

    }
    printf("%d cycles",cycle);
    getchar();
}
