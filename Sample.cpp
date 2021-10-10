#include <fstream>
#include <iostream>
#include <vector>
#include <string> 

using namespace std;

vector<double> regression(ifstream & input1, ifstream& input2)
{
	string data1;
	string data2;
	double var1, var2;
	int i = 0;
	vector<double> data_1;
	vector<double> data_2;
	while(input1 >> data1 and input2 >> data2)
	{
		if (!data1.empty() and !data2.empty())
		{
			var1 = stod(data1);
			var2 = stod(data2);
			data_1.resize(i + 1);
			data_2.resize(i + 1);
			data_1[i] = var1;
			data_2[i] = var2;
			i++;
		}
	}
	int n = data_1.size();
	double Sx = 0, Sy = 0, Sx2 = 0, Sxy = 0;
	for (i = 0; i < n; i++)
	{
		Sx += data_1[i];
		Sx2 += data_1[i] * data_1[i];
		Sxy += data_1[i] * data_2[i];
		Sy += data_2[i];
		
	}
	double a, b, d, c;
	a = (n * Sxy - Sx * Sy) / (n * Sx2 - Sx * Sx);
	b = (Sy - a * Sx) / n;
	vector<double> coef = {a,b};
	return coef;
}

int main()
{
	ifstream x("data_1.txt");
	ifstream y("data_2.txt"); 
	vector<double> coef = regression(x, y);
	cout << "a = " << coef[0] << "; b = " << coef[1] << endl;
	cout << "y = " << coef[0]<< "x" << " + " << coef[1];
}


