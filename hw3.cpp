#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>

void comb(int n, std::vector<int>& picked, int toPick, std::vector<std::vector<int>>& result) {
    if (toPick == 0) {
        std::vector<int> tmp(picked.size());
        for (int i = 0; i < picked.size(); ++i) {
            tmp[i] = picked[i];
        }
        result.push_back(tmp);
    }
    int smallest = picked.empty() ? 0 : picked.back() + 1;
    for (int next = smallest; next < n; ++next) {
        picked.push_back(next);
        comb(n, picked, toPick - 1, result);
        picked.pop_back();
    }
}

void print_result(std::vector<std::vector<int>>& result) {
    for (int i = 0; i < result.size(); ++i) {
        for (int j = 0; j < result[i].size(); ++j) {
            if (j > 0)
                std::cout << " ";
            std::cout << result[i][j];
        }
        std::cout << std:: endl;
    }
}

bool comp_vec_size(std::vector<std::pair<int, int>>& vec1, std::vector<std::pair<int, int>>& vec2) {
    return vec1.size() < vec2.size();
}

std::vector<bool> encode_edge(std::vector<std::vector<int>>& board, std::pair<int, int>& p, int n) {
    std::vector<bool> encoded = std::vector<bool>(n, false);
    if (board[p.first][p.second] >= 0 || board[p.second][p.first] >= 0)
        encoded[board[p.first][p.second]] = true;
    return encoded;
}

std::vector<bool> encode_cycle(std::vector<std::vector<int>>& board, std::vector<std::pair<int, int>>& cycle, int n) {
    std::vector<bool> final_encoded = std::vector<bool>(n, false);
    for (int i = 0; i < cycle.size(); ++i) {
        std::vector<bool> encoded = encode_edge(board, cycle[i], n);
        for (int j = 0; j < n; ++j)
            final_encoded[j] = final_encoded[j] | encoded[j];
    }
    return final_encoded;
}

