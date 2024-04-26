

import java.util.*;
import java.util.regex.*;



public class Main {
	
	 private static final Scanner scanner = new Scanner(System.in);
	 	
	 
	 
	    public static void main(String[] args) {
	        int T = scanner.nextInt();
	        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
	        
	        String [] array = new String[T];
	        
	    for (int i = 0; i < array.length ; i++) {
	    	 array [i] = scanner.next(); 
	    } 
	    
	    
	    //Creating a pattern Object
	    Pattern p = Pattern.compile("4", Pattern.LITERAL);
	    
	    //Creating a matcher object
	    Matcher m;
	    
	    for (int i = 0; i < array.length; i++) {
	    	int count = 0, startIndex = 0;
	    	
	    
	    	m = p.matcher(array[i]);
	    	while (m.find(startIndex)) {
	    		count++; 
	    		startIndex = m.start() + 1;
	    	}
	    	
	    	
	    	System.out.println(count);
	    }
	        
	        scanner.close();
	    }
	}
