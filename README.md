1. *********solution *********


#include <iostream>

using namespace std;

int main()
{

   int n;
   
   cout<<"Enter the N"<<endl;
   
   cin>>n;
   
   int sum=0;
   
   if(n>0)
   {
       
       sum=n*(n+1)/2;
   }
   
  /* 
   for(int i=1;i<=n;i++)
   {
      cout<<i<<", ";
      
      // sum+=i;
       
       
       
   }
*/

  cout<<"||Sum : "<<sum;

    return 0;
}




2. *************Solution ************


#include <iostream>

using namespace std;

int main()
{
  
   int n;
   
   cout<<"Enter the number "<<endl;
   cin>>n;
   
   int count=0;
   
   while(n!=0)  
   {  
       n=n/10;  
       count++;  
   }  
   
   cout<<"Total digits: "<<count<<endl;
   
      return 0;
}


3. solution 


#include <iostream>
using namespace std;

class Overloading1 {
   
    float pi = 3.14f;

public:
    
    void area(int l, int b, int h) {
        int rect_area = l * b * h;
        cout << "Area of rectangle is: " << rect_area << endl;
    }

    
    void area(int radius) {
        float circle_area = pi * radius * radius;
        cout << "Area of circle is: " << circle_area << endl;
    }

  
    void area(int b, int h) {
        float triangle_area = 0.5 * b * h;
        cout << "Area of triangle is: " << triangle_area << endl;
    }
};

int main() {
   
    Overloading1 obj1;
    obj1.area(2, 3, 4);         
    obj1.area(10);              
    obj1.area(20, 30);     

    return 0;
}


4. solution 


#include <iostream>
using namespace std;


int main() {
   
   int n;
   
   cout<<"Enter the number: "<<endl;
   cin>>n;
   
   for(int i=1;i<=10;i++){
       
       cout<<" "<<n<<" * "<<i<<" = "<<n*i<<endl;
       
   }
   
  
  
    return 0;
}


5. solution 



#include <iostream>

using namespace std;

int main()
{
  
   int n;
   
   cout<<"Enter the number "<<endl;
   cin>>n;
   
  
   int rev=0;
   
   while(n>0)  
   {  
       
       rev=rev*10+n%10;
        
        n=n/10;   
    
   }  
   
   cout<<"Total digits: "<<rev<<endl;
   
      return 0;
}


6. solution 

#include <iostream>

using namespace std;

class salaryCal {

    public:
    
    void calSalary(int baseSalary) 
    {
    
        cout << "Intern's Salary: " << baseSalary << endl;
    }

    
    void calSalary(int baseSalary, int bonus)
    {
    
        int totalSalary = baseSalary + bonus;
    
        cout << "Regular Employee's Salary: " << totalSalary << endl;
    }

    
    void calSalary(int baseSalary, int bonus, int performanceIncentive)
    {
    
        int totalSalary = baseSalary + bonus + performanceIncentive;
    
        cout << "Manager's Salary: " << totalSalary << endl;
    }

};


int main() {
    
    salaryCal cal;

    cal.calSalary(10000);
    cout<<"\n";
    cal.calSalary(30000, 15000); 
    cout<<"\n";
    cal.calSalary(60000, 10000, 15000); 

    return 0;
}


7. solution *********************


#include <iostream>
using namespace std;

class Base {
public:
    int rollno;
    string name;

    Base(int r, string n) {
        rollno = r;
        name = n;
    }

    void display1() {
        cout << "**** Student Details *****" << endl;
        cout << "Name: " << name << ", Roll No.: " << rollno << endl;
    }
};

class child : public Base {
public:
    int maths, DSA, Java;
    int total;
    float percentage;

    child(int r, string n, int m, int d, int j) : Base(r, n) {
        maths = m;
        DSA = d;
        Java = j;
    }

    void display2() {
        total = maths + DSA + Java;
        percentage = total / 3.0; // Ensure floating-point division
        cout << "Total Marks: " << total << ", Percentage: " << percentage << "%" << endl;
    }
};

int main() {
    int rollno;
    string name;
    int m, d, j;

    cout << "Enter the Roll No: ";
    cin >> rollno;

    cout << "Enter the Name: ";
    cin.ignore(); // Clear input buffer
    getline(cin, name);

    cout << "Enter the marks for Maths, DSA, and Java: ";
    cin >> m >> d >> j;

    // Create an object of the derived class
    child student(rollno, name, m, d, j);

    // Display details
    student.display1();
    student.display2();

    return 0;
}


*****************


/*create the program that demonstrates polymorphism by calculating the area of different shapes using a base class shape 
and drived classes for circle, rectangle and triangle each drived class should override a virtual function to compute the 
area of respective shape. the program should accept radius of the cirle , L and B for a rect and base and height for a triangle 

*/