bool encoded_vec_equal(std::vector<bool>& vec1, std::vector<bool>& vec2) {
    int vec1_size = vec1.size();
    int vec2_size = vec2.size();
    if (vec1_size != vec2_size)
        return false;
    for (int i = 0; i < vec1_size; ++i) {
        if (vec1[i] != vec2[i])
            return false;
    }
    return true;
}

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

    std::vector<std::vector<int>> cycles;

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



                            std::vector<int> vec;
                            for(j=0;j<=no;j++)
                                vec.push_back(order[i][j]);
                            vec.push_back(order[i][0]);
                            cycles.push_back(vec);
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

    /*
    for (i = 0; i < cycles.size(); ++i) {
        for (j = 0; j < cycles[i].size(); ++j) {
            std::cout << cycles[i][j] << "->";
        }
        std::cout << cycles[i][0] << std::endl;
    }
    std::cout << cycles.size() << " cycles" << std::endl;
    */

    std::vector<std::vector<std::pair<int, int>>> edges;
    for (i = 0; i < cycles.size(); ++i) {
        std::vector<std::pair<int, int>> edges_tmp;
        for (j = 0; j < cycles[i].size() - 1; ++j) {
            std::pair<int, int> p;
            p.first = cycles[i][j];
            p.second = cycles[i][j + 1];
            edges_tmp.push_back(p);
        }
        edges.push_back(edges_tmp);
    }

    /*
    for (i = 0; i < edges.size(); ++i) {
        std::cout << "Cycle " << i + 1 << ":" << std::endl;
        for (j = 0; j < edges[i].size(); ++j) {
            std::cout << "(" << edges[i][j].first << ", " << edges[i][j].second << ")" << std::endl;
        }
    }
    */

    int encodes = 0;
    std::vector<std::vector<int>> edge_id_board(nodenum, std::vector<int>(nodenum, -1));
    for (i = 0; i < edges.size(); ++i) {
        for (j = 0; j < edges[i].size(); ++j) {
            if (edge_id_board[edges[i][j].first][edges[i][j].second] < 0 || edge_id_board[edges[i][j].second][edges[i][j].first] < 0) {
                edge_id_board[edges[i][j].first][edges[i][j].second] = encodes;
                edge_id_board[edges[i][j].second][edges[i][j].first] = encodes;
                ++encodes;
            }
        }
    }

    /*
    for (i = 0; i < edge_id_board.size(); ++i) {
        for (j = 0; j < edge_id_board[i].size(); ++j) {
            if (j != 0)
                std::cout << "\t";
            std::cout << edge_id_board[i][j];
        }
        std::cout << std::endl;
    }
    std::cout << encodes << std::endl;
    */

    /*
    for (i = 0; i < edges.size(); ++i) {
        std::cout << "Cycle " << i + 1 << ":" << std::endl;
        for (j = 0; j < edges[i].size(); ++j) {
            std::cout << "(" << edges[i][j].first << ", " << edges[i][j].second << ")" << std::endl;
        }
    }
    */

    std::vector<std::vector<bool>> encoded_cycles(edges.size(), std::vector<bool>(encodes));
    for (i = 0; i < edges.size(); ++i) {
        std::vector<bool> encoded_cycle = encode_cycle(edge_id_board, edges[i], encodes);
        for (j = 0; j < encodes; ++j) {
            encoded_cycles[i][j] = encoded_cycle[j];
        }
    }

    /*
    for (i = 0; i < encoded_cycles.size(); ++i) {
        for (j = 0; j < encoded_cycles[i].size(); ++j) {
            std::cout << encoded_cycles[0][j];
        }
        std::cout << std::endl;
    }
    */

    int required = encodes - nodenum + 1;
    int current_selected = 0;
    std::vector<int> cycle_indexes(required);
    std::vector<std::vector<bool>> selected_encoded_cycles(required, std::vector<bool>(encodes));
    std::vector<int> picked;
    std::vector<std::vector<int>> result; //Cn取k的結果

    for (i = 0; i < encoded_cycles.size(); ++i) {
        if (current_selected < 2) {
            for (j = 0; j < encoded_cycles[i].size(); ++j) {
                selected_encoded_cycles[current_selected][j] = encoded_cycles[i][j];
            }
            cycle_indexes[current_selected] = i;
            ++current_selected;
            if (current_selected >= required)
                break;
        }
        else {
            //Cn取k的k => j
            bool all_zero = true;
            for (j = 2; j <= current_selected; ++j) {
                result.clear();
                picked.clear();
                comb(current_selected, picked, j, result);

                for (int x = 0; x < result.size(); ++x) {
                    //Init a tmp 01 encoded cycle for checking all 0
                    std::vector<bool> c_cycle(encodes);
                    for (int z = 0; z < encodes; ++z) {
                        c_cycle[z] = selected_encoded_cycles[result[x][0]][z];
                    }
                    //
                    for (int y = 1; y < j; ++y) {
                        for (int z = 0; z < encodes; ++z) {
                            c_cycle[z] = c_cycle[z] ^ selected_encoded_cycles[result[x][y]][z];
                        }
                    }
                    //
                    for (int z = 0; z < encodes; ++z) {
                        c_cycle[z] = c_cycle[z] ^ encoded_cycles[i][z];
                    }
                    //Check
                    all_zero = true;
                    for (int z = 0; z < encodes; ++z) {
                        if (c_cycle[z]) {
                            all_zero = false;
                            break;
                        }
                    }
                    if (all_zero)
                        break;
                }
                if (all_zero)
                    break;
            }
            if (all_zero)
                continue;
            for (int z = 0; z < encodes; ++z) {
                selected_encoded_cycles[current_selected][z] = encoded_cycles[i][z];
            }
            cycle_indexes[current_selected] = i;
            ++current_selected;
            if (current_selected >= required)
                break;
        }
    }
    
    /*
    for (i = 0; i < 16; ++i) {
        for (j = 0; j < encodes; ++j) {
            std::cout << selected_encoded_cycles[i][j];
        }
        std::cout << std::endl;
    }
    */

    /*
    for (i = 0; i < current_selected; ++i) {
        std::cout << cycle_indexes[i] << std::endl;
    }
    */

    for (i = 0; i < current_selected; ++i) {
        std::cout << "Weight: " << edges[cycle_indexes[i]].size() << " => ";
        for (j = 0; j < edges[cycle_indexes[i]].size(); ++j) {
            std::cout << edges[cycle_indexes[i]][j].first << "->";
        }
        std::cout << edges[cycle_indexes[i]][0].first << std::endl;
    }
}
