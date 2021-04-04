import java.io.*;
public class Main
{
	public static void main(String[] args) throws Exception {
		long startTime = System.currentTimeMillis();
	    	long a = 0;
	    	int b = 3;
	    	int c = 3;
		for(int i = 0;i<100000000;i++)
		{
		    a = a + b*2 +c -i; 
		}
		long stopTime = System.currentTimeMillis();
	    	FileWriter writer = new FileWriter("result.txt", true);
	    	String text = "a = " + a +"	In java it take: " +(double)(stopTime - startTime)/100 + "sec\n" ;
        	writer.write(text);
		writer.close();
	}
}
