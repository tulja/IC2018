#include <iostream>
#include <cstdlib>
#include <pthread.h>
#include <cmath>
#include <vector>
#include <mutex>
#include <fstream>
#include <chrono>
#include <ctime>
#include <atomic>
using namespace std;
int number_of_requests=0;
    int i;


void *check_prime_numbers_sam(void *tid)
{
	 const char *str=" while true; do curl 192.168.136.88:8080; done";
	system(str);
}





	

int main () {
   //Declaratons being done here
   int n;        // Declare parameter 'n'
   int rc1;        // Declare variable to store info. of threads
   int rc2;
   int i,j;
   void *status;        // Declaring status for threads
   // Making threads joinable
   pthread_attr_t attr;
   pthread_attr_init(&attr);
   pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);
   // Declare variables start and end to denote times of clock
   std::chrono::time_point<std::chrono::system_clock> start_sam,end_sam,start_dam,end_dam;
   // Declare file input parameter
   ifstream fin("server_data_out.txt");
   int tid[100];       // Declare thread IDs
   pthread_t pthreads[100],pthreads1[100];  //Declare threads
   start_sam=std::chrono::system_clock::now();   // System clock
   // Thread execution for SAM starts here
   while(fin>>number_of_requests)
   {
   		number_of_requests*=18;	
       for(i=0;i<number_of_requests;i++)
        {
            tid[i]=i;
            rc1=pthread_create(&pthreads[i],NULL, check_prime_numbers_sam, &tid[i]);
            if (rc1){
                cout << "Error:unable to create thread," << rc1 << endl;
                exit(-1);
            }
        }
        pthread_attr_destroy(&attr);
        for(int i=0;i<number_of_requests;i++)
        {
        rc1=pthread_join(pthreads[i], &status);
            if (rc1){
                cout << "Error:unable to create thread," << rc1 << endl;
                exit(-1);
            }
        }
    }
   // pthread_exit(NULL);



   pthread_attr_destroy(&attr);
   
   pthread_exit(NULL);

}
