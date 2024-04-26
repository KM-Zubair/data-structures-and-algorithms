package ProjectJava;

import java.util.*;



public class Main {
	
	 private static final Scanner scanner = new Scanner(System.in);
	 	
	 
	 
	    public static void main(String[] args) {
	        int N = scanner.nextInt();
	        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
	        
	     if (N%2 == 1)
	    	 System.out.println("Alice");
	     else 
	    	 System.out.println("Bob");
	        
	        scanner.close();
	    }
	}