#include <iostream>
#include <cmath>
using namespace std;

class Shape {
public:
    virtual double calculateArea() = 0;
    virtual ~Shape() {}
};

class Circle : public Shape {
private:
    double radius;
public:
    Circle(double r) : radius(r) {}
    double calculateArea() override {
        return M_PI * radius * radius;
    }
};

class Rectangle : public Shape {
private:
    double length;
    double breadth;
public:
    Rectangle(double l, double b) : length(l), breadth(b) {}
    double calculateArea() override {
        return length * breadth;
    }
};

class Triangle : public Shape {
private:
    double base;
    double height;
public:
    Triangle(double b, double h) : base(b), height(h) {}
    double calculateArea() override {
        return 0.5 * base * height;
    }
};

int main() {
    double r, l, b, base, height;

    cout << "Radius of circle: ";
    cin >> r;
    
    Shape* circle = new Circle(radius);

    cout << "Length and breadth of rectangle: ";
    cin >> l >> b;
    
    Shape* rectangle = new Rectangle(length, breadth);

    cout << "Base and height of triangle: ";
    cin >> base >> height;
    
    Shape* triangle = new Triangle(base, height);

    cout << "Area of Circle: " << circle->calculateArea() << endl;
    cout << "Area of Rectangle: " << rectangle->calculateArea() << endl;
    cout << "Area of Triangle: " << triangle->calculateArea() << endl;

    delete circle;
    delete rectangle;
    delete triangle;

    return 0;
}

9. solution **********


#include <iostream>

using namespace std;


class matrix_operation{
    
public:    

void operate(int A[10][10], int B[10][10], int result[10][10], int rows, int cols) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            result[i][j] = A[i][j] + B[i][j];
        }
    }
}

void operate(int A[10][10], int B[10][10], int result[10][10], int rowsA, int colsA, int rowsB, int colsB) {
    if (colsA != rowsB) {
        throw invalid_argument("Number of columns in A must equal number of rows in B for multiplication.");
    }

    for (int i = 0; i < rowsA; ++i) {
        for (int j = 0; j < colsB; ++j) {
            result[i][j] = 0; 
            for (int k = 0; k < colsA; ++k) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

void printMatrix(int matrix[10][10], int rows, int cols) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}

};

int main() {
    
    
    matrix_operation op;
    
    int A[10][10] = {{1, 2, 3}, {4, 5, 6}};
    int B[10][10] = {{7, 8, 9}, {10, 11, 12}};
    int sum[10][10]; 

    op.operate(A, B, sum, 2, 3);
    cout << "Matrix Addition Result:" << endl;
    op.printMatrix(sum, 2, 3);

    int C[10][10] = {{1, 2}, {3, 4}, {5, 6}};
    int D[10][10] = {{7, 8, 9}, {10, 11, 12}};
    int product[10][10]; 

    op.operate(C, D, product, 3, 2, 2, 3);
    cout << "Matrix Multiplication Result:" << endl;
    op.printMatrix(product, 3, 3);

    return 0;
}

10. Solution **********

#include <iostream>
#include <string>

using namespace std;


class Account {
protected:
    string accountHolder;
    double balance;

public:
    Account(string name, double initialBalance) : accountHolder(name), balance(initialBalance) {}

    virtual void calculateInterest() = 0; 

    void displayBalance() {
        cout << "Account Holder: " << accountHolder << endl;
        cout << "Current Balance: " << balance << endl;
    }
};


class SavingsAccount : public Account {
private:
    double interestRate; 
    double time;         

public:
    SavingsAccount(string name, double initialBalance, double rate, double t)
        : Account(name, initialBalance), interestRate(rate), time(t) {}

    void calculateInterest() override {
        double interest = balance * interestRate * time;
        balance += interest;
        cout << "Interest added to Savings Account: " << interest << endl;
    }
};


class CurrentAccount : public Account {
private:
    double maintenanceFee;
public:
    CurrentAccount(string name, double initialBalance, double fee)
        : Account(name, initialBalance), maintenanceFee(fee) {}

    void calculateInterest() override {
        balance -= maintenanceFee;
        cout << "Maintenance fee deducted from Current Account: " << maintenanceFee << endl;
    }
};

int main() {
    
    SavingsAccount savings("Gautam", 5000.0, 0.10, 1); 
    savings.displayBalance();
    savings.calculateInterest();
    savings.displayBalance();

    cout << endl;

    
    CurrentAccount current("Ayush", 2500.0, 50.0); 
    current.displayBalance();
    current.calculateInterest();
    current.displayBalance();

    return 0;
}
