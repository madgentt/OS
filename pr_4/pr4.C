using namespace std;
#include <iostream>
#include <fstream>
#include <time.h>

int main()
{
	clock_t tStart = clock(); // начальное время
	long long int a = 0;
	int  b = 3;
	int  c = 3;
	for (int i = 0; i < 100000000; i++)
	{
		a =a + ( b * 2) + c - i;
	}

	ofstream out("result.txt", ios::app);
	if (out.is_open())
	{
		out <<"a = "<< a<< "	In C++ it take:	"<< (double)(clock()-tStart)/CLOCKS_PER_SEC <<"sec"<< endl;
	}
	out.close();

	return 0;
}
