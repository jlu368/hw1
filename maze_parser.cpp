#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

class Node {
	Node left;
	Node right;
	Node top;
	Node bottom;
	bool point;

	public Node(){
		left = right = top = bottom = NULL;
		point = false;	
	}	
}


int main()
{
 ifstream myfile;
 myfile.open("medium_maze.txt");
 string curr = ""; 
 string prev = "";
 string after = "";
 int width = 0;

 if (myfile.is_open()) 
 {
   getline(myfile, curr);
   width = curr.length();
   vector< vector<Node> >* maze = new vector< vector<Node> >(width);
   maze.push(new vector<Node>);
   for(int i = 0; i < cuu.length(); i++)
   {

   }

   getline(myfile, after);
   while (!myfile.eof()) {
   	 prev = curr;
   	 curr = after;
     getline(myfile, after);
    
     //=============================


     for(int index = 1; index < curr.length()-1; index++)
     {
        Node *temp = new Node();
        if(curr[index] == '%')
        	temp->wall = true;
        	prev[index]->wall
     }


     //==============================
     //cout << output << endl;
   } 
  }
  myfile.close(); 
  
  




return 0;
}
